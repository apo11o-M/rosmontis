from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = "Create graph images with help of graphviz module"
LONG_DESCRIPTION = "This module simplified the steps of creating a graph, where it adds the nodes and edges automatically from the inputed data structure to graphviz, creating the graph in one function call."

setup(
    name = "rosmontis", 
    version = VERSION,
    author = "Rick Wang",
    author_email = "yenhao0508@gmail.com",
    license = "MIT",
    description = DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["graphviz"],
    python_requires='>=3',
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