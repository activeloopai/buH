echo "uninstalling hub..."
pip3 uninstall hub -y >> /dev/null 2>&1

rm -rf ./datasets/

export BUGGER_OFF="true"
BASEDIR=$(dirname $0)
SCRIPT=$BASEDIR/../create_current_version.py

for i in \
    2.0.2 \
    2.0.3 \
    2.0.4 \
    2.0.5 \
    2.0.6 \
    2.0.7
do
    echo "\ninstalling hub version $i..."
    pip3 install hub==$i >> /dev/null 2>&1
    echo "creating dataset for hub version $i"
    python3 $SCRIPT || python $SCRIPT
done

echo "\nfinished creating datasets for all versions!\n"

# in case the user used `pip3 install -e .` before they ran this
echo "uninstalling hub..."
pip3 uninstall hub -y >> /dev/null 2>&1