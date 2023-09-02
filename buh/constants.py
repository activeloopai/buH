try:
    import hub
except ImportError:
    import deeplake as hub

UNDERSCORED_VERSION = hub.__version__.replace(".", "_")

DATASETS_FOLDER = "datasets"

# Only include the last patch release for each X.Y version.
# When a new patch version is released, replace the last row.
# When a new minor version is released, add it as  new row
ALL_VERSIONS = [
    "2.2.3",
    "2.3.5",
    "2.4.2",
    "2.5.2",
    "2.6.0",
    "2.7.5",
    "2.8.5",
    "3.0.17",
    "3.1.12",
    "3.2.22",
    "3.3.2",
    "3.4.4",
    "3.5.4",
    # Replace this with the new patch version
    "3.6.22"
]  # TODO use inside the .sh script

# the staging deeplake version is the version that will be the next release
# this should be updated when the staging deeplake is released.
# IMPORTANT: after updating this version, update `ALL_VERSIONS` and `create_all.sh`!
# TODO: automate this
STAGING_HUB_VERSION = "3.6.23"

COMPRESSION = None
IMAGES = "images"
LABELS = "labels"
LABELS_WITH_NONE = "labels_with_none"
