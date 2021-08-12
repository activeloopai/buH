echo "uninstalling hub..."
pip uninstall hub -y >> /dev/null 2>&1

rm -rf ./datasets/

BASEDIR=$(dirname $0)

for i in \
    2.0.2 \
    2.0.3 \
    2.0.4 \
    2.0.5 \
    2.0.6 
do
    echo "\ninstalling hub version $i..."
    pip install hub==$i >> /dev/null 2>&1
    echo "creating dataset for hub version $i"
    python $BASEDIR/../create_current_version.py
done

echo "\nfinished creating datasets for all versions!\n"

# in case the user used `pip install -e .` before they ran this
echo "uninstalling hub..."
pip uninstall hub -y >> /dev/null 2>&1