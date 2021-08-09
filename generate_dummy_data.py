import numpy as np


def get_images():
    # ~39MB
    return np.random.randint(255, size=(50000, 28, 28), dtype=np.uint8)


def get_labels():
    return np.random.randint(255, size=50000, dtype=np.uint8)