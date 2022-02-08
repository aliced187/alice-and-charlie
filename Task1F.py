import py
from floodsystem.geo import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list
import floodsystem.datafetcher

def run():
    stations = build_station_list()
    ans = inconsistent_typical_range_stations(stations)
    print (sorted(ans))

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()