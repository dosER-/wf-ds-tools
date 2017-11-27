# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


PACKAGE_NAME = 'wf-ds-tools'

__version__ = '1.0.4'


setup(
    name=PACKAGE_NAME,
    version=__version__,
    url='http://pypi.wargaming.net/metagames/dev/{}/'.format(PACKAGE_NAME),
    maintainer='Konstantin Kovalev',
    maintainer_email='xxx@xxx.com',
    description='WF DS Tools',
    long_description='',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: Other/Proprietary License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7.x+',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'numpy==1.13.3',
        'scikit-learn==0.19.1',
        'scipy==1.0.0',
    ],
    dependency_links=[
        'https://pypi.python.org/simple/scipy',
    ],
    scripts=[
        'src/dst'
    ],
)
