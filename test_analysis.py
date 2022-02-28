from distutils.command.build import build
from os import times
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem import analysis
from floodsystem.datafetcher import fetch_measure_levels
from matplotlib import dates
import numpy as np 
import pytest
import datetime

stations = build_station_list()
update_water_levels(stations)

def test():
    dt = 10
    times, levels = fetch_measure_levels(stations[0].measure_id, dt = datetime.timedelta(days=dt))
    x = dates.date2num(times)

    poly, d0 = analysis.polyfit(times, levels, 2)

    assert d0 == x[0]
    assert isinstance(poly, np.poly1d)