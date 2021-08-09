import hub
import pytest
from buh.constants import *

versions = pytest.mark.parametrize("version", ALL_VERSIONS)


def skip_if_not_available(required_version):
    """Calls pytest.skip if the current hub version is <= required_version"""

    if hub.__version__ <= required_version:
        pytest.skip()