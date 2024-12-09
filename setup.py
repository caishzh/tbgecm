from setuptools import setup, find_packages

def read_requirements(file):
    with open(file) as f:
        return f.read().splitlines()

def read_file(file):
    with open(file) as f:
        return f.read()

long_description = read_file("README.md")
version = read_file("VERSION")
requirements = read_requirements("requirements.txt")

setup(
    name = 'tbgecm',
    version = version,
    author = 'KitaKitaCirillasz',
    author_email = 'caishuzhede@163.com',
    url = 'https://github.com/caishzh/tbgecm',
    description = 'A numerical program for twisted bilayer graphene effective continuum model',
    long_description_content_type = "text/markdown",
    long_description = long_description,
    license = "MIT license",
    packages = find_packages(),
    install_requires = requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)