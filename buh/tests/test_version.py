import warnings
import hub
from buh.constants import ALL_VERSIONS, STAGING_HUB_VERSION


def test(): 
    is_staging = hub.__version__ == STAGING_HUB_VERSION
    if not is_staging:
        warnings.warn(f"Testing hub backwards compatibility for {hub.__version__}, even though the staging hub version is {STAGING_HUB_VERSION}!")

    assert hub.__version__ in ALL_VERSIONS or is_staging, "When incrementing version string for hub, you must update backwards compatibility tests. IMPORTANT: Make sure when you update `ALL_VERSIONS` you also update the `create_all.sh` script!"