# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from re import I
from .utils import sorted_by_key  #noqa

from haversine import haversine #noqa
from collections import Counter
from . import datafetcher
from .station import MonitoringStation
from floodsystem.stationdata import build_station_list


def stations_by_distance(stations, p):
    #Function for list of stations and distance from a point p

    #stations = build_station_list()
    names = []
    distance = []
    towns = []
    for station in stations:
        names.append(station.name)
        towns.append(station.town)
        distance.append(haversine(p, station.coord))
    #Create a list of tuples and sort them 
    output = list(zip(names, towns, distance))    
    output = sorted_by_key(output, 2)
    return output
    
def stations_within_radius(stations, centre, r):
    #Function to return list of names of stations with a radius, 'r', of a point 'centre'
    x = stations_by_distance(stations, centre)
    test = []
    for i in x:
        if i[2] < r:
            test.append(i[0])
    return test
    
def rivers_with_stations(stations):
    #create and empty set
    names = set()
    for i in stations:
        names.add(i.river)
    
    output = list(sorted(names))
            
    return output 

def stations_by_river(stations):
    #Function that returns a dict that maps river names (key) to a list of station objects on that river
    river_dict = {}
    for station in stations:
        river_dict[station.river] = None
    
    for river in river_dict:
        river_stations = []
        for station in stations:
            if station.river == river:
                river_stations += [station.name]
        
        river_dict[river] = river_stations
    
    return (river_dict)

    

    
    
#create a list of stations for one river 

def rivers_by_station_number(stations, N):
    rnames = []
    c = 0
    for station in stations:
        rnames.append(station.river)
    drivstat = Counter(rnames)
    rivstat = drivstat.items()
    sortrivstat = sorted(rivstat,key=lambda x: x[1], reverse=True)
    rivnum = [item[1] for item in sortrivstat]
    last = N - 1
    lastval = rivnum[last] 
    for x in range(len(rivnum)):
        if rivnum[x] >= lastval:
            c += 1
    return  sortrivstat[:c]
    



    
    
