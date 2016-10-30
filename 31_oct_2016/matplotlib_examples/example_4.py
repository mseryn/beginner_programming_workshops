#!/usr/bin/python3

#***
#*  Plotting Exercise 1 
#*  Melanie Cornelius, mseryn, melanie.e.cornelius@gmail.com
#*  
#*  Making 3D surface plot
#*
#*  Original code from tutorial located at: 
#*       http://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html
#*  See license.py for information on Matplotlib demo licensing.
#*
#*  Comments added and changes made by Melanie Cornelius (mseryn@github)
#***

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot
import numpy

# Makes an instance of figure directly and stores its reference in "fig"
fig = matplotlib.pyplot.figure()

# Makes a subplot of "fig", and stores in it a 3D plot referenced by "axis"
axis = fig.add_subplot(111, projection='3d')

# Makes evenly-spaced points in range (start, end)
u = numpy.linspace(0, 2 * numpy.pi, 100)
v = numpy.linspace(0, numpy.pi, 100)

# Takes the outer-product of two vectors specified by above points
x = 10 * numpy.outer(numpy.cos(u), numpy.sin(v))
y = 10 * numpy.outer(numpy.sin(u), numpy.sin(v))
z = 10 * numpy.outer(numpy.ones(numpy.size(u)), numpy.cos(v))

# Specifies a surface plot with the parameters made above
# Sets the color to blue
# Sets size of stride used to show points in dataset
axis.plot_surface(x, y, z, rstride=4, cstride=4, color='b')

# Shows the plot
matplotlib.pyplot.show()
