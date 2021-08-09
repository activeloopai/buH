import pytest
import numpy as np
from buh.util import *
from buh.constants import *

def _load0(path):
    return hub.Dataset(path)

def _load1(path):
    return hub.load(path)

LOAD_FUNCS = {
    "2.0.2": _load0,
    "default": _load1,
}
 
def _load_dataset(version):
    # TODO: docstring
    dataset_path = get_dataset_path(version.replace(".", "_")) # TODO format util func
    loader = LOAD_FUNCS.get(hub.__version__, LOAD_FUNCS["default"])
    return loader(dataset_path)


def _assert_valid(ds):
    images = ds[IMAGES].numpy()
    labels = ds[LABELS].numpy()
    np.testing.assert_array_equal(images, get_images())
    np.testing.assert_array_equal(labels, get_labels())


def _skip_if_not_available(required_version):
    """Calls pytest.skip if the current hub version is < required_version"""

    if hub.__version__ < required_version:
        pytest.skip()

@pytest.mark.parametrize("version", ALL_VERSIONS)
def test(version):
    _skip_if_not_available(version)
    ds = _load_dataset(version)
    _assert_valid(ds)