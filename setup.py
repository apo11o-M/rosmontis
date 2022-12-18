import pathlib
from setuptools import setup, find_packages

VERSION = "1.0.0"
DESCRIPTION = "Create graph images with help of graphviz module"
LONG_DESCRIPTION = pathlib.Path('README.md').read_text(encoding='utf-8')

setup(
    name = "rosmontis", 
    version = VERSION,
    author = "Rick Wang",
    author_email = "yenhao0508@gmail.com",
    license = "MIT",
    description = DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    long_description_content_type = "text/markdown",
    url = "https://github.com/apo11o-m/rosmontis",

    python_requires='>=3',
    packages=find_packages(),
    install_requires=["graphviz"],
    keywords = ["graph", "visualization", "dot", "render"],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
)