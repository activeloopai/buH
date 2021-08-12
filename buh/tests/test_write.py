import numpy as np
from .common import *
from buh.constants import *


def assert_new_versions(ds):
    v = hub.__version__

    img = ds[IMAGES]
    assert img.meta.version == v
    assert img.chunk_engine.chunk_id_encoder.version == v

    lab = ds[LABELS]
    assert lab.meta.version == v
    assert img.chunk_engine.chunk_id_encoder.version == v


@versions
def test_new_samples(version, request):
    try_skipping(request)
    skip_if_not_available(version)
    ds = load_dataset_copy(version, overwrite=True)

    starting_len = len(ds)
    ds[IMAGES].extend(get_images()[:10])
    for l in get_labels()[:10]:
        ds[LABELS].append(l)
    ending_len = len(ds)

    assert ending_len == starting_len + 10

    actual_images = ds[IMAGES].numpy()
    actual_labels = ds[LABELS].numpy()
    expected_images = np.concatenate((get_images(), get_images()[:10]))
    expected_labels = np.expand_dims(np.concatenate((get_labels(), get_labels()[:10])), axis=-1)

    np.testing.assert_array_equal(actual_images, expected_images)
    np.testing.assert_array_equal(actual_labels, expected_labels)

    assert_new_versions(ds)

@versions
def test_new_tensor(version, request):
    try_skipping(request)
    skip_if_not_available(version)
    ds = load_dataset_copy(version, overwrite=True)

    ds.create_tensor("new_tensor")
    ds.new_tensor.extend(get_images()[:10])

    assert ds.meta.version == hub.__version__


@versions
def test_update_samples(version, request):
    try_skipping(request)
    skip_if_not_available(version)
    ds = load_dataset_copy(version, overwrite=True)

    ds[IMAGES][10:20] = get_images()[:10]
    ds[LABELS][10:30] = get_labels()[:20]

    assert_new_versions(ds)

    actual_images = ds[IMAGES].numpy()
    actual_labels = ds[LABELS].numpy()
    expected_images = np.concatenate((get_images()[:10], get_images()[:10], get_images()[20:]))
    expected_labels = np.expand_dims(np.concatenate((get_labels()[:10], get_labels()[:20], get_labels()[30:])), axis=-1)

    np.testing.assert_array_equal(actual_images, expected_images)
    np.testing.assert_array_equal(actual_labels, expected_labels)