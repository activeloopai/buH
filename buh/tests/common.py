import os
import shutil
import pytest
from buh.util import *
from buh.constants import *
try:
    import hub
except ImportError:
    import deeplake as hub


def _(version):
    """Replace all `.`s with `_`s."""
    return version.replace(".", "_")


def version_compare(v1, v2):
    """Returns -1 if v1 is older than v2, 0 if v1 == v2, and +1 if v1 > v2."""

    arr1 = v1.split(".")
    arr2 = v2.split(".")
    n = len(arr1)
    m = len(arr2)

    # converts to integer from string
    arr1 = [int(i) for i in arr1]
    arr2 = [int(i) for i in arr2]

    # compares which list is bigger and fills
    # smaller list with zero (for unequal delimeters)
    if n > m:
        for i in range(m, n):
            arr2.append(0)
    elif m > n:
        for i in range(n, m):
            arr1.append(0)

    # returns 1 if version 1 is bigger and -1 if
    # version 2 is bigger and 0 if equal
    for i in range(len(arr1)):
        if arr1[i] > arr2[i]:
            return 1
        elif arr2[i] > arr1[i]:
            return -1
    return 0


versions = pytest.mark.parametrize("version", ALL_VERSIONS)
DATASET_SUFFIX = f"ffw{UNDERSCORED_VERSION}"


# TODO: move these to a separate file
def _load0(path):
    return hub.Dataset(path)


def _load1(path):
    return hub.load(path)


LOAD_FUNCS = {
    "2.0.2": _load0,
    "default": _load1,
}


def assert_version(required_version):
    """Asserts that the required version is met by the installation of deeplake."""

    assert (
        version_compare(hub.__version__, required_version) >= 0
    ), f"deeplake version {hub.__version__} is too old. Required version is {required_version}"


def _bc_load_dataset(path):
    # TODO: docstring/rename func

    loader = LOAD_FUNCS.get(hub.__version__, LOAD_FUNCS["default"])
    return loader(path)


def load_dataset(version):
    # TODO: docstring

    dataset_path = get_dataset_path(_(version))  # TODO format util func
    return _bc_load_dataset(dataset_path)


def load_dataset_copy(version, suffix=DATASET_SUFFIX, overwrite=False):
    # TODO: docstring/rename func

    dataset_path = get_dataset_path(_(version))  # TODO format util func
    new_dataset_path = f"{dataset_path}_{suffix}"
    if overwrite:
        shutil.rmtree(new_dataset_path, ignore_errors=True)
    new_path = shutil.copytree(dataset_path, new_dataset_path)
    return _bc_load_dataset(new_path)
