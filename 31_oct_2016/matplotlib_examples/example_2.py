#!/usr/bin/python3

#***
#*  Plotting Exercise 1 
#*  Melanie Cornelius, mseryn, melanie.e.cornelius@gmail.com
#*
#*  3D Wire plot example
#*  
#*  Original code from tutorial located at:
#*       http://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html
#*  See license.py for information on Matplotlib demo licensing.
#*
#*  Comments added and changes made by Melanie Cornelius (mseryn@github)
#***

# Cleaned up namespace
import matplotlib.pyplot
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

# Makes an instance of figure referenced by "fig"
fig = matplotlib.pyplot.figure()

# Makes an instance of a 3D subplot referenced by "axis"
axis = fig.add_subplot(111, projection='3d')

# Makes a tuple containing some test data provided by the software
X, Y, Z = axes3d.get_test_data(0.05)

# Specifies the plot type to be a wireframe with specified data point spacings
axis.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

# Shows the plot
matplotlib.pyplot.show()
