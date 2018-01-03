
from setuptools import setup, find_packages

setup(
    name="Dungeon Adventure",
    version="1.0.0",
    author='Sven Sabas',
    author_email='sven.sabas.17@ucl.ac.uk',
    license='The MIT License (MIT)',
    packages=find_packages(exclude=['*test']),
    entry_points={'console_scripts': ['hunt = adventure.command:run_dungeon']},
    install_requires=['argparse', 'yaml']
)
