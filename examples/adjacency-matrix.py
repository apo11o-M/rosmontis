from collections import defaultdict
from rosmontis import renderGraphMatrix

# g[i] = [node1, node2], meaning there is a undirected path
# from node1 to node2
g1 = [["A", "B"], ["A", "E"], ["B", "E"], 
      ["B", "C"], ["C", "D"], ["D", "E"], ["D", "F"]]

g2 = [["A", "B", 2], ["A", "E", 0.5], ["B", "E", 0.2], 
      ["B", "C", 3], ["C", "D", 7], ["D", "E", 0.15], ["D", "F", 1.6]]

# ------------------------------------------------------------------------------
# Unweighted, Undirect
# Create a graph using adjacency matrix as representation
adjMatrix1 = [
    [None, "A", "B", "C", "D", "E", "F"],
    ["A",   0,   1,   0,   0,   1,   0 ],
    ["B",   1,   0,   1,   0,   1,   0 ],
    ["C",   0,   1,   0,   1,   0,   0 ],
    ["D",   0,   0,   1,   0,   1,   1 ],
    ["E",   1,   1,   0,   1,   0,   0 ],
    ["F",   0,   0,   0,   1,   0,   0 ]
]

# output a png image representing the graph in the same
# directory of this file.
renderGraphMatrix(graph=adjMatrix1, graphName="unweighted-undirect", 
                          weighted=False, directed=False)

# ------------------------------------------------------------------------------
# Unweighted, Direct
adjMatrix2 = [
    [None, "A", "B", "C", "D", "E", "F"],
    ["A",   0,   1,   0,   0,   1,   0 ],
    ["B",   0,   0,   1,   0,   1,   0 ],
    ["C",   0,   0,   0,   1,   0,   0 ],
    ["D",   0,   0,   0,   0,   1,   1 ],
    ["E",   0,   0,   0,   0,   0,   0 ],
    ["F",   0,   0,   0,   0,   0,   0 ]
]

renderGraphMatrix(graph=adjMatrix2, graphName="unweighted-direct",
                          weighted=False, directed=True)

# ------------------------------------------------------------------------------
# Weighted, Undirect
adjMatrix3 = [
    [None, "A",   "B",   "C",   "D",   "E",   "F"  ],
    ["A",   0,     2,     0,     0,     0.5,   0   ],
    ["B",   2,     0,     3,     0,     0.2,   0   ],
    ["C",   0,     3,     0,     7,     0,     0   ],
    ["D",   0,     0,     7,     0,     0.15,  1.6 ],
    ["E",   0.5,   0.2,   0,     0.15,  0,     0   ],
    ["F",   0,     0,     0,     1.6,   0,     0   ]
]

renderGraphMatrix(graph=adjMatrix3, graphName="weighted-undirect", 
                          weighted=True, directed=False)

# ------------------------------------------------------------------------------
# Weighted, Direct
adjMatrix4 = [
    [None, "A",   "B",   "C",   "D",   "E",   "F"  ],
    ["A",   0,     2,     0,     0,     0.5,   0   ],
    ["B",   0,     0,     3,     0,     0.2,   0   ],
    ["C",   0,     0,     0,     7,     0,     0   ],
    ["D",   0,     0,     0,     0,     0.15,  1.6 ],
    ["E",   0,     0,     0,     0,     0,     0   ],
    ["F",   0,     0,     0,     0,     0,     0   ]
]
renderGraphMatrix(graph=adjMatrix4, graphName="weighted-direct",
                          weighted=True, directed=True)
