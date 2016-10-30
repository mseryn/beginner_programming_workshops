#!/usr/bin/python3

#***
#*  Plotting Exercise 1 
#*  Melanie Cornelius, mseryn, melanie.e.cornelius@gmail.com
#*  
#*  Intricate coloring in 3D
#*  
#*  Original code from tutorial located at:
#*       http://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html
#*  See license.py for information on Matplotlib demo licensing.
#*
#*  Comments prefaced with mseryn: are changes made by Melanie Cornelius (mseryn@github)
#***

import numpy
import matplotlib.pyplot
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# mseryn: Sets a few parameters for use
n_angles = 36
n_radii = 8

# An array of radii
# Does not include radius r=0, this is to eliminate duplicate points
radii = numpy.linspace(0.125, 1.0, n_radii)

# An array of angles
# mseryn: Makes an array of equally-spaced points on the range (start, stop)
# mseryn: Specifies the number of points to ne n_angles set above
angles = numpy.linspace(0, 2*numpy.pi, n_angles, endpoint=False)

# Repeat all angles for each radius
# mseryn: copys an array n_radii number of times and specifies to use
#         the 1st axis
angles = numpy.repeat(angles[..., numpy.newaxis], n_radii, axis=1)

# Convert polar (radii, angles) coords to cartesian (x, y) coords
# (0, 0) is added here. There are no duplicate points in the (x, y) plane
# mseryn: numpy.append simply appends to a numpy array - not a standard array
# mseryn: Uses some simple math to manipulate above data, then flattens - 
#         flattening is simply turning some dimensional array to a 1D array
x = numpy.append(0, (radii*numpy.cos(angles)).flatten())
y = numpy.append(0, (radii*numpy.sin(angles)).flatten())

# Pringle surface
# mseryn: More simple math
z = numpy.sin(-x*y)

# mseryn: Makes an instance of figure referenced by "fig"
fig = matplotlib.pyplot.figure()

# mseryn: Sets the current axis as a 3D projection
axis = fig.gca(projection='3d')

# mseryn: Specifies the plot surface is a tri-surface
# mseryn: A tri-surface is made using triangular pieces taked together
axis.plot_trisurf(x, y, z, cmap=cm.jet, linewidth=0.2)

# mseryn: Shows the plot
matplotlib.pyplot.show()
