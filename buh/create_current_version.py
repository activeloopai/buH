import pytest
try:
    import hub
except ImportError:
    import deeplake as hub
from buh.util import *
from buh.constants import *
from buh.tests.common import *


dataset_path = get_dataset_path(UNDERSCORED_VERSION)
print("Creating dataset at", dataset_path)
COMPRESSION = None


def _assert_lengths(ds):
    assert len(ds[IMAGES]) == 50000
    assert len(ds[LABELS]) == 50000


def _populate_dummy_data(ds):
    with ds:
        ds.images.extend(get_images())
        ds.labels.extend(get_labels())
    _assert_lengths(ds)


def _create0():
    ds = hub.empty(dataset_path)

    ds.create_tensor(IMAGES, htype="image", sample_compression=COMPRESSION)
    ds.create_tensor(
        LABELS, htype="class_label", class_names=["class1", "class2"], dtype=np.uint8
    )
    _populate_dummy_data(ds)


def _create1():
    ds = hub.empty(dataset_path, overwrite=True)
    ds.create_tensor(IMAGES, htype="image", sample_compression=COMPRESSION)
    ds.create_tensor(LABELS, htype="class_label", class_names=["class1", "class2"])
    ds.create_tensor(LABELS_WITH_NONE, htype="class_label")
    _populate_dummy_data(ds)

    samples = get_labels_with_none()
    for sample in samples:
        ds[LABELS_WITH_NONE].append(sample)

def _create2():
    ds = hub.empty(dataset_path, overwrite=True)
    ds.create_tensor(IMAGES, htype="image", sample_compression=COMPRESSION)
    ds.create_tensor(LABELS, htype="class_label", class_names=["class1", "class2"])
    _populate_dummy_data(ds)


CREATE_FUNCS = {
    "2": _create0,
    "3": _create1,
    "default": _create2,
}


def _create_dataset_for_current_version():
    # TODO: docstring
    major = hub.__version__.split(".")[0]
    if major == "2":
        print("\033[33m", "creator function for 2~", "\033[00m")
        return _create0()
    elif major == "3":
        print("\033[33m", "creator function for 3~", "\033[00m")
        return _create1()
    else:
        print("\033[33m", "creator function for default", "\033[00m")
        return _create2()


if __name__ == "__main__":
    _create_dataset_for_current_version()  # TODO: compressions?
