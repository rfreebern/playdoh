import os

from setuptools import setup, find_packages
from project_module import PROJECT_MODULE

setup(name=PROJECT_MODULE,
      version='1.0',
      description='Django application.',
      long_description='',
      author='',
      author_email='',
      license='',
      url='',
      include_package_data=True,
      classifiers = [],
      packages=find_packages(exclude=['tests']),
      install_requires=[])
