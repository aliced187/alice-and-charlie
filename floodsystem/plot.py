#Task 2E - New submodule for plotting water levels
from sympy import rotations
from . import datafetcher
from .station import MonitoringStation
from floodsystem.stationdata import build_station_list
import matplotlib.pyplot as plt 
import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.datafetcher import fetch_latest_water_level_data

def plot_water_levels(station, dates, levels):

    #Creating multiple plots for different stations 
    
    
    #Plot 
    plt.plot(dates, levels)

    #Labelling plot
    plt.xlabel('Date')
    plt.ylabel('Water level (m)')
    plt.xticks(rotation=45)
    name = station.name 
    plt.title(name)

    #Display plot
    plt.tight_layout()

    return plt.show()

