#!/usr/bin/env python
from setuptools import setup, find_packages

VERSION = "0.1.3b" # also in __init__.py

import os
long_description = open(os.path.join(os.path.dirname(__file__), "README.textile")).read()

setup(
	name="django-badbrowser",
	version=VERSION,
	url="http://github.com/adamcharnock/django-badbrowser",
	download_url="git@github.com:adamcharnock/django-badbrowser.git",
	description="Browser detection (including browser upgrade notices) for Django",
	long_description=long_description,
	author="Adam Charnock",
	author_email="adam@playnice.ly",
	platforms=["any"],
	license="MIT",
	packages=[
		"badbrowser",
	],
	classifiers=[
		"Development Status :: 4 - Beta",
		"License :: OSI Approved :: MIT License",
		"Environment :: Web Environment",
		"Framework :: Django",
		"Intended Audience :: Developers",
		"Operating System :: OS Independent",
		"Programming Language :: Python",
		"Topic :: Software Development :: Libraries :: Application Frameworks",
		"Topic :: Software Development :: Libraries :: Python Modules",
		"Topic :: Internet :: WWW/HTTP :: Browsers",
	],
	install_requires=[
		"httpagentparser==1.2.2",
	],
	zip_safe=False,
	include_package_data=True,
)
