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

@pytest.mark.parameterize("version", ["3.2.21"])
def test_read_none(version):
    assert_version(version)
    ds = load_dataset(version)
    _assert_valid(ds)

    shapes = get_labels_with_none_shapes()
    for i, sample in enumerate(ds[LABELS_WITH_NONE]):
        assert sample.shape == shapes[i]
