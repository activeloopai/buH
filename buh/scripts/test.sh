#!/bin/bash

readarray -t versions <<< "$($PYTHON -c '
from buh.constants import ALL_VERSIONS
for i in ALL_VERSIONS:
    print(i)
')"

for i in "${versions[@]}"; do
    # shellcheck source=/dev/null
    source "venv_$i"
    pytest --junitxml="buh.$i.results.xml" --capture=sys -o junit_logging=all buH/
    deactivate
done
