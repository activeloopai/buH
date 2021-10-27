import hub

UNDERSCORED_VERSION = hub.__version__.replace(".", "_")

DATASETS_FOLDER = "datasets"

# 2.0.1 is not backwards-supported
ALL_VERSIONS = [
    "2.0.4",
    "2.0.6",
    "2.0.7",
    "2.0.8",
    "2.0.11",
    "2.0.12",
    "2.0.14"
]  # TODO use inside the .sh script

# the staging hub version is the version that will be the next release
# this should be updated when the staging hub is released.
# IMPORTANT: after updating this version, update `ALL_VERSIONS` and `create_all.sh`!
# TODO: automate this
STAGING_HUB_VERSION = "2.0.15"

COMPRESSION = None
IMAGES = "images"
LABELS = "labels"
