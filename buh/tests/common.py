import os
import shutil
import pytest
from buh.util import *
from buh.constants import *
import hub


def _(version):
    """Replace all `.`s with `_`s."""
    return version.replace(".", "_")


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


def skip_if_not_available(required_version):
    """Calls pytest.skip if the current hub version is < required_version"""

    if hub.__version__ < required_version:
        pytest.skip()


def try_skipping(request):
    """Will only skip if the argument `--buh` exists and is not provided. Useful for running pytest from the hub package with `--buh`."""

    try:
        if not request.config.getoption("--buh"):
            pytest.skip()
    except:
        ValueError


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
