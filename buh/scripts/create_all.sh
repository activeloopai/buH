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
from buH.buh.versions import VERSIONS
for i in VERSIONS:
    print(i)
')"


y_print() {
  echo -e "\033[33m $* \033[00m"
}

rm -rf ./datasets/ || true

# ## Restore dataset cache since they take a while to rebuild
# if [ -d "datasets_clean" ]; then
#   y_print "Restoring datasets_clean cache"
#   cp -r datasets_clean datasets
# fi

export BUGGER_OFF="true"
BASEDIR=$(dirname $0)
SCRIPT=$BASEDIR/../create_current_version.py

for i in "${versions[@]}"; do
    y_print "creating virtual environment: $i"
    $PYTHON -m venv "venv_$i"
    # shellcheck source=/dev/null
    source "venv_$i/bin/activate"
    y_print "installing deeplake and dependencies"
    pip install -U pip setuptools
    pip install -r deeplake/requirements/common.txt
    pip install -r deeplake/requirements/tests.txt
    pip install -e .[all]
    dataset_dir="datasets/${i//[\\.]/_}"
    if [ -d "${dataset_dir}" ]
    then
      y_print "Dataset ${dataset_dir} already exists"
      continue
    fi
    y_print "installing deeplake version: $i"
    python -m pip install git+https://github.com/activeloopai/deeplake.git@v$i
    y_print "creating dataset for hub version $i"
    python "${SCRIPT}"
    cp -rn datasets datasets_clean
    y_print "installing buh"
    pip install -e buH
    pytest --junitxml="buh.$i.results.xml" --capture=sys -o junit_logging=all buH/
    deactivate
    rm -r "venv_$i"
done

y_print "Finished creating datasets for all versions"
y_print "Saving datasets_clean cache to $(pwd)/datasets_clean"

