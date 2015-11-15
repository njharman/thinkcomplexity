#!/usr/bin/env python

import os
import sys
import codecs
from setuptools import Command, find_packages, setup


# Note: This only exists so tox can automatically test. You really don't want
# to install this package.


class RunTests(Command, object):
    description = 'All the tests with coverage!'
    user_options = [('pytest-args=', 'a', 'Arguments to pass to py.test')]

    def initialize_options(self):
        self.pytest_args = [
                '--cov=thinkcomplexity',
                '--cov-report=term-missing',
                ]

    def finalize_options(self):
        if not isinstance(self.pytest_args, list):
            self.pytest_args = self.pytest_args.split(',')

    def run(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


class CleanBuild(Command, object):
    '''Remove build artifacts.'''
    user_options = list()

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        os.system('/bin/rm -rvf MANIFEST ./build ./dist ./*.egg-info')
        os.system('/usr/bin/find * -name "*py[co]" -exec /bin/rm -vf {} ";"')
        os.system('/usr/bin/find * -name "__pycache__" -exec /bin/rm -rvf {} ";"')


class CleanSuper(CleanBuild):
    '''Remove build artifacts and .tox, .cache, .coverage.'''
    def run(self):
        super(CleanSuper, self).run()
        os.system('/bin/rm -rvf .cache .tox .coverage')


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
        'superclean': CleanSuper,
        },
    )
