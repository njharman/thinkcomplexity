#!/usr/bin/env python

import codecs
import os
import os.path
import subprocess
from setuptools import Command, find_packages, setup


# Note: This only exists so tox can automatically test. You really don't want
# to install this package.


class RunTests(Command):
    '''Run all tests.'''
    description = 'run tests'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        '''Run all tests!'''
        errno = subprocess.call(['py.test', '--cov=bubba', '--cov-report=term-missing'])
        raise SystemExit(errno)


class CleanBuild(Command):
    '''Custom clean command to tidy up the project root.'''
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        os.system('rm -vrf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info */__pycache__')


this_dir = os.path.abspath(os.path.dirname(__file__))
with codecs.open(os.path.join(this_dir, 'README.rst'), encoding='utf-8') as file:
    long_description = file.read()


setup(
    name='thinkcomplexity',
    version='1.0',
    description='Exercises from book Think Complexity by Allen B. Downey',
    long_description=long_description,
    url='https://github.com/njharman/thinkcomplexity',
    author='Norman Harman',
    author_email='njharman@gmail.com',
    license='UNLICENSE',
    zip_safe=False,
    packages=find_packages(exclude=['docs', 'tests*']),
    extras_require={
        'test': ['coverage', 'pytest', 'pytest-cov'],
        },
    cmdclass={
        'test': RunTests,
        'clean': CleanBuild,
        },
    )
