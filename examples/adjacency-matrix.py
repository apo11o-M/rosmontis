from rosmontis import renderGraphMatrix

# 1 indicates there is an edge, 0 indicates no connection
# One can change the 1 into other numbers and use it to represent the weight of
# the edges

# ------------------------------------------------------------------------------
# Unweighted, Undirect
# Create a graph using adjacency matrix as representation
adjMatrix1 = [
    [None, "A", "B", "C", "D", "E", "F"],
    ["A",   0,   0,   0,   0,   1,   1 ],
    ["B",   0,   0,   1,   0,   0,   1 ],
    ["C",   0,   1,   0,   1,   0,   0 ],
    ["D",   0,   0,   1,   0,   1,   1 ],
    ["E",   1,   0,   0,   1,   0,   1 ],
    ["F",   1,   1,   0,   1,   1,   0 ]
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
