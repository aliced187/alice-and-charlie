import string
from floodsystem.geo import stations_by_distance


from re import I
from floodsystem.utils import sorted_by_key  # noqa

from haversine import haversine
import floodsystem.datafetcher
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list

def test_stations_by_distance():

    #Build test station list 
    stations = build_station_list()
    
    #Point to test 
    p =(52.2053, 0.1218)

    x = stations_by_distance(stations, p)

    #Test sorting of distance of tuples in list
    assert x[0][2] < x[1][2]
    #assert x[i][2] < x[i + 1][2]

    #Test output is a tuple, first two entries in tuple are strings and final entry in tuple is a float 

    assert type(x[0]) == tuple
    assert type(x[0][0]) and type(x[0][1]) == string
    assert type(x[0][2]) == float

    #Test that there is an output

    assert len(x) > 0