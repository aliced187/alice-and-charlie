# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation

def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_typical_range_consistent():

    # Create a station for higher lower range
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (22.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Create a station for higher lower range
    s2_id = "test-s2-id"
    m2_id = "test-m2-id"
    label2 = "a station"
    coord2 = (2.0, -4.0)
    trange2 = (None)
    river2 = "River Y"
    town2 = "Not My Town"
    s2 = MonitoringStation(s2_id, m2_id, label2, coord2, trange2, river2, town2)

    # Create a station for correct ranges
    s3_id = "test-s3-id"
    m3_id = "test-m3-id"
    label3 = "another station"
    coord3 = (1.5, 3.0)
    trange3 = (1.3, 3.4445)
    river3 = "River X"
    town3 = "Our Town"
    s3 = MonitoringStation(s3_id, m3_id, label3, coord3, trange3, river3, town3)


    assert s.typical_range_consistent() == False
    assert s2.typical_range_consistent() == False
    assert s3.typical_range_consistent() == True

def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_relative_water_level():

    # Create a station for higher lower range
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (22.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)7
    s.latest_level = 5.0

    # Create a station for higher lower range
    s2_id = "test-s2-id"
    m2_id = "test-m2-id"
    label2 = "a station"
    coord2 = (2.0, -4.0)
    trange2 = (None)
    river2 = "River Y"
    town2 = "Not My Town"
    s2 = MonitoringStation(s2_id, m2_id, label2, coord2, trange2, river2, town2)
    s2.latest_level = -3.0

    # Create a station for correct ranges
    s3_id = "test-s3-id"
    m3_id = "test-m3-id"
    label3 = "another station"
    coord3 = (1.5, 3.0)
    trange3 = (0.0, 5.0)
    river3 = "River X"
    town3 = "Our Town"
    s3 = MonitoringStation(s3_id, m3_id, label3, coord3, trange3, river3, town3)
    s3.latest_level = 3

    # Create a station for correct ranges
    s4_id = "test-s4-id"
    m4_id = "test-m4-id"
    label4 = "yet another station"
    coord4 = (4.5, 4.0)
    trange4 = (-2, 2)
    river4 = "River W"
    town4 = "This Town"
    s4 = MonitoringStation(s4_id, m4_id, label4, coord4, trange4, river4, town4)
    s4.latest_level = 4


    assert s.relative_water_level() == None
    assert s2.relative_water_level() == None
    assert s3.relative_water_level() == 0.6
    assert s4.relative_water_level() == 1.5