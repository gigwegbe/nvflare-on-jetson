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

# import os

# import torch
# from simple_network import SimpleNetwork
# from torch import nn
# from torch.optim import SGD
# from torch.utils.data.dataloader import DataLoader
# from torchvision.datasets import CIFAR10
# from torchvision.transforms import Compose, Normalize, ToTensor

import os
import torch
from simple_network import SimpleNetwork
from torch import nn
from torch.optim import SGD
from torch.utils.data import DataLoader
from torchvision.datasets import CIFAR10
from torchvision.transforms import Compose, Normalize, ToTensor

import nvflare.client as flare
from torch.utils.tensorboard import SummaryWriter 

DATASET_PATH = "/tmp/nvflare/data"

def main():
    batch_size, epochs, lr = 32, 5, 0.01
    model = SimpleNetwork()
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    criterion = nn.CrossEntropyLoss()
    optimizer = SGD(model.parameters(), lr=lr, momentum=0.9)
    transforms = Compose([ToTensor(), Normalize((0.5,) * 3, (0.5,) * 3)])

    flare.init()
    client_name = flare.system_info()["site_name"]

    # Use unique TensorBoard log directory per client
    summary_writer = SummaryWriter(log_dir=f"runs/{client_name}")

    # Data loaders
    train_loader = DataLoader(
        CIFAR10(
            root=os.path.join(DATASET_PATH, client_name),
            train=True,
            download=True,
            transform=transforms
        ),
        batch_size=batch_size,
        shuffle=True
    )

    val_loader = DataLoader(
        CIFAR10(
            root=os.path.join(DATASET_PATH, client_name),
            train=False,
            download=True,
            transform=transforms
        ),
        batch_size=batch_size,
        shuffle=False
    )

    while flare.is_running():
        input_model = flare.receive()
        current_round = input_model.current_round
        model.load_state_dict(input_model.params)
        model.to(device)

        steps = epochs * len(train_loader)

        # Training loop
        model.train()
        for epoch in range(epochs):
            running_loss = 0.0
            for i, (images, labels) in enumerate(train_loader):
                images, labels = images.to(device), labels.to(device)
                optimizer.zero_grad()
                preds = model(images)
                loss = criterion(preds, labels)
                loss.backward()
                optimizer.step()
                running_loss += loss.item()

                # Log loss every 300 batches
                if i % 300 == 0:
                    avg_loss = running_loss / (i + 1)
                    global_step = current_round * steps + epoch * len(train_loader) + i
                    summary_writer.add_scalar("loss_for_each_batch", avg_loss, global_step)
                    running_loss = 0.0

        # Validation loop (accuracy)
        model.eval()
        correct = total = 0
        with torch.no_grad():
            for images, labels in val_loader:
                images, labels = images.to(device), labels.to(device)
                outputs = model(images)
                _, preds = torch.max(outputs, 1)
                total += labels.size(0)
                correct += (preds == labels).sum().item()

        accuracy = correct / total
        summary_writer.add_scalar("accuracy", accuracy, current_round)

        #Ensure logs are written to disk
        summary_writer.flush()

        #Send updated model back to server
        flare.send(flare.FLModel(
            params=model.cpu().state_dict(),
            meta={"NUM_STEPS_CURRENT_ROUND": steps},
        ))

    summary_writer.close()


if __name__ == "__main__":
    main()
