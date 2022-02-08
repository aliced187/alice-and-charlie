import py
from floodsystem.geo import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list
import floodsystem.datafetcher

#Demonstation to build a list of station names, in alphabetical order, for stations with inconsistent data
def run():
    stations = build_station_list()
    ans = inconsistent_typical_range_stations(stations)
    print (sorted(ans))

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()