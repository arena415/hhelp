# setup.py
from setuptools import setup, find_packages

setup(
    name="hhelp",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "google-generativeai",
        "nbformat",
        "nbconvert",
        "PyPDF2",
    ],
)
