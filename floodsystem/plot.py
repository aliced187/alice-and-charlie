#Task 2E - New submodule for plotting water levels
import matplotlib
from sympy import rotations
import matplotlib.pyplot as plt 
from floodsystem.analysis import polyfit
import numpy as np 

def plot_water_levels(station, dates, levels):
    typical_high = station.typical_range[1]
    typical_low = station.typical_range[0]
    #Plot 
    plt.plot(dates, levels)
    plt.axhline(y = typical_high, color = 'r', linestyle = '-')
    plt.axhline(y = typical_low, color = 'b', linestyle = '-')

    #Labelling plot
    plt.xlabel('Date')
    plt.ylabel('Water level (m)')
    plt.xticks(rotation=45)
    name = station.name 
    plt.title(name)

    #Display plot
    plt.tight_layout()

    return plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    y = polyfit(dates, levels, p)
    typical_high = station.typical_range[1]
    typical_low = station.typical_range[0]
    pol = y[0]
    
    #Plot 
    plt.plot(dates, levels, label = "$\Real data$")

    plt.axhline(y = typical_high, color = 'r', linestyle = '-')
    plt.axhline(y = typical_low, color = 'b', linestyle = '-')

    x1 = np.linspace(x[0], x[-1], 50)
    plt.plot(x1, pol(x1 - x[0]), label="$\polyfit$")

    #Labelling plot
    plt.xlabel('Date')
    plt.ylabel('Water level (m)')
    plt.xticks(rotation=45)
    name = station.name 
    plt.title(name)

    #Display plot
    plt.tight_layout()

    return plt.show()

    