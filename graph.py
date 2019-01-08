from line import Station
from Requirements import Requirement


class Graph:
    def __init__(self, map):
        self.map = map[0]
        self.requirements = Requirement(map[1])

    def get_all_stations(self):
        """ turn all the station into Station objects """
        station_on_line = {}
        for key in self.map.keys():
            station_on_line[key] = Station(self.map[key])
        return station_on_line

    def get_transfer_points(self):
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
        # get all the station objects
        all_stations = self.get_all_stations()
        # get all the transfer points
        transfer_points = self.get_transfer_points()
        # get the requirements
        requirements = self.get_requirements()
        start_line, start_stationId = requirements.get_start_point()
        end_line, end_stationId = requirements.get_end_point()
        # find all the transfer points have to take to go from start line to end line
        transfer_point_paths = self.find_transfer_points(transfer_points, start_line, end_line)
        path = []
        for transfer_point_path in transfer_point_paths:
            line = []
            # traverse through all the transfer points in path
            for transfer_point in transfer_point_path:
                # find the path from start station id to the id of transfer point on the same line
                line.append((start_line, self.find_station_path(start_stationId, int(transfer_point.split(':')[0]))))
                # set the new start line and start id to continue the loop
                start_line = transfer_point.split(':')[-1].strip()
                start_stationId = all_stations[start_line].get_stationId_from_name(transfer_point.split(':')[1])
            # end of loop, path still lacks end station -> append it to the path
            line.append((start_line, self.find_station_path(start_stationId, end_stationId)))
            path.append(line)
            # set the original requirements again to continue the big loop
            start_line, start_stationId = requirements.get_start_point()
            end_line, end_stationId = requirements.get_end_point()
        return path
    
    def get_requirements(self):
        """ return the requirements """
        return self.requirements