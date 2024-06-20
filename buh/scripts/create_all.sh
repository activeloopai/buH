#!/usr/bin/env bash

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


y_print() {
  echo -e "\033[33m $* \033[00m"
}

y_print "uninstalling hub..."
$PYTHON -m pip uninstall hub -y
y_print "uninstalling deeplake..."
$PYTHON -m pip uninstall deeplake -y

rm -rf ./datasets/

## Restore dataset cache since they take a while to rebuild
if [ -d "datasets_clean" ]; then
  y_print "Restoring datasets_clean cache"
  cp -r datasets_clean datasets
fi

export BUGGER_OFF="true"
BASEDIR=$(dirname $0)
SCRIPT=$BASEDIR/../create_current_version.py

for i in "${versions[@]}"; do
    $PYTHON -m venv "venv_$i"
    # shellcheck source=/dev/null
    source "venv_$i/bin/activate"
    dataset_dir="datasets/${i//[\\.]/_}"
    y_print "Version: $i"
    if [ -d "${dataset_dir}" ]
    then
      y_print "Dataset ${dataset_dir} already exists"
      continue
    fi

    y_print "Installing hub version $i..."

    # use this install method instead of `pip install deeplake==$i` because deeplake== impacts reporting statistics for pypi

    python -m pip install git+https://github.com/activeloopai/deeplake.git@v$i

    y_print "creating dataset for hub version $i"
    python "${SCRIPT}"
    deactivate
done

y_print "Finished creating datasets for all versions"
y_print "Saving datasets_clean cache to $(pwd)/datasets_clean"
cp -rn datasets datasets_clean
