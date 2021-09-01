#!/usr/bin/env python
# Learn more: https://github.com/kennethreitz/setup.py
import os
import sys

from codecs import open

from setuptools import setup
from setuptools.command.test import test as TestCommand

here = os.path.abspath(os.path.dirname(__file__))

# 'setup.py publish' shortcut.
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')
    sys.exit()

packages = ['awsglue']

requires = []
test_requirements = []

with open('awsglue/README.md', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name="awsglue-dev",
    version="0.0.1",
    description="AWS Glue Dev",
    long_description=readme,
    long_description_content_type='text/markdown',
    packages=packages,
    package_data={'': ['LICENSE', 'NOTICE']},
    package_dir={'awsglue': 'awsglue'},
    include_package_data=True,
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*",
    install_requires=requires,
    license="Amazon Software License 1.0",
    zip_safe=False,
)
