import hub
from .dummy_data import *

v = hub.__version__.replace(".", "_")
dataset_path = f"./datasets/{v}"

COMPRESSION = None
IMAGES = "images"
LABELS = "labels"


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


def v2_0_1():
    assert v == "2_0_1"
    compression = "uncompressed" if COMPRESSION is None else COMPRESSION
    _create0(compression)


def v2_0_2():
    assert v == "2_0_2"
    _create0(COMPRESSION)


def v2_0_3():
    assert v == "2_0_3"
    _create1()


def v2_0_4():
    assert v == "2_0_4"
    _create1()


if __name__ == "__main__":
    print(f"generating dataset for hub version {hub.__version__}")
    eval(f"v{v}()")
    print("success")
