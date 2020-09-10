# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

setup(
    name='discount-calculator',
    version='1.0.0',
    description='Project to calculate discount by product and user',
    long_description=readme,
    author='Rudge Ferreira',
    author_email='rudgee@gmail.com',
    url='https://github.com/Rudge/example-grpc-integration/discount-calculator-service',
    packages=find_packages(exclude=('tests', 'docs'))
)