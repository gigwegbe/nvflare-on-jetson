# /home/george/nvflare-env/lib/python3.10/site-packages/torch/utils/tensorboard/__init__.py
import tensorboard
from setuptools._distutils.version import LooseVersion

if not hasattr(tensorboard, '__version__') or LooseVersion(tensorboard.__version__) < LooseVersion('1.15'):
    raise ImportError('TensorBoard logging requires TensorBoard version 1.15 or above')

del LooseVersion
del tensorboard

from .writer import FileWriter, SummaryWriter  # noqa: F401
from tensorboard.summary.writer.record_writer import RecordWriter  # noqa: F401