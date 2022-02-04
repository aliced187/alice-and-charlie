
import py
from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
import floodsystem.datafetcher


#Demonstration program printing list of 10 closest and 10 furthest stations



def run():

    stations = build_station_list()
    p = (52.2053, 0.1218)

    x = stations_by_distance(stations, p)
    print(x[:10])
    print(x[-10:])

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()

    
