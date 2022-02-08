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


    assert test_typical_range_consistent(s) == False
    assert test_typical_range_consistent(s2) == False
    assert test_typical_range_consistent(s3) == True
