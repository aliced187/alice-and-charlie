# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d
    
    def typical_range_consistent(self):
        if self.typical_range == None:
            return False
        #If a value of the range is provided as None (none available), it will return False to show a inconsistant dataset
        else:
            value = self.typical_range[1] - self.latest_level[0]
            if value >= 0:
                return True
                #If the range is positive (higher val is larger than lower val), it will return True for a consistant data set as we know all ranges are provided.
            else:
                return False
                #If the range is negative (higher val is smaller than lower val (inconsistant data)), it will return False to show a inconsistant dataset

    def relative_water_level(self):
        #retrieves typical range and checks if it is consistant, if not, return None
        rrange = typical_range_consistent(self)
        if rrange == False:
            return None
        #if typical range is consistant, returns relative water level
        else:
            relwlev = (self.latest_level - self.latest_level[0]) / rrange[x]
            return relwlev