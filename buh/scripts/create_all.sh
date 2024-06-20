#!/usr/bin/env bash

if ( hash python3 ); then
  PYTHON=python3
elif ( hash python); then
  PYTHON=python
else
  echo "Neither python or python3 executable found in PATH"
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

y_print "installing deeplake common dependencies so venv can take from local cache"
y_print "installing pip and setuptools globally"
$PYTHON -m pip install -qqq -U pip setuptools
y_print "installing deeplake common dependencies globally"
$PYTHON -m pip install -qqq -r deeplake/requirements/common.txt
y_print "installing deeplake test dependencies globally"
$PYTHON -m pip install -qqq -r deeplake/requirements/tests.txt
y_print "installing deeplake globally"
$PYTHON -m pip install -qqq -e .[all]
y_print "installing pytest globally"
$PYTHON -m pip install -qqq pytest
y_print "installing buH globally"
$PYTHON -m pip install -qqq -e buH

for i in "${versions[@]}"; do
    y_print "creating virtual environment: $i"
    $PYTHON -m venv "venv_$i"
    # shellcheck source=/dev/null
    source "venv_$i/bin/activate"
    y_print "installing pip and setuptools"
    pip install -qqq -U pip setuptools
    y_print "installing deeplake common dependencies"
    pip install -qqq -r deeplake/requirements/common.txt
    y_print "installing deeplake test dependencies"
    pip install -qqq -r deeplake/requirements/tests.txt
    y_print "installing pytest"
    pip install -qqq pytest
    y_print "installing buH"
    pip install -qqq -e buH
    dataset_dir="datasets/${i//[\\.]/_}"
    if [ -d "${dataset_dir}" ]
    then
      y_print "Dataset ${dataset_dir} already exists"
      continue
    fi
    y_print "installing deeplake version: $i"
    python -m pip install -qqq git+https://github.com/activeloopai/deeplake.git@v$i
    y_print "creating dataset for hub version $i"
    python "${SCRIPT}"
    cp -rf datasets/* datasets_clean/
    pytest --junitxml="buh.$i.results.xml" --capture=sys -o junit_logging=all buH/
    deactivate
    rm -r "venv_$i"
done
