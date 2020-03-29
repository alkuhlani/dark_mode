# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in dark_mode/__init__.py
from dark_mode import __version__ as version

setup(
	name='dark_mode',
	version=version,
	description='Dark Mode for Frappe',
	author='Alkuhlani',
	author_email='aalkuhlani95@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
