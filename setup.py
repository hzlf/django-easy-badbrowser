import os
from setuptools import setup, find_packages

VERSION = "1.0.7" # also in __init__.py

README = open(os.path.join(os.path.dirname(__file__), "README.textile")).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="django-easy-badbrowser",
    version=VERSION,
    packages=["badbrowser"],
    include_package_data=True,
    license="MIT License",
    description="Browser detection (including browser upgrade notices) for Django",
    long_description=README,
    url="http://github.com/bashu/django-badbrowser",
    author="Adam Charnock",
    author_email="adam@playnice.ly",
    install_requires=[
        "httpagentparser==1.2.2",
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
    zip_safe=False,
)
