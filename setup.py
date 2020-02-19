#!/usr/bin/env python

from setuptools import setup

setup(
    name="concattabs",
    version="0.0.1",
    description="Append rows from other tabs to this tab",
    author="Adam Hooper",
    author_email="adam@adamhooper.com",
    url="https://github.com/CJWorkbench/concattabs",
    packages=[""],
    py_modules=["concattabs"],
    install_requires=["pandas==0.25.0"],
)
