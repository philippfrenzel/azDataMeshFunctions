import os
import sys

from setuptools import setup
from sqlalchemy.orm import registry

__prog__ = 'eventbooking'
__version__ = '0.0.3'

mapper_registry = registry()

def read_content(filepath):
    with open(filepath) as fobj:
        return fobj.read()

classifiers = [
    "Development Status :: 1 - Development/Unstable",
    "Intended Audience :: Developers",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: Implementation :: CPython",
    "Topic :: Software Development",
    "Topic :: System :: Software Distribution"
]

requires = ['wheel',
    'azure-common',
    'azure-functions',
    'azure-identity',
    'azure-keyvault-secrets',
    'azure-storage-blob',
    'jsonschema',
    'pyodbc',
    'python-dotenv',
    'pytest',
    'logging',
    'setuptools',
    'sqlalchemy']

long_description = (
    read_content("readme.md"))

setup(name=__prog__,
      version=__version__,
      description='azDataMesh Package',
      long_description=long_description,
      long_description_content_type='text/x-rst',
      author='Philipp Frenzel',
      author_email='philipp.frenzel@swica.ch',
      url='https://github.com/philippfrenzel/azDataMeshFunctions',
      classifiers=classifiers,
      packages=['azDataMesh'],
      data_files=[],
      install_requires=requires,
      include_package_data=True
      )