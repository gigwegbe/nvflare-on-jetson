# Copyright (c) 2023, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

import torch
from simple_network import SimpleNetwork
from torch import nn
from torch.optim import SGD
from torch.utils.data.dataloader import DataLoader
from torchvision.datasets import CIFAR10
from torchvision.transforms import Compose, Normalize, ToTensor

import nvflare.client as flare
from nvflare.client.tracking import SummaryWriter

DATASET_PATH = "/tmp/nvflare/data"


def main():
    batch_size = 32 # Your updated batch size from the logs
    epochs = 5
    lr = 0.01
    model = SimpleNetwork()
    # Using CUDA if available (good for Jetson), otherwise CPU
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    loss = nn.CrossEntropyLoss()
    optimizer = SGD(model.parameters(), lr=lr, momentum=0.9)
    transforms = Compose(
        [
            ToTensor(),
            Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
        ]
    )

    flare.init()
    sys_info = flare.system_info()
    client_name = sys_info["site_name"]

    # Training dataset and loader
    train_dataset = CIFAR10(
        root=os.path.join(DATASET_PATH, client_name), transform=transforms, download=True, train=True
    )
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

    # Test dataset and loader (for evaluation)
    test_dataset = CIFAR10(root=os.path.join(DATASET_PATH, client_name), train=False, download=True, transform=transforms)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False) # No need to shuffle test data


    summary_writer = SummaryWriter()
    
    # Helper function to evaluate the model
    def evaluate(net_to_eval, loader_to_use, device_to_use):
        net_to_eval.eval() # Set model to evaluation mode
        correct = 0
        total = 0
        with torch.no_grad(): # Disable gradient calculations for inference
            for data in loader_to_use:
                inputs, labels = data[0].to(device_to_use), data[1].to(device_to_use)
                outputs = net_to_eval(inputs)
                _, predicted = torch.max(outputs, 1) # Get the class with the highest probability
                total += labels.size(0)
                correct += (predicted == labels).sum().item() # Count correct predictions, use .item() for scalar
        return 100 * correct / total # Return accuracy as a float


    while flare.is_running():
        input_model = flare.receive()
        print(f"current_round={input_model.current_round}")

        model.load_state_dict(input_model.params)
        model.to(device)
        model.train() # Ensure model is in training mode at the start of the round

        # Calculate total local steps per round for accurate global_step tracking
        steps_per_local_epoch = len(train_loader) # Number of batches per epoch (e.g., 1563 for CIFAR10 with batch_size 32)
        total_local_steps_in_round = epochs * steps_per_local_epoch

        for epoch in range(epochs):
            running_loss = 0.0 # Reset running_loss for each epoch's accumulation
            log_interval_batches = 100 # Log loss every 100 batches (adjust as desired)

            for i, batch in enumerate(train_loader):
                images, labels = batch[0].to(device), batch[1].to(device)
                optimizer.zero_grad()

                predictions = model(images)
                cost = loss(predictions, labels)
                cost.backward()
                optimizer.step()

                running_loss += cost.item() # Accumulate the scalar loss value from the current batch

                # Log average loss for the interval
                if (i + 1) % log_interval_batches == 0: # Log after 100 batches, 200 batches, etc.
                    avg_interval_loss = running_loss / log_interval_batches
                    print(f"Epoch: {epoch}/{epochs}, Iteration: {i+1}, Loss: {avg_interval_loss:.4f}")
                    
                    # Global step for loss: Federated_Round * Total_Local_Steps_in_Round + Local_Epoch * Steps_per_Local_Epoch + Current_Batch_Iteration
                    global_step_loss = input_model.current_round * total_local_steps_in_round + epoch * steps_per_local_epoch + (i + 1)
                    summary_writer.add_scalar(tag="loss_for_each_batch", scalar=avg_interval_loss, global_step=global_step_loss)
                    running_loss = 0.0 # Reset for the next interval
            
            # --- Handle any remaining loss at the end of the epoch ---
            # This ensures that if len(train_loader) is not a perfect multiple of log_interval_batches,
            # the remaining accumulated loss for the partial interval is still logged.
            if running_loss > 0: # If there's any accumulated loss not yet logged
                num_batches_in_last_interval = len(train_loader) % log_interval_batches
                if num_batches_in_last_interval == 0: # This means len(train_loader) was a perfect multiple, the last interval was full
                    num_batches_in_last_interval = log_interval_batches # Use the full interval size for averaging

                avg_remaining_loss = running_loss / num_batches_in_last_interval
                print(f"Epoch: {epoch}/{epochs}, Iteration: {len(train_loader)}, Loss (end of epoch): {avg_remaining_loss:.4f}")
                # Global step for this final logging point for the epoch
                global_step_loss_end_epoch = input_model.current_round * total_local_steps_in_round + (epoch + 1) * steps_per_local_epoch
                summary_writer.add_scalar(tag="loss_for_each_batch", scalar=avg_remaining_loss, global_step=global_step_loss_end_epoch)
                running_loss = 0.0 # Reset

            # --- Evaluate Accuracy AFTER EACH EPOCH ---
            acc = evaluate(model, test_loader, device)
            # Global step for accuracy: Federated_Round * Num_Local_Epochs + Current_Local_Epoch_Number (1-indexed)
            # This ensures accuracy plots are continuous across federated rounds
            global_step_accuracy = input_model.current_round * epochs + (epoch + 1)
            summary_writer.add_scalar(tag="accuracy_per_epoch", scalar=acc, global_step=global_step_accuracy)
            print(f"Epoch {epoch+1}/{epochs} Accuracy: {acc:.2f}%")

            model.train() # Set model back to training mode for the next epoch

        print(f"Finished Local Training for round {input_model.current_round}")

        PATH = "./cifar_net.pth"
        torch.save(model.state_dict(), PATH)

        output_model = flare.FLModel(
            params=model.cpu().state_dict(),
            meta={"NUM_STEPS_CURRENT_ROUND": total_local_steps_in_round},
        )

        flare.send(output_model)


if __name__ == "__main__":
    main()

# import os

# import torch
# from simple_network import SimpleNetwork
# from torch import nn
# from torch.optim import SGD
# from torch.utils.data.dataloader import DataLoader
# from torchvision.datasets import CIFAR10
# from torchvision.transforms import Compose, Normalize, ToTensor

# import nvflare.client as flare
# from nvflare.client.tracking import SummaryWriter

# DATASET_PATH = "/tmp/nvflare/data"


# def main():
#     batch_size = 32 # Your updated batch size
#     epochs = 5
#     lr = 0.01
#     model = SimpleNetwork()
#     device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
#     loss = nn.CrossEntropyLoss()
#     optimizer = SGD(model.parameters(), lr=lr, momentum=0.9)
#     transforms = Compose(
#         [
#             ToTensor(),
#             Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
#         ]
#     )

#     flare.init()
#     sys_info = flare.system_info()
#     client_name = sys_info["site_name"]

#     train_dataset = CIFAR10(
#         root=os.path.join(DATASET_PATH, client_name), transform=transforms, download=True, train=True
#     )
#     train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

#     test_dataset = CIFAR10(root=os.path.join(DATASET_PATH, client_name), train=False, download=True, transform=transforms)
#     test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)


#     summary_writer = SummaryWriter()
    
#     # The evaluate function is good, just ensure it returns a float for accuracy
#     def evaluate(net_to_eval, loader_to_use, device_to_use):
#         net_to_eval.eval() # Set model to evaluation mode
#         correct = 0
#         total = 0
#         with torch.no_grad():
#             for data in loader_to_use:
#                 inputs, labels = data[0].to(device_to_use), data[1].to(device_to_use)
#                 outputs = net_to_eval(inputs)
#                 _, predicted = torch.max(outputs, 1)
#                 total += labels.size(0)
#                 correct += (predicted == labels).sum().item() # Use .item() for scalar value
#         return 100 * correct / total # Use float division


#     while flare.is_running():
#         input_model = flare.receive()
#         print(f"current_round={input_model.current_round}")

#         model.load_state_dict(input_model.params)
#         model.to(device)
#         model.train() # Ensure model is in training mode at start of round/epochs

#         # Calculate total local steps per round for accurate global_step tracking
#         total_local_steps_in_round = epochs * len(train_loader)

#         for epoch in range(epochs):
#             running_loss = 0.0
#             for i, batch in enumerate(train_loader):
#                 images, labels = batch[0].to(device), batch[1].to(device)
#                 optimizer.zero_grad()

#                 predictions = model(images)
#                 cost = loss(predictions, labels)
#                 cost.backward()
#                 optimizer.step()

#                 running_loss += cost.cpu().detach().numpy() / images.size()[0]
#                 if i % 3000 == 0:
#                     print(f"Epoch: {epoch}/{epochs}, Iteration: {i}, Loss: {running_loss / 3000:.4f}")
#                     # Global step for loss: Federated_Round * Total_Local_Steps_in_Round + Local_Epoch * Steps_per_Local_Epoch + Local_Batch_Iteration
#                     global_step_loss = input_model.current_round * total_local_steps_in_round + epoch * len(train_loader) + i
#                     summary_writer.add_scalar(tag="loss_for_each_batch", scalar=running_loss, global_step=global_step_loss)
#                     running_loss = 0.0

#             # --- Calculate and log accuracy AFTER EACH EPOCH ---
#             acc = evaluate(model, test_loader, device)
#             # Global step for accuracy: Federated_Round * Num_Local_Epochs + Current_Local_Epoch_Number (1-indexed)
#             global_step_accuracy = input_model.current_round * epochs + (epoch + 1)
#             summary_writer.add_scalar(tag="accuracy_per_epoch", scalar=acc, global_step=global_step_accuracy)
#             print(f"Epoch {epoch+1}/{epochs} Accuracy: {acc:.2f}%")

#             model.train() # Set model back to training mode for the next epoch

#         print(f"Finished Local Training for round {input_model.current_round}")

#         PATH = "./cifar_net.pth"
#         torch.save(model.state_dict(), PATH)

#         # Removed the problematic accuracy logging line here, as it's now done per epoch
#         # summary_writer.add_scalar("accuracy", acc, epoch)

#         output_model = flare.FLModel(
#             params=model.cpu().state_dict(),
#             meta={"NUM_STEPS_CURRENT_ROUND": total_local_steps_in_round},
#         )

#         flare.send(output_model)


# if __name__ == "__main__":
#     main()



# import os

# import torch
# from simple_network import SimpleNetwork
# from torch import nn
# from torch.optim import SGD
# from torch.utils.data.dataloader import DataLoader
# from torchvision.datasets import CIFAR10
# from torchvision.transforms import Compose, Normalize, ToTensor

# import nvflare.client as flare
# from nvflare.client.tracking import SummaryWriter

# DATASET_PATH = "/tmp/nvflare/data"


# def main():
#     batch_size = 32
#     epochs = 5
#     lr = 0.01
#     model = SimpleNetwork()
#     device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
#     loss = nn.CrossEntropyLoss()
#     optimizer = SGD(model.parameters(), lr=lr, momentum=0.9)
#     transforms = Compose(
#         [
#             ToTensor(),
#             Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
#         ]
#     )

#     flare.init()
#     sys_info = flare.system_info()
#     client_name = sys_info["site_name"]

#     train_dataset = CIFAR10(
#         root=os.path.join(DATASET_PATH, client_name), transform=transforms, download=True, train=True
#     )
#     train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

#     test_dataset = CIFAR10(root=os.path.join(DATASET_PATH, client_name), train=False, download=True, transform=transforms)
#     test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)


#     summary_writer = SummaryWriter()
    
#     def evaluate(input_weights):
#         net = SimpleNetwork()
#         net.load_state_dict(input_weights)
#         net.to(device)

#         correct = 0
#         total = 0
#         with torch.no_grad():
#             for data in test_loader:
#                 # (optional) use GPU to speed things up
#                 inputs, labels = data[0].to(device), data[1].to(device)
#                 # calculate outputs by running images through the network
#                 outputs = net(inputs)
#                 # the class with the highest energy is what we choose as prediction
#                 _, predicted = torch.max(outputs, 1)
#                 total += labels.size(0)
#                 correct += (predicted == labels).sum().item()
#         return 100 * correct // total
    


#     while flare.is_running():
#         input_model = flare.receive()
#         print(f"current_round={input_model.current_round}")

#         model.load_state_dict(input_model.params)
#         model.to(device)

#         steps = epochs * len(train_loader)
#         for epoch in range(epochs):
#             running_loss = 0.0
#             for i, batch in enumerate(train_loader):
#                 images, labels = batch[0].to(device), batch[1].to(device)
#                 optimizer.zero_grad()

#                 predictions = model(images)
#                 cost = loss(predictions, labels)
#                 cost.backward()
#                 optimizer.step()

#                 running_loss += cost.cpu().detach().numpy() / images.size()[0]
#                 if i % 3000 == 0:
#                     print(f"Epoch: {epoch}/{epochs}, Iteration: {i}, Loss: {running_loss / 3000}")
#                     global_step = input_model.current_round * steps + epoch * len(train_loader) + i
#                     summary_writer.add_scalar(tag="loss_for_each_batch", scalar=running_loss, global_step=global_step)
#                     running_loss = 0.0

#         print("Finished Training")

#         PATH = "./cifar_net.pth"
#         torch.save(model.state_dict(), PATH)
#         acc = evaluate(model.state_dict())
#         summary_writer.add_scalar("accuracy", acc, epoch)
#         print(f"Epoch {epoch} accuracy: {acc}")

#         output_model = flare.FLModel(
#             params=model.cpu().state_dict(),
#             meta={"NUM_STEPS_CURRENT_ROUND": steps},
#         )

#         flare.send(output_model)


# if __name__ == "__main__":
#     main()







# import os
# import torch
# from simple_network import SimpleNetwork
# from torch import nn
# from torch.optim import SGD
# from torch.utils.data import DataLoader
# from torchvision.datasets import CIFAR10
# from torchvision.transforms import Compose, Normalize, ToTensor

# import nvflare.client as flare
# from torch.utils.tensorboard import SummaryWriter 

# DATASET_PATH = "/tmp/nvflare/data"

# def main():
#     batch_size, epochs, lr = 32, 5, 0.01
#     model = SimpleNetwork()
#     device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
#     criterion = nn.CrossEntropyLoss()
#     optimizer = SGD(model.parameters(), lr=lr, momentum=0.9)
#     transforms = Compose([ToTensor(), Normalize((0.5,) * 3, (0.5,) * 3)])

#     flare.init()
#     client_name = flare.system_info()["site_name"]

#     # Use unique TensorBoard log directory per client
#     summary_writer = SummaryWriter(log_dir=f"runs/{client_name}")

#     # Data loaders
#     train_loader = DataLoader(
#         CIFAR10(
#             root=os.path.join(DATASET_PATH, client_name),
#             train=True,
#             download=True,
#             transform=transforms
#         ),
#         batch_size=batch_size,
#         shuffle=True
#     )

#     val_loader = DataLoader(
#         CIFAR10(
#             root=os.path.join(DATASET_PATH, client_name),
#             train=False,
#             download=True,
#             transform=transforms
#         ),
#         batch_size=batch_size,
#         shuffle=False
#     )

#     while flare.is_running():
#         input_model = flare.receive()
#         current_round = input_model.current_round
#         model.load_state_dict(input_model.params)
#         model.to(device)

#         steps = epochs * len(train_loader)

#         # Training loop
#         model.train()
#         for epoch in range(epochs):
#             running_loss = 0.0
#             for i, (images, labels) in enumerate(train_loader):
#                 images, labels = images.to(device), labels.to(device)
#                 optimizer.zero_grad()
#                 preds = model(images)
#                 loss = criterion(preds, labels)
#                 loss.backward()
#                 optimizer.step()
#                 running_loss += loss.item()

#                 # Log loss every 300 batches
#                 if i % 300 == 0:
#                     avg_loss = running_loss / (i + 1)
#                     global_step = current_round * steps + epoch * len(train_loader) + i
#                     summary_writer.add_scalar("loss_for_each_batch", avg_loss, global_step)
#                     running_loss = 0.0

#         # Validation loop (accuracy)
#         model.eval()
#         correct = total = 0
#         with torch.no_grad():
#             for images, labels in val_loader:
#                 images, labels = images.to(device), labels.to(device)
#                 outputs = model(images)
#                 _, preds = torch.max(outputs, 1)
#                 total += labels.size(0)
#                 correct += (preds == labels).sum().item()

#         accuracy = correct / total
#         summary_writer.add_scalar("accuracy", accuracy, current_round)

#         #Ensure logs are written to disk
#         summary_writer.flush()

#         #Send updated model back to server
#         flare.send(flare.FLModel(
#             params=model.cpu().state_dict(),
#             meta={"NUM_STEPS_CURRENT_ROUND": steps},
#         ))

#     summary_writer.close()


# if __name__ == "__main__":
#     main()
