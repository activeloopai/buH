import os
import re

from setuptools import find_packages, setup

project_name = "buh"


this_directory = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(this_directory, f"{project_name}/requirements/common.txt")) as f:
    requirements = f.readlines()

with open(os.path.join(this_directory, f"{project_name}/requirements/tests.txt")) as f:
    tests = f.readlines()

with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


init_file = os.path.join(project_name, "__init__.py")


def get_property(prop):
    result = re.search(
        # find variable with name `prop` in the __init__.py file
        rf'{prop}\s*=\s*[\'"]([^\'"]*)[\'"]',
        open(init_file).read(),
    )
    return result.group(1)


setup(
    name=project_name,
    version=get_property("__version__"),
    description="Activeloop Hub backwards (buH) compatibility",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="activeloop.ai",
    author_email="support@activeloop.ai",
    packages=find_packages(),
    install_requires=requirements,
    tests_require=tests,
    include_package_data=True,
    zip_safe=False,
    # entry_points={"console_scripts": ["activeloop = deeplake.cli.commands:cli"]},  # TODO
    setup_requires=[],
    dependency_links=[],
    project_urls={
        "Documentation": "https://docs.activeloop.ai/",  # TODO: docs page
        "Source": "https://github.com/activeloopai/buH",
    },
)
