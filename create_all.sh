echo "uninstalling hub..."
pip uninstall hub -y >> /dev/null 2>&1

for i in \
    2.0.1 \
    2.0.2 \
    2.0.3 \
    2.0.4
do
    echo "\ninstalling $i..."
    pip install hub==$i >> /dev/null 2>&1
    python create.py
done

echo "\nfinished creating datasets for all versions!\n"

echo "uninstalling hub..."
pip uninstall hub -y >> /dev/null 2>&1