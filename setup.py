# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

long_desc = """
This package contains the sphinxcontrib-golangdomain Sphinx extension.

This extension adds golang Domain to Sphinx.
It needs Sphinx 1.0 or newer, and sphinx-autoapi 1.8.3 or newer
"""

requires = ["Sphinx>=1.0" "sphinx-autoapi>=1.8.3"]

setup(
    name="sphinxcontrib-golangdomain",
    version="0.2.0",
    url="https://github.com/chrisdoherty4/sphinxcontrib-golangdomain",
    download_url="https://github.com/chrisdoherty4/sphinxcontrib-golangdomain",
    license="BSD",
    author="Chris Doherty",
    author_email="chris dot doherty4 at gmail dot com",
    description="Sphinx extension sphinxcontrib-golangdomain",
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Documentation",
        "Topic :: Utilities",
    ],
    platforms="any",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=["sphinxcontrib"],
)
