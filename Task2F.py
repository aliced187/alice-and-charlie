from distutils.command.build import build

from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime
from floodsystem.utils import sorted_by_key
from matplotlib import dates
from floodsystem import analysis
import numpy as np


def run():
    stations = build_station_list()
    update_water_levels(stations)

    #Create list of station names and levels 
    names = []
    level = []
    
    for station in stations:
        if station.latest_level == None:
            pass
        elif station.latest_level > 90:
            pass
        else:
            level.append(station.latest_level)
            names.append(station.name)

    #Create a list of tuples and sort them 
    output = list(zip(names, level))  
    output = sorted_by_key(output, 1)

    #5 stations with highest relative water level
    x = output[-5:]

    names = []

    for i in x:
        names.append(i[0])
    
    for station in stations:
        if station.name in names:
            dates, levels = fetch_measure_levels(station.measure_id, dt = datetime.timedelta(days=2))
            plot_water_level_with_fit(station, dates, levels, 4)
         
if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
