try:
    import hub
except ImportError:
    import deeplake as hub

UNDERSCORED_VERSION = hub.__version__.replace(".", "_")

DATASETS_FOLDER = "datasets"

# 2.0.1, 2.0.4, 2.0.6, 2.0.10, 2.0.12 is not backwards-supported
ALL_VERSIONS = [
    "2.0.14",
    "2.1.2",
    "2.2.0",
    "2.2.1",
    "2.2.2",
    "2.2.3",
    "2.3.0",
    "2.3.1",
    "2.3.2",
    "2.3.3",
    "2.3.4",
    "2.3.5",
    "2.4.0",
    "2.4.1",
    "2.4.2",
    "2.5.1",
    "2.5.2",
    "2.6.0",
    "2.7.0",
    "2.7.1",
    "2.7.2",
    "2.7.3",
    "2.7.4",
    "2.7.5",
    "2.8.1",
    "2.8.4",
    "2.8.5",
    "3.0.6",
    "3.0.7",
    "3.0.8",
    "3.0.9",
    "3.0.10",
    "3.0.12",
    "3.0.13",
    "3.0.14",
    "3.0.15",
    "3.0.16",
    "3.0.17",
    "3.1.0",
    "3.1.1",
    "3.1.2",
    "3.1.3",
    "3.1.4",
    "3.1.5",
    "3.1.6",
    "3.1.7",
    "3.1.8",
    "3.1.9",
    "3.1.10",
    "3.1.11",
    "3.1.12",
    "3.2.1",
    "3.2.2",
    "3.2.3",
    "3.2.4",
    "3.2.5",
    "3.2.6",
    "3.2.7",
    "3.2.8",
    "3.2.9",
    "3.2.10",
    "3.2.11",
    "3.2.12",
    "3.2.13",
    "3.2.15",
    "3.2.16",
    "3.2.17",
    "3.2.18",
    "3.2.19",
    "3.2.21",
    "3.2.22",
    "3.3.0",
    "3.3.1",
    "3.3.2",
    "3.4.0",
    "3.4.1",
    "3.4.2",
    "3.4.3",
    "3.4.4",
    "3.5.0",
    "3.5.1",
    "3.5.2",
    "3.5.3",
    "3.5.4",
    "3.6.0",
    "3.6.1"
]  # TODO use inside the .sh script

# the staging deeplake version is the version that will be the next release
# this should be updated when the staging deeplake is released.
# IMPORTANT: after updating this version, update `ALL_VERSIONS` and `create_all.sh`!
# TODO: automate this
STAGING_HUB_VERSION = "3.6.2"

COMPRESSION = None
IMAGES = "images"
LABELS = "labels"
LABELS_WITH_NONE = "labels_with_none"
