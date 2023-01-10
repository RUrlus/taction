import importlib
import importlib.metadata

__version__ = importlib.metadata.version("taction")
from taction.lib import _taction_ext as ext

__all__ = ["ext", "__version__"]
