#***
#*  Simple Plotting Exercise 3 
#*  Melanie Cornelius, mseryn, melanie.e.cornelius@gmail.com
#*  
#*  Make a simple line plot.
#*  Showing use of figure and subplots to simplify modification of attributes.
#***

# Importing plotting package
import matplotlib.pyplot

# Making simple sample data sets
sample_x_data = [1,2,5,7,11,13,14,16]
sample_y_data = [x for x in range(1, len(sample_x_data) + 1)]

# Making a figure and an axis object
figure, axis = matplotlib.pyplot.subplots()

# Giving the data points to the plot
axis.plot(sample_x_data, sample_y_data, lw=2)

# Giving the plot a title and axis labels
axis.set_title("Sample Plot 2")
axis.set_xlabel("Sample x Points")
axis.set_ylabel("Sample y Points")

# Adjusting the axis range
axis.set_xlim([0, 25])
axis.set_ylim([0, 15])

# Showing the plot
matplotlib.pyplot.show()
