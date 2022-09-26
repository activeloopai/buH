import deeplake

UNDERSCORED_VERSION = deeplake.__version__.replace(".", "_")

DATASETS_FOLDER = "datasets"

# 2.0.1 is not backwards-supported
ALL_VERSIONS = [
    "2.0.4",
    "2.0.6",
    "2.0.10",
    "2.0.12",
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
]  # TODO use inside the .sh script

# the staging deeplake version is the version that will be the next release
# this should be updated when the staging deeplake is released.
# IMPORTANT: after updating this version, update `ALL_VERSIONS` and `create_all.sh`!
# TODO: automate this
STAGING_HUB_VERSION = "2.8.6"

COMPRESSION = None
IMAGES = "images"
LABELS = "labels"
