#!/usr/bin/python3

#***
#*  Plotting Exercise 1 
#*  Melanie Cornelius, mseryn, melanie.e.cornelius@gmail.com
#*  
#*  Make a 3D line plot.
#*
#*  Original code from tutorial located at: 
#*       http://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html
#*  See license.py for information on Matplotlib demo licensing.
#*
#*  Comments added and changes made by Melanie Cornelius (mseryn@github)
#***

import matplotlib
import matplotlib.pyplot
import numpy
from mpl_toolkits.mplot3d import Axes3D

matplotlib.rcParams['legend.fontsize'] = 10

# This specifies the current figure under the name 'fig'
fig = matplotlib.pyplot.figure()

# This asks for the current axes ("get current axes" = GCA, see why abbreviations
# are difficult?) and stores it in "axis"
axis = fig.gca(projection='3d')

# numpy.linspace gives evenly-spaced points on interval (start, end)
theta = numpy.linspace(-4 * numpy.pi, 4 * numpy.pi, 100)
z = numpy.linspace(-2, 2, 100)

# Some simple math
r = z**2 + 1
x = r * numpy.sin(theta)
y = r * numpy.cos(theta)

# Specifies the plot with its 3D projection, gives the data, and gives a title
axis.plot(x, y, z, label='parametric curve')

# Specifies to use a legend following the specifications on line 17
axis.legend()

# Shows the plot
matplotlib.pyplot.show()
