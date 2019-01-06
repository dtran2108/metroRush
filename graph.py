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
        all_path = []
        # traverse through all of the transfer point of the line
        for transferPoint in stations[line1]:
            path = [transferPoint]
            start = path[-1]
            # a boolean list to check whether the transfer point is visited
            check = [start]
            # loop until the destination line is found
            while start.split(':')[-1].strip() != line2:
                # get the name of the line
                line_name = start.split(':')[-1].strip()
                # check each transfer point in the line
                for transfer_point in stations[line_name]:
                    # if it hasn't been visited yet
                    if transfer_point not in check:
                        path.append(transfer_point)
                        # mark the visited point
                        check.append(transfer_point)
                        break
                start = path[-1]
            # get all the possible path
            all_path.append(path)
        return all_path

    def find_path_to_transfer_point(self, station, transfer_point):
        """ return the path from a station to the transfer point """
        pass
    
    def get_requirements(self):
        """ return the requirements """
        return self.requirements