import pathlib
from setuptools import setup, find_packages

PACKAGE_DIR = pathlib.Path(__file__).parent

PACKAGE_NAME = 'pynada'
VERSION = '0.0.1' 
AUTHOR = 'Kamwoo Lee'
URL = 'https://github.com/kl9ch/PyNADA'

LICENSE = 'GPLv3+'
DESCRIPTION = 'Python client for NADA API'
LONG_DESCRIPTION = (PACKAGE_DIR / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = []


# Setting up
setup(
        name = PACKAGE_NAME, 
        version = VERSION,
        author = AUTHOR,
        url = URL,
        description = DESCRIPTION,
        long_description = LONG_DESCRIPTION,
        long_description_content_type = LONG_DESC_TYPE,
        install_requires = INSTALL_REQUIRES,
        packages = find_packages()
)