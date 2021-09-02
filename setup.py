from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name='ampl-parser',
    version='0.0.1',
    description='A AMPL Parser',
    long_description=long_description,
    packages=['ampl_parser'],
    install_requires=[
        'pytest',
        'parsimonious',
    ]
)
