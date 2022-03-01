
def stations_level_over_threshold(stations, tol):
    names = []
    ranges = []
    waterlevels = []
    relwaterlevels = []
    for station in stations:
        names.append(station.name)
        waterlevels.append(station.latest_level)
        ranges.append(station.typical_range)
    for z in range(len(ranges)):
        if ranges[z] == None:
            pass
        else:
            value = ranges[z][1] - ranges[z][0]
            if value < 0:
                pass
            elif waterlevels[z] == None:
                pass
            else:
                relwl = (waterlevels[z]- ranges[z][0]) / (ranges[z][1] - ranges[z][0])
                if relwl > tol:
                    relwat = (names[z], relwl)
                    relwaterlevels.append(relwat)
                else:
                    pass
    return sorted(relwaterlevels, key=lambda x: -x[1])