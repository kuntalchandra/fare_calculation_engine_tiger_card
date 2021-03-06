from setuptools import setup, find_packages

NAME = "tiger_card"
VERSION = "1.0.0"
AUTHOR = "Kuntal Chandra"
EMAIL = "chandra.kuntal@gmail.com"
DESCRIPTION = "Design a Fare Calculation Engine for the Tiger Card"
URL = ""
REQUIRES_PYTHON = "3.6"

INSTALL_REQUIRES = [str(ir) for ir in open("requirements.txt")]
TESTS_REQUIRE = ["nose"]

setup(
    name=NAME,
    version=VERSION,
    packages=find_packages(),
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    tests_require=TESTS_REQUIRE,
    entry_points={"console_scripts": ["tiger_card=tiger_card.cli:tiger_card"]},
)
