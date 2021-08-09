import pytest
import numpy as np
from buh.util import *
from buh.constants import *

def _load0(dataset_path):
    return hub.Dataset(dataset_path)

def _load_v2_0_1(dataset_path):
    assert UNDERSCORED_VERSION == "2_0_1"
    return _load0(dataset_path)


def _load_v2_0_2(dataset_path):
    assert UNDERSCORED_VERSION == "2_0_2"
    return _load_v2_0_1(dataset_path)


def _load_v2_0_3(dataset_path):
    raise NotImplementedError


def _load_v2_0_4(dataset_path):
    raise NotImplementedError
 
 
def _load_dataset(underscored_version):
    # TODO: docstring
    dataset_path = get_dataset_path(underscored_version)
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
 
 
def test_v2_0_1():
    _skip_if_not_available("2.0.1")
    ds = _load_dataset("2_0_1")
    _assert_valid(ds)


def test_v2_0_2():
    _skip_if_not_available("2.0.2")
    ds = _load_dataset("2_0_2")
    _assert_valid(ds)


def test_v2_0_3():
    _skip_if_not_available("2.0.3")
    ds = _load_dataset("2_0_3")
    _assert_valid(ds)


def test_v2_0_4():
    _skip_if_not_available("2.0.4")
    ds = _load_dataset("2_0_4")
    _assert_valid(ds)