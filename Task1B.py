from turtle import st
import py
from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
import floodsystem.datafetcher



def run():
    stations = build_station_list()
    p = (52.2053, 0.1218)

    x = stations_by_distance(stations, p)
    print(x[:10])
    print(x[-10:])

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()

    
