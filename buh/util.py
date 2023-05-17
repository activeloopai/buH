import numpy as np
from buh.constants import *


def get_images():
    # ~39MB
    np.random.seed(0)
    return np.random.randint(255, size=(50000, 28, 28), dtype=np.uint8)


def get_labels():
    np.random.seed(0)
    return np.random.randint(2, size=50000, dtype=np.uint8)

def get_labels_with_none():
    return [1] * 10000 + [None, [],  np.array([])] * 10000 + [1] * 10000

def get_labels_with_none_shapes():
    return [(1,)] * 10000 + [(0,)] * 30000 + [(1,)] * 10000


def get_dataset_path(underscored_version):
    return f"./{DATASETS_FOLDER}/{underscored_version}"
