import numpy as np
from .common import *
from buh.constants import *




@versions
def test(version, request):
    try_skipping(request)
    skip_if_not_available(version)
    ds = load_dataset_copy(version)

    starting_len = len(ds)
    ds[IMAGES].extend(get_images()[:10])
    ds[LABELS].extend(get_labels()[:10])
    ending_len = len(ds)

    assert starting_len == ending_len + 10

    actual_images = ds[IMAGES].numpy()
    actual_labels = ds[LABELS].numpy()
    expected_images = np.concatenate((get_images(), get_images()[:10]))
    expected_labels = np.concatenate((get_labels(), get_labels()[:10]))

    np.testing.assert_array_equal(actual_images, expected_images)
    np.testing.assert_array_equal(actual_labels, expected_labels)
