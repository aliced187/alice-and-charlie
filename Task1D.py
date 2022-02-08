
import py
from floodsystem.geo import stations_by_distance, stations_by_river
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
import floodsystem.datafetcher
from floodsystem.geo import stations_within_radius
from floodsystem.geo import rivers_with_stations 




def run():
    stations = build_station_list()
    x = rivers_with_stations(stations)
    
    return print(len(x), 'stations, First 10:', x[:10])


#Testing second part of Task 1D
def part_b():
    stations = build_station_list()
    x = stations_by_river(stations)
   
    return print('River Aire:', sorted((x)['River Aire'])), print('River Cam:', sorted((x)['River Cam'])), print('River Thames:', sorted((x)['River Thames']))
    

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
    part_b()