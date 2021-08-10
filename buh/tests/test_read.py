import numpy as np
from buh.tests.common import *
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
    dataset_path = get_dataset_path(version.replace(".", "_"))  # TODO format util func
    loader = LOAD_FUNCS.get(hub.__version__, LOAD_FUNCS["default"])
    return loader(dataset_path)


def _assert_valid(ds):
    images = np.squeeze(ds[IMAGES].numpy())
    labels = np.squeeze(ds[LABELS].numpy())
    np.testing.assert_array_equal(images, get_images())
    np.testing.assert_array_equal(labels, get_labels())


@versions
def test(version, request):
    try_skipping(request)
    skip_if_not_available(version)
    ds = _load_dataset(version)
    _assert_valid(ds)
