from distutils.command.build import build
import py
from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
import floodsystem.datafetcher
from floodsystem.geo import stations_within_radius

#Demonstration program, list of stations within 10km of centre
def run_C():
    stations = build_station_list()

    centre = (52.2053, 0.1218)
    r = 10 
    output = stations_within_radius(stations, centre, r)
    
    return print(sorted(output))

    

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run_C()
    