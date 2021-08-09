import hub
from buh.util import *
from buh.constants import *


dataset_path = get_dataset_path(UNDERSCORED_VERSION)


def _assert_lengths(ds):
    assert len(ds[IMAGES]) == 50000
    assert len(ds[LABELS]) == 50000


def _populate_dummy_data(ds):
    with ds:
        ds.images.extend(get_images())
        ds.labels.extend(get_labels())
    _assert_lengths(ds)


def _create0(compression):
    ds = hub.Dataset(dataset_path)
    ds.delete()
    ds = hub.Dataset(dataset_path)

    ds.create_tensor(IMAGES, htype="image", sample_compression=compression)
    ds.create_tensor(
        LABELS, htype="class_label", class_names=["class1", "class2"], dtype=np.uint8
    )

    _populate_dummy_data(ds)


def _create1():
    ds = hub.empty(dataset_path, overwrite=True)
    ds.create_tensor(IMAGES, htype="image", sample_compression=COMPRESSION)
    ds.create_tensor(LABELS, htype="class_label", class_names=["class1", "class2"])
    _populate_dummy_data(ds)


def _create_v2_0_2():
    assert UNDERSCORED_VERSION == "2_0_2"
    _create0(COMPRESSION)


def _create_v2_0_3():
    assert UNDERSCORED_VERSION == "2_0_3"
    _create1()


def _create_v2_0_4():
    assert UNDERSCORED_VERSION == "2_0_4"
    _create1()


def _create_current_version():
    eval(f"_create_v{UNDERSCORED_VERSION}()")


if __name__ == "__main__":
    print(f"generating dataset for hub version {hub.__version__}")
    _create_current_version()
    print("success")
