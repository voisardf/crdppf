# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

requires = [
    'pyramid_oereb[recommend]==1.5.1'
]

setup(
    name='crdppfportal',
    version='3.0',
    description='SITN, public law restriction portal',
    author='sitn',
    author_email='sitn@ne.ch',
    url='http://www.ne.ch/sitn',
    install_requires=requires,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'paste.app_factory': [
            'main = crdppfportal:main',
        ],
    },
)
