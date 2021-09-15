import numpy as np
from buh.tests.common import *
from buh.util import *
from buh.constants import *


def _assert_valid(ds):
    images = np.squeeze(ds[IMAGES].numpy())
    labels = np.squeeze(ds[LABELS].numpy())
    np.testing.assert_array_equal(images, get_images())
    np.testing.assert_array_equal(labels, get_labels())


@versions
def test(version, request):
    assert_version(version)
    ds = load_dataset(version)
    _assert_valid(ds)
