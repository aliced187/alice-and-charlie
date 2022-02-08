import py
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
import floodsystem.datafetcher
from floodsystem.geo import rivers_by_station_number

#Demonstration that prints the list of (river, number stations) tuples when N = 9.

def run():
    stations = build_station_list()
    N = 9
    return print(rivers_by_station_number(stations, N))

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()