
import datetime
from distutils.command import build 
from matplotlib.pyplot import plot
from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.utils import sorted_by_key

def run():
    stations = build_station_list()
    #Programme to plot water levels over the past 10 days for 5 stations at which current relative water level is greatest 
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
            dates, levels = fetch_measure_levels(station.measure_id, dt = datetime.timedelta(days=10))
            plot_water_levels(station, dates, levels)

   # for station in stations:
    #    if station.name == 'Letcombe Basset':
     #       dates, levels = fetch_measure_levels(station.measured_id, dt = datetime.timedelta(days=10))
  
           
  
    
run()


