import string
from floodsystem.geo import stations_by_distance, stations_by_river, stations_within_radius, rivers_with_stations, rivers_by_station_number, inconsistent_typical_range_stations


from re import I
from floodsystem.utils import sorted_by_key  # noqa

from haversine import haversine
import floodsystem.datafetcher
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list

def test_stations_by_distance():

    #Build test station list 
    station1 = MonitoringStation(station_id= 'stn_id_1',
                                 measure_id= 'measure_id_1',
                                 label= 'Test 1',
                                 coord= (0.0, 1.0),
                                 typical_range= (0.0, 1.0),
                                 river= 'river1',
                                 town= 'town1' )
    station2 = MonitoringStation(station_id= 'stn_id_2',
                                 measure_id= 'measure_id_2',
                                 label= 'Test 2',
                                 coord= (1.0, 1.0),
                                 typical_range= (0.0, 1.0),
                                 river= 'river2',
                                 town= 'town2' )

    stations = [station1, station2]
    
    #Point to test 
    p =(0.0, 0.0)

    x = stations_by_distance(stations, p)

    #Test sorting of distance of tuples in list
    assert x[0][2] < x[1][2]

    #Test output is a tuple, first two entries in tuple are strings and final entry in tuple is a float 

    assert type(x[0]) == tuple
    assert type(x[0][0]) and type(x[0][1]) == str
    assert type(x[0][2]) == float

    #Test that there is an output

    assert len(x) > 0

    #Test correct outputs

    assert x[0][0:2] == ('Test 1', 'town1')
    assert x[1][0:2] == ('Test 2', 'town2')


def test_stations_within_radius():
    
    #Build list of stations
    station1 = MonitoringStation(station_id= 'stn_id_1',
                                 measure_id= 'measure_id_1',
                                 label= 'Test 1',
                                 coord= (0.0, 1.0),
                                 typical_range= (0.0, 1.0),
                                 river= 'river1',
                                 town= 'town1' )
    station2 = MonitoringStation(station_id= 'stn_id_2',
                                 measure_id= 'measure_id_2',
                                 label= 'Test 2',
                                 coord= (1.0, 1.0),
                                 typical_range= (0.0, 1.0),
                                 river= 'river2',
                                 town= 'town2' )
    station3 = MonitoringStation(station_id= 'stn_id_3',
                                 measure_id= 'measure_id_3',
                                 label= 'Test 3',
                                 coord= (100.0, 100.0),
                                 typical_range= (0.0, 1.0),
                                 river= 'river3',
                                 town= 'town3' )
    
    stations = [station1, station2, station3]
    #Centre point and radius 
    centre = (0.0, 0.0)
    r = 200 

    #Naming function to test
    x = stations_within_radius(stations, centre, r)

    #Test type of output
    assert type(x) == list
    assert type(x[0]) == str 

    #Test correct output
    assert len(x) == 2
    assert x[0] == 'Test 1'
    assert x[1] == 'Test 2'
    
def test_rivers_with_stations():

    #Create test station list 
    station1 = MonitoringStation(station_id= 'stn_id_1',
                                 measure_id= 'measure_id_1',
                                 label= 'Test 1',
                                 coord= (0.0, 1.0),
                                 typical_range= (0.0, 1.0),
                                 river= 'river1',
                                 town= 'town1' )
    station2 = MonitoringStation(station_id= 'stn_id_2',
                                 measure_id= 'measure_id_2',
                                 label= 'Test 2',
                                 coord= (1.0, 1.0),
                                 typical_range= (0.0, 1.0),
                                 river= 'river2',
                                 town= 'town2' )
    station3 = MonitoringStation(station_id= 'stn_id_3',
                                 measure_id= 'measure_id_3',
                                 label= 'Test 3',
                                 coord= (100.0, 100.0),
                                 typical_range= (0.0, 1.0),
                                 river= 'river2',
                                 town= 'town3' )

    stations = [station1, station2, station3]
    output = rivers_with_stations(stations)
    #Test type of output
    assert type(output) == list

    #Test correct output
    assert 'river1' in output
    assert 'river2' in output
    assert 'river3' not in output



def test_stations_by_river():

    #Define station list 
    station1 = MonitoringStation(station_id= 'stn_id_1',
                                 measure_id= 'measure_id_1',
                                 label= 'Test 1',
                                 coord= (0.0, 1.0),
                                 typical_range= (0.0, 1.0),
                                 river= 'river1',
                                 town= 'town1' )
    station2 = MonitoringStation(station_id= 'stn_id_2',
                                 measure_id= 'measure_id_2',
                                 label= 'Test 2',
                                 coord= (1.0, 1.0),
                                 typical_range= (0.0, 1.0),
                                 river= 'river2',
                                 town= 'town2' )
    station3 = MonitoringStation(station_id= 'stn_id_3',
                                 measure_id= 'measure_id_3',
                                 label= 'Test 3',
                                 coord= (100.0, 100.0),
                                 typical_range= (0.0, 1.0),
                                 river= 'river2',
                                 town= 'town3' )

    stations = [station1, station2, station3]

    x = stations_by_river(stations)

    #Test type of output
    assert type(x) == dict
    assert x['river2'] == ['Test 2', 'Test 3']
    assert x['river1'] == ['Test 1']
    

def test_rivers_by_station_number():
    #Create test station list 
    station1 = MonitoringStation(station_id= 'stn_id_1',
                                 measure_id= 'measure_id_1',
                                 label= 'Test 1',
                                 coord= (0.0, 1.0),
                                 typical_range= (0.0, 1.0),
                                 river= 'river1',
                                 town= 'town1' )
    station2 = MonitoringStation(station_id= 'stn_id_2',
                                 measure_id= 'measure_id_2',
                                 label= 'Test 2',
                                 coord= (1.0, 1.0),
                                 typical_range= (0.0, 1.0),
                                 river= 'river2',
                                 town= 'town2' )
    station3 = MonitoringStation(station_id= 'stn_id_3',
                                 measure_id= 'measure_id_3',
                                 label= 'Test 3',
                                 coord= (100.0, 100.0),
                                 typical_range= (0.0, 1.0),
                                 river= 'river2',
                                 town= 'town3' )
    stations = [station1, station2, station3]
    N = 2
    outputr = rivers_by_station_number(stations, N)
    #Test type of output
    assert type(outputr) == list
    #Test output
    assert outputr == [('river2', 2),('river1', 1)]

def test_inconsistent_typical_range_stations():

    #Create test station list 
    station1 = MonitoringStation(station_id= 'stn_id_1',
                                 measure_id= 'measure_id_1',
                                 label= 'Test 1',
                                 coord= (0.0, 1.0),
                                 typical_range= (0.0, 1.0),
                                 river= 'river1',
                                 town= 'town1' )
    station2 = MonitoringStation(station_id= 'stn_id_2',
                                 measure_id= 'measure_id_2',
                                 label= 'Test 2',
                                 coord= (1.0, 1.0),
                                 typical_range= (5.0, 1.0),
                                 river= 'river2',
                                 town= 'town2' )
    station3 = MonitoringStation(station_id= 'stn_id_3',
                                 measure_id= 'measure_id_3',
                                 label= 'Test 3',
                                 coord= (100.0, 100.0),
                                 typical_range= (None),
                                 river= 'river2',
                                 town= 'town3' )

    stations = [station1, station2, station3]
    output = inconsistent_typical_range_stations(stations)
    assert type(output) == list
    assert output == ['Test 2', 'Test 3']
