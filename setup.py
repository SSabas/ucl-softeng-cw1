
from setuptools import setup, find_packages

setup(
    name = "adventure",
    version = "1.0.0",
    author='Sven Sabas',
    author_email='sven.sabas.17@ucl.ac.uk',
    license='The MIT License (MIT)',
    packages = find_packages(exclude=['*test']),
    scripts = ['scripts/adventure'],
    install_requires = ['argparse','random','copy']
)
