echo "uninstalling hub..."
python3 -m pip uninstall hub -y || python -m pip uninstall hub -y

rm -rf ./datasets/

export BUGGER_OFF="true"
BASEDIR=$(dirname $0)
SCRIPT=$BASEDIR/../create_current_version.py

for i in \
    2.0.4 \
    2.0.7 \
    2.0.8 \
    2.0.11 \
    2.0.12 \
    2.0.14
do
    echo "\ninstalling hub version $i..."
    
    # use this install method instead of `pip install hub==$i` because hub== impacts reporting statistics for pypi
    python3 -m pip install git+https://github.com/activeloopai/Hub.git@release/$i || python -m pip install git+https://github.com/activeloopai/Hub.git@release/$i
    
    echo "creating dataset for hub version $i"
    python3 $SCRIPT || python $SCRIPT
done

echo "\nfinished creating datasets for all versions!\n"

# in case the user used `pip3 install -e .` before they ran this
echo "uninstalling hub..."
python3 -m pip uninstall hub -y || python -m pip uninstall hub -y
