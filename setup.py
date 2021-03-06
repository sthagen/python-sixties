# -*- coding: utf-8 -*-
import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="sixties",
    version="0.0.1",
    description="Parsing of fixed width text databases derived in the Seventies from the Sixties' spirit of the previous century.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/sdrees/python-sixties",
    author="Stefan Hagen",
    author_email="stefan@hagen.link",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "sixties=sixties.cli:main",
        ]
    },
)
