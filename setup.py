#!/usr/bin/env python

from setuptools import setup, Extension

setup(
    name='setuptools_dso',
    version="1.3",
    description="setuptools extension to build non-python shared libraries",
    long_description="""setuptools extension for building non-python shared libraries
and packaging them for distribution.  eg. for use by python extensions.

This extension provides at alternative to bundling externally built
libraries in Python Wheel packages.  This is to replace the external
build system (eg. Makefile).

If you have to ask "why", then keep moving along.  There is nothing for you to see here.
""",
    url='https://github.com/mdavidsaver/setuptools_dso',

    author='Michael Davidsaver',
    author_email='mdavidsaver@gmail.com',
    license='BSD',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Archiving :: Packaging',
    ],
    python_requires='>=2.7',

    packages=['setuptools_dso'],
    package_dir={'':'src'},
)
