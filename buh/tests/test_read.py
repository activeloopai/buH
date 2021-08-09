import numpy as np
from buh.util import *
from buh.constants import *

def _load0():
    dataset_path = get_dataset_path("2_0_1")
    return hub.Dataset(dataset_path)

def _load_v2_0_1():
    assert UNDERSCORED_VERSION == "2_0_1"
    return _load0()


def _load_v2_0_2():
    assert UNDERSCORED_VERSION == "2_0_2"
    return _load_v2_0_1()


def _load_v2_0_3():
    raise NotImplementedError


def _load_v2_0_4():
    raise NotImplementedError
 
 
def _load_dataset():
    return eval(f"_load_v{UNDERSCORED_VERSION}()")


def _assert_valid(ds):
    images = ds[IMAGES].numpy()
    labels = ds[LABELS].numpy()

    np.testing.assert_array_equal(images, get_images())
    np.testing.assert_array_equal(labels, get_labels())
 
 
# don't parametrize these tests (in case there are API changes)

def test_v2_0_1():
    ds = _load_dataset()
    _assert_valid(ds)


def test_v2_0_2():
    ds = _load_dataset()
    _assert_valid(ds)


def test_v2_0_3():
    ds = _load_dataset()
    _assert_valid(ds)


def test_v2_0_4():
    ds = _load_dataset()
    _assert_valid(ds)