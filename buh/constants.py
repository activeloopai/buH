try:
    import hub
except ImportError:
    import deeplake as hub

from buh.versions import VERSIONS

ALL_VERSIONS = VERSIONS.copy()

UNDERSCORED_VERSION = hub.__version__.replace(".", "_")

DATASETS_FOLDER = "datasets"

# the staging deeplake version is the version that will be the next release
# this should be updated when the staging deeplake is released.
# IMPORTANT: after updating this version, update `ALL_VERSIONS` and `create_all.sh`!
# TODO: automate this
STAGING_HUB_VERSION = "3.9.11"

COMPRESSION = None
IMAGES = "images"
LABELS = "labels"
LABELS_WITH_NONE = "labels_with_none"
