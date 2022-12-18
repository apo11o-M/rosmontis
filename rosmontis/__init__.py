"""
Create graph images with help of the graphviz module.

This module simplified the steps of creating a graph, where it adds the nodes and edges automatically from the inputed data structure to graphviz, creating the graph in one function call.
"""

from .rosmontis import renderGraphDict
from .rosmontis import renderGraphList
from .rosmontis import renderGraphMatrix
