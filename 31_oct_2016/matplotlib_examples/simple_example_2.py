#***
#*  Simple Plotting Exercise 2 
#*  Melanie Cornelius, mseryn, melanie.e.cornelius@gmail.com
#*  
#*  Make a simple line plot.
#*  Augment the plot with labels, color changes, etc.
#***

# Importing plotting package
import matplotlib.pyplot

# Making simple sample data sets
sample_x_data = [1,2,5,7,11,13,14,16]
sample_y_data = [x for x in range(1, len(sample_x_data) + 1)]

# Making a figure and an axis object

# Giving the data points to the plot
matplotlib.pyplot.plot(sample_x_data, sample_y_data, 'ro')

# Giving the plot a title and axis labels
matplotlib.pyplot.title("Sample Plot 2")
matplotlib.pyplot.xlabel("Sample x Points")
matplotlib.pyplot.ylabel("Sample y Points")

# Adjusting the axis range
matplotlib.pyplot.axis([0, 25, 0, 15])

# Showing the plot
matplotlib.pyplot.show()
