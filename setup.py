#!/usr/bin/env python
import os
import sys
from setuptools import setup, find_packages

is_release = False
if "--release" in sys.argv:
    is_release = True
    sys.argv.remove("--release")

base = os.path.dirname(os.path.abspath(__file__))

README_PATH = os.path.join(base, "README.rst")

install_requires = [
    'jsonschema',
    'schematics>=2.0.0'
]

tests_require = []

setup(name='swagger-schema',
      setup_requires=["vcver"],
      vcver={
          "is_release": is_release,
          "path": base
      },
      description=(
          "a schematics-based schema for Swagger definitions."
      ),
      long_description=open(README_PATH).read(),
      author='Yusuke Tsutsumi',
      author_email='yusuke@tsutsumi.io',
      url='https://github.com/toumorokoshi/swagger-schema',
      packages=find_packages(),
      install_requires=install_requires,
      classifiers=[
          'Development Status :: 4 - Beta',
          'Operating System :: MacOS',
          'Operating System :: POSIX :: Linux',
          'Topic :: System :: Software Distribution',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
      ],
      tests_require=tests_require
)
