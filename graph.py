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

    def lamgido(self):
        stations = self.get_all_stations()
        for line in stations.keys():
            stations[line] = stations[line].get_all_transfer_points()
        return stations

    @staticmethod
    def find_transfer_points(stations, line1, line2):
        """ return the transfer points have to take when 
            go from line1 to line2 """
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

    @staticmethod
    def find_station_path(station1_id, station2_id):
        """ return the path from station to station on the same line """
        path = []
        if station1_id < station2_id:
            for i in range(station1_id, station2_id+1):
                path.append(i)
        elif station1_id > station2_id:
            for i in reversed(range(station2_id, station1_id+1)):
                path.append(i)
        else:
            return [station1_id]
        return path

    def find_all_paths(self):
        """ return all the possible paths """
        path = []
        stations = self.lamgido()
        # get the requirements
        requirements = self.get_requirements()
        start_line, start_station = requirements.get_start_point()
        end_line, end_station = requirements.get_end_point()
        # get the transfer points have to take when go from start line to end line
        transfer_paths = self.find_transfer_points(stations, start_line, end_line)
        transfer_path = transfer_paths[0]
        path_in_line = {}
        for transfer_point in transfer_path:
            path_in_line[start_line] = self.find_station_path(start_station, int(transfer_point.split(':')[0]))
            start_station = int(transfer_point.split(':')[0])
            start_line = transfer_point.split(':')[-1].strip()
        path_in_line[start_line] = self.find_station_path(start_station, end_station)
        path.append(path_in_line)
        return path
    
    def get_requirements(self):
        """ return the requirements """
        return self.requirements