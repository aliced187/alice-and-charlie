
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
import datetime
from floodsystem.utils import sorted_by_key



def run():
    stations = build_station_list()
    update_water_levels(stations)
    names = []
    namessev = []
    nameshigh = []
    namesmod = []
    level = []
    ranges = []
    
    sevlist = stations_level_over_threshold(stations, 1)
    for l in sevlist:
        namessev.append(l[0])
    print("Severe Flood risk ( current relative water level > 1): " + str(namessev))
    #judged to be highest of risks because the water is above the highest value
    hlist = stations_level_over_threshold(stations, 0.8)
    for a in hlist:
        nameshigh.append(a[0])
    nameshighf = set(nameshigh) - set(namessev)
    mlist = stations_level_over_threshold(stations, 0.7)
    for k in mlist:
        namesmod.append(k[0])
    namesmodf = set(namesmod) - set(nameshigh)
    for station in stations:
        names.append(station.name)
    nameslow = set(names) - set(namesmod)


run()
         
