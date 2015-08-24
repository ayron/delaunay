from random import randint, seed
from math import ceil, sqrt, log, floor

import delaunay as D

seed(4)
n = 20
xs = [randint(1, 98) for x in range(n)]
ys = [randint(1, 98) for x in range(n)]
zs = [0 for x in range(n)]

DT = D.Delaunay_Triangulation()
for x, y in zip(xs, ys):
    DT.AddPoint(D.Point(x, y))

XS, YS, TS = DT.export()

print xs
print ys

#print XS
#print YS
#print TS

"""
Creating and plotting unstructured triangular grids.
"""
import matplotlib.pyplot as plt
import matplotlib.tri as tri
import math

# Creating a Triangulation without specifying the triangles results in the
# Delaunay triangulation of the points.

# Create the Triangulation; no triangles so Delaunay triangulation created.
triang = tri.Triangulation(xs, ys)

# Plot the triangulation.
fig, ax = plt.subplots()
ax.margins(0.1)
ax.set_aspect('equal')
ax.triplot(triang, 'bo-')

ax.triplot(tri.Triangulation(XS, YS, TS), 'ro--')
ax.set_title('triplot of Delaunay triangulation')


xx = [0, 99, 99, 0] + xs
yy = [0, 0, 99, 99] + ys

tt = [(5,4,0),
(5,0,3),
(8,5,3),
(9,1,0),
(10,2,1),
(13,0,4),
(13,4,9),
(14,9,4),
(14,6,11),
(14,11,12),
(15,9,0),
(15,0,13),
(15,13,9),
(16,3,2),
(16,8,3),
(17,7,5),
(17,5,8),
(17,8,16),
(17,16,7),
(18,4,5),
(18,5,6),
(18,6,14),
(18,14,4),
(19,1,9),
(19,9,14),
(19,14,12),
(19,12,10),
(19,10,1),
(20,16,2),
(20,2,10),
(21,11,10),
(21,10,12),
(21,12,11),
(22,6,16),
(22,16,20),
(22,20,10),
(22,10,11),
(22,11,6),
(23,6,5),
(23,5,7),
(23,7,16),
(23,16,6)]



ax.triplot(tri.Triangulation(xx, yy, tt), 'go--')

plt.show()

