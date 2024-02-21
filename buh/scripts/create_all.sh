#!/usr/bin/env bash

echo "uninstalling hub..."
python3 -m pip uninstall hub -y || python -m pip uninstall hub -y
echo "uninstalling deeplake..."
python3 -m pip uninstall deeplake -y || python -m pip uninstall deeplake -y

rm -rf ./datasets/

## Restore dataset cache since they take a while to rebuild
if [ -d "datasets_clean" ]; then
  echo "Restoring datasets_clean cache"
  cp -r datasets_clean datasets
fi

export BUGGER_OFF="true"
BASEDIR=$(dirname $0)
SCRIPT=$BASEDIR/../create_current_version.py

for i in \
    2.0.13 \
    2.1.1 \
    2.2.3 \
    2.3.5 \
    2.4.2 \
    2.5.2 \
    2.6.0 \
    2.7.5 \
    2.8.5
do
    dataset_dir="datasets/${i//[\\.]/_}"
    echo $underscore_version
    if [ -d $dataset_dir ]
    then
      echo "Dataset ${dataset_dir} already exists"
      continue
    fi

    echo "Installing hub version $i..."
    
    # use this install method instead of `pip install deeplake==$i` because deeplake== impacts reporting statistics for pypi
    python3 -m pip install git+https://github.com/activeloopai/deeplake.git@v$i || python -m pip install git+https://github.com/activeloopai/deeplake.git@v$i
    
    echo "creating dataset for hub version $i"
    python3 $SCRIPT || python $SCRIPT
done

echo "Finished creating datasets for all versions"

# in case the user used `pip3 install -e .` before they ran this
echo "uninstalling hub..."
python3 -m pip uninstall hub -y || python -m pip uninstall hub -y


# Only include the last patch release for each X.Y version.
# When a new patch version is released, replace the last row.
# When a new minor version is released, add it as  new row
for i in \
    3.0.17 \
    3.1.12 \
    3.2.22 \
    3.3.2 \
    3.4.4 \
    3.5.4 \
    3.6.26 \
    3.7.3 \
    3.8.21
# Replace the above line with the new patch version on release

do
    dataset_dir="datasets/${i//[\\.]/_}"
    echo $underscore_version
    if [ -d $dataset_dir ]
    then
      echo "Dataset ${dataset_dir} already exists"
      continue
    fi

    echo "Installing deeplake version $i..."
    
    # use this install method instead of `pip install deeplake==$i` because deeplake== impacts reporting statistics for pypi
    (python3 -m pip install git+https://github.com/activeloopai/deeplake.git@v$i || python -m pip install git+https://github.com/activeloopai/deeplake.git@v$i) && echo "creating dataset for deeplake version $i" && (python3 $SCRIPT || python $SCRIPT)

done

echo "Saving datasets_clean cache to $(pwd)/datasets_clean"
cp -rn datasets datasets_clean

# echo "Finished creating datasets for all versions!"

# in case the user used `pip3 install -e .` before they ran this
echo "uninstalling deeplake..."
python3 -m pip uninstall hub -y || python -m pip uninstall hub -y
python3 -m pip uninstall deeplake -y || python -m pip uninstall deeplake -y

