#!/bin/bash

if ( hash python3 ); then
  PYTHON=python3
elif ( hash python); then
  PYTHON=python
else
  echo "Neither python or python3 is found in PATH"
  exit 1
fi

readarray -t versions <<< "$($PYTHON -c '
from buh.constants import ALL_VERSIONS
for i in ALL_VERSIONS:
    print(i)
')"

for i in "${versions[@]}"; do
    # shellcheck source=/dev/null
    source "venv_$i"
    python3 -m pytest --junitxml="buh.$i.results.xml" --capture=sys -o junit_logging=all buH/
    deactivate
done