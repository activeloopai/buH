echo "uninstalling hub..."
python3 -m pip uninstall hub -y || python -m pip uninstall hub -y
echo "uninstalling deeplake..."
python3 -m pip uninstall deeplake -y || python -m pip uninstall deeplake -y
rm -rf ./datasets/

export BUGGER_OFF="true"
BASEDIR=$(dirname $0)
SCRIPT=$BASEDIR/../create_current_version.py

for i in \
    2.0.4 \
    2.0.7 \
    2.0.8 \
    2.0.11 \
    2.0.13 \
    2.1.1 \
    2.2.0 \
    2.2.1.0 \
    2.2.2 \
    2.2.3 \
    2.3.0 \
    2.3.1 \
    2.3.2 \
    2.3.3 \
    2.3.4 \
    2.3.5 \
    2.4.0 \
    2.4.1 \
    2.4.2 \
    2.5.0 \
    2.5.1 \
    2.5.2 \
    2.6.0 \
    2.7.0 \
    2.7.1 \
    2.7.2 \
    2.7.3 \
    2.7.4 \
    2.7.5 \
    2.8.1 \
    2.8.4 \
    2.8.5
do
    echo "\ninstalling hub version $i..."
    
    # use this install method instead of `pip install deeplake==$i` because deeplake== impacts reporting statistics for pypi
    python3 -m pip install git+https://github.com/activeloopai/deeplake.git@v$i || python -m pip install git+https://github.com/activeloopai/deeplake.git@v$i
    
    echo "creating dataset for hub version $i"
    python3 $SCRIPT || python $SCRIPT
done

echo "\nfinished creating datasets for all versions!\n"

# in case the user used `pip3 install -e .` before they ran this
echo "uninstalling hub..."
python3 -m pip uninstall hub -y || python -m pip uninstall hub -y


for i in \
    3.0.6

do
    echo "\ninstalling deeplake version $i..."
    
    # use this install method instead of `pip install deeplake==$i` because deeplake== impacts reporting statistics for pypi
    (python3 -m pip install git+https://github.com/activeloopai/deeplake.git@v$i || python -m pip install git+https://github.com/activeloopai/deeplake.git@v$i) && echo "creating dataset for deeplake version $i" && (python3 $SCRIPT || python $SCRIPT)

done

# echo "\nfinished creating datasets for all versions!\n"

# in case the user used `pip3 install -e .` before they ran this
echo "uninstalling deeplake..."
python3 -m pip uninstall hub -y || python -m pip uninstall hub -y
python3 -m pip uninstall deeplake -y || python -m pip uninstall deeplake -y

