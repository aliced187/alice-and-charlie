# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from re import I
from .utils import sorted_by_key  # noqa

from haversine import haversine
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
    #create empty dictionary
    one = {}
    stations = build_station_list()
    rivers = rivers_with_stations(stations)

    for i in rivers:
        x = {i: 0}
        one.update(x)
    y = []
    
#create a list of stations for one river 