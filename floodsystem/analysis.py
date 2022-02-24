import matplotlib
import numpy as np 
import matplotlib.pyplot as plt
def polyfit(dates, levels, p):
    #Function computes a least-squares fit of a polynomial of a degree p to water level data
    #Function should return a tuple of (i) the polynomila object and (ii) any shift of the time(date) axis
        
    x = matplotlib.dates.date2num(dates)

    #Find coefficients of best fit polynomial f(x) of degree p

    p_coeff = np.polyfit(x - x[0], levels, p)

    #Convert coefficient into a polynomial that can be evaluated 
    poly = np.poly1d(p_coeff)

    d0 = dates[0]


    return (poly, d0)



