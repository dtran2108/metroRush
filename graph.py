from line import Station
from Requirements import Requirement


class Graph:
    def __init__(self, map):
        self.map = map[0]
        self.requirements = Requirement(map[1])

    def get_all_stations(self):
        """ turn all the station into Station objects """
        for key in self.map.keys():
            self.map[key] = Station(self.map[key])
        return self.map

    def find_transfer_points(self, line1, line2):
        """ return the transfer points have to take when 
            go from line1 to line2 """
        stations = self.get_all_stations()
        for line in stations.keys():
            stations[line] = stations[line].get_all_transfer_points()
        print(stations)
        pass

    def find_path_to_transfer_point(self, station, transfer_point):
        """ return the path from a station to the transfer point """
        pass
    
    def get_requirements(self):
        """ return the requirements """
        return self.requirements