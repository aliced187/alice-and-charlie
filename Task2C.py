from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level

def run():
    stations = build_station_list()
    # Update latest level data for all stations
    update_water_levels(stations)
    N=4
    slist = stations_highest_rel_level(stations, N)
    for x in slist:
        print(*x)

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()