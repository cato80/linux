"""
The program linear_fit_noerror.py uses curve_fit to do a linear fit to data
with NO uncertainty estimate for the data.
"""
# The following two commands import the program modules needed to
# run this program.
from pylab import *
from scipy.optimize import curve_fit

# This line reads the data from a the file `data_noerror.txt` and places
# into two arrays.

freq,Kmax=loadtxt('data_noerror.txt',unpack=True)

# This function defines the function to be fit. In this case a linear
# function with slope 'b' and intercept 'a'.
def func(x,intercept,slope):
    y = intercept + slope * x
    return y

# This line calls the curve_fit function. It returns two arrays.
# 'a_fit' contains the best fit parameters and 'cov' contains
# the covariance matrix.
a_fit,cov=curve_fit(func,freq,Kmax)

# The next four lines define variables for the slope, intercept, and
# there associated uncertainties d_slope and d_inter. The uncertainties
# are computed from elements of the covariance matrix.
slope = a_fit[1]
inter = a_fit[0]
d_slope = sqrt(cov[1][1])
d_inter = sqrt(cov[0][0])

# Create a graph showing the data.
plot(freq,Kmax,'ro',label='Data')

# Compute a best fit from the fit intercept and slope.
Kmax_fit = inter + slope*freq

# Create a graph of the fit to the data.
plot(freq,Kmax_fit,label='Fit')

# Display a legend, label the x and y axes and title the graph.
legend()
xlabel('Frequency (Hz)')
ylabel('Energy (J)')
title('Frequency versus maximum electron energy')

# Save the figure to a file
savefig('noerror_fit.png')

# Show the graph in a new window on the users screen.
show()

# Display the best fit values for the slope and intercept. These print
# statments illustrate how to print a mix of strings and variables.
print(f'The slope = {slope}, with uncertainty {d_slope}')
print(f'The intercept = {inter}, with uncertainty {d_inter}')
