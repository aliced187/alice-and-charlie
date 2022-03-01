from re import I
from floodsystem.utils import sorted_by_key  # noqa

from haversine import haversine
import floodsystem.datafetcher
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level

def test_stations_level_over_threshold():
     #Create test station list 
    station1 = MonitoringStation(station_id= 'stn_id_1',
                                 measure_id= 'measure_id_1',
                                 label= 'Test 1',
                                 coord= (0.0, 1.0),
                                 typical_range= (0.0, 1.0),
                                 river= 'river1',
                                 town= 'town1')

    station2 = MonitoringStation(station_id= 'stn_id_2',
                                 measure_id= 'measure_id_2',
                                 label= 'Test 2',
                                 coord= (1.0, 1.0),
                                 typical_range= (5.0, 1.0),
                                 river= 'river2',
                                 town= 'town2')
                                 
    station3 = MonitoringStation(station_id= 'stn_id_3',
                                 measure_id= 'measure_id_3',
                                 label= 'Test 3',
                                 coord= (100.0, 100.0),
                                 typical_range= (None),
                                 river= 'river2',
                                 town= 'town3')
    station4 = MonitoringStation(station_id= 'stn_id_4',
                                 measure_id= 'measure_id_4',
                                 label= 'Test 4',
                                 coord= (0.0, 1.0),
                                 typical_range= (0.0, 3.0),
                                 river= 'river4',
                                 town= 'town4')
    station5 = MonitoringStation(station_id= 'stn_id_5',
                                 measure_id= 'measure_id_5',
                                 label= 'Test 5',
                                 coord= (0.0, 1.0),
                                 typical_range= (0.0, 6.0),
                                 river= 'river5',
                                 town= 'town5')
                                 

    stations = [station1, station2, station3, station4, station5]
    station1.latest_level = 1.5 
    station2.latest_level = 3
    station3.latest_level = 4.8
    station4.latest_level = 1.5 
    station5.latest_level = -2.0
    tol = 0.2
    output = stations_level_over_threshold(stations, tol)
    assert type(output) == list
    assert output == [('Test 1', 1.5), ('Test 4', 0.5)]

def test_stations_highest_rel_level():
     #Create test station list 
    station1 = MonitoringStation(station_id= 'stn_id_1',
                                 measure_id= 'measure_id_1',
                                 label= 'Test 1',
                                 coord= (0.0, 1.0),
                                 typical_range= (0.0, 1.0),
                                 river= 'river1',
                                 town= 'town1')

    station2 = MonitoringStation(station_id= 'stn_id_2',
                                 measure_id= 'measure_id_2',
                                 label= 'Test 2',
                                 coord= (1.0, 1.0),
                                 typical_range= (5.0, 1.0),
                                 river= 'river2',
                                 town= 'town2')
                                 
    station3 = MonitoringStation(station_id= 'stn_id_3',
                                 measure_id= 'measure_id_3',
                                 label= 'Test 3',
                                 coord= (100.0, 100.0),
                                 typical_range= (None),
                                 river= 'river2',
                                 town= 'town3')
    station4 = MonitoringStation(station_id= 'stn_id_4',
                                 measure_id= 'measure_id_4',
                                 label= 'Test 4',
                                 coord= (0.0, 1.0),
                                 typical_range= (0.0, 4.0),
                                 river= 'river4',
                                 town= 'town4')
    station5 = MonitoringStation(station_id= 'stn_id_5',
                                 measure_id= 'measure_id_5',
                                 label= 'Test 5',
                                 coord= (0.0, 1.0),
                                 typical_range= (0.0, 6.0),
                                 river= 'river5',
                                 town= 'town5' )
    
    N = 2
    stations = [station1, station2, station3, station4, station5]
    station1.latest_level = 1.7
    station2.latest_level = 3.0
    station3.latest_level = 4.8
    station4.latest_level = 2.0
    station5.latest_level = 1.2
    output = stations_highest_rel_level(stations, N)
    assert type(output) == list
    assert output == [('Test 1', 1.7), ('Test 4', 0.5)]