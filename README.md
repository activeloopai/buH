# Buh
[Hub](https://github.com/activeloopai/Hub) backwards (buH) compatibility tests!

## Running buH Tests
1. Clone this repository.
2. `cd buH`
3. `pip install -e .`
4. `sh buh/scripts/create_all.sh` -- see script [here](./buh/scripts/create_all.sh)
    - Creates a new directory inside the clone location of `buH` called `datasets`.
    - Warning, this will `pip uninstall hub` so it can pip install all versions of hub and use them. After calling this script (you should only have to call it once per machine), you should pip install the version of hub you want to test using.
5. `pytest .`