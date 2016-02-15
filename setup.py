#! /usr/bin/env python

from distutils.core import setup

setup(name='koine-nlp',
      version='0.2',
      description='A library for common NLP-related tasks for Koine Greek.',
      long_description=open("README.rst").read(),
      author='Nathan D. Smith',
      author_email='nathan@smithfam.info',
      url='http://koine-nlp.nathan.smithfam.info/',
      packages=['koinenlp'],
      package_data={'koinenlp': ['doc/_build/text/*.txt']},
      license="MIT",
      classifiers=["Development Status :: 5 - Production/Stable",
                   "Programming Language :: Python",
                   "Programming Language :: Python :: 2",
                   "Programming Language :: Python :: 2.7",
                   "Programming Language :: Python :: 3",
                   "Programming Language :: Python :: 3.3",
                   "Programming Language :: Python :: 3.4",
                   "Programming Language :: Python :: 3.5",
                   "Operating System :: OS Independent",
                   "Operating System :: POSIX",
                   "Intended Audience :: End Users/Desktop"])
