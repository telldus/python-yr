#!/usr/bin/env python2

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='python-yr',
    version='1.4.6',
    description='Get the forecast from the norwegian wheather service yr.no in python',
    long_description=open('README.rst').read() + '\n' + open('CHANGES.rst').read(),
    author='Alexander Hansen',
    author_email='alexander@alexanderhansen.no',
    maintainer='Hugo Shamrock',
    maintainer_email='hugo.shamrock@gmail.com',
    url='https://github.com/wckd/python-yr',
    packages=['yr'],
    classifiers=[  # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Programming Language :: Python :: 3',
        'Programming Language :: Python',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Internet',
    ],
    package_data={
        'yr': [
            'languages/*.json',
        ],
    },
    install_requires=['xmltodict'],  # $$solve$$ ~> /usr/lib/python3.4/distutils/dist.py:260: UserWarning: Unknown distribution option: 'install_requires' warnings.warn(msg)
)
