# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa

from haversine import haversine
from . import datafetcher
from .station import MonitoringStation
from floodsystem.stationdata import build_station_list


def stations_by_distance(stations, p):
    #Function for list of stations and distance from a point p

    stations = build_station_list()
    names = []
    distance = []
    for station in stations:
        names.append(station.name)
        distance.append(haversine(p, station.coord))
    #Create a list of tuples and sort them 
    output = list(zip(names, distance))    
    output = sorted_by_key(output, 1)
    return output
    
def stations_within_radius(stations, centre, r):
    #Function to return list of names of stations with a radius, 'r', of a point 'centre'
    x = stations_by_distance(stations, centre)
    test = []
    for i in x:
        if i[1] < r:
            test.append(i[0])
    return test
    

  