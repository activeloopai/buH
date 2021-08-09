import pytest
import numpy as np
from buh.util import *
from buh.constants import *

def _load0(dataset_path):
    return hub.Dataset(dataset_path)

def _load1(dataset_path):
    return hub.load(dataset_path)


def _load_v2_0_2(dataset_path):
    assert UNDERSCORED_VERSION == "2_0_2"
    return _load0(dataset_path)


def _load_v2_0_3(dataset_path):
    assert UNDERSCORED_VERSION == "2_0_3"
    return _load1(dataset_path)


def _load_v2_0_4(dataset_path):
    assert UNDERSCORED_VERSION == "2_0_4"
    return _load1(dataset_path)
 
 
def _load_dataset(version):
    # TODO: docstring
    dataset_path = get_dataset_path(version.replace(".", "_")) # TODO format util func
    return eval(f"_load_v{UNDERSCORED_VERSION}(\"{dataset_path}\")")


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