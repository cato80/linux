"""
The program linear_fit_error.py uses curve_fit to do a linear fit to data
with uncertainty estimate for the y-axis data.
"""
# The following two commands import the program modules needed to
# run this program.
from pylab import *
from scipy.optimize import curve_fit

# This line reads the data from a the file `data_error.txt` places into three
# arrays.

freq,Kmax,d_Kmax=loadtxt('data_error.txt',unpack=True)

# This function defines the function to be fit. In this case a linear
# function with slope 'b' and intercept 'a'.
def func(x,intercept,slope):
    y = intercept + slope * x
    return y

# This line calls the curve_fit function. It returns two arrays.
# 'a_fit' contains the best fit parameters and 'cov' contains
# the covariance matrix.
a_fit,cov=curve_fit(func,freq,Kmax,sigma=d_Kmax)

# The next four lines define variables for the slope, intercept, and
# there associated uncertainties d_slope and d_inter. The uncertainties
# are computed from elements of the covariance matrix.
slope = a_fit[1]
inter = a_fit[0]
d_slope = sqrt(cov[1][1])
d_inter = sqrt(cov[0][0])

# Create a graph showing the data.
errorbar(freq,Kmax,yerr=d_Kmax,fmt='r.',label='Data')

# Compute a best fit from the fit intercept and slope.
Kmax_fit = inter + slope*freq

# Create a graph of the fit to the data. We just use the ordinary plot
# command for this.
plot(freq,Kmax_fit,label='Fit')

# Display a legend, label the x and y axes and title the graph.
legend()
xlabel('Frequency (Hz)')
ylabel('Energy (J)')
title('Frequency versus maximum electron energy')

# Save the figure to a file
savefig('error_fit.png')

# Show the graph in a new window on the users screen.
show()

# Display the best fit values for the slope and intercept. These print
# statments illustrate how to print a mix of strings and variables.
print(f'The slope = {slope}, with uncertainty {d_slope}')
print(f'The intercept = {inter}, with uncertainty {d_inter}')

# We can estimate the goodness of fit for a fit to data with uncertainties by
# computing the reduced chi-squared statistic. For a good fit it should be
# approximatly equal to one.
chisqr = sum((Kmax-func(freq,inter,slope))**2/d_Kmax**2)
dof = len(Kmax) - 2
chisqr_red = chisqr/dof
print(f'Reduced chi^2 = {chisqr_red}')
