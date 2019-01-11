from line import Station
from Requirements import Requirement
from path_findingMethods import Path_finding
from train import Train


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
        transfer_point_paths = Path_finding.find_transfer_points(transfer_points, start_line, end_line)
        path = []
        for transfer_point_path in transfer_point_paths:
            line = []
            # traverse through all the transfer points in path
            for transfer_point in transfer_point_path:
                # find the path from start station id to the id of transfer point on the same line
                new_id = int(transfer_point.split(':')[0])
                path_to_new_id = Path_finding.find_station_path(start_stationId, new_id)
                for id in path_to_new_id:
                    line.append('{}:{}'.format(start_line, id)) 
                # set the new start line and start id to continue the loop
                start_line = transfer_point.split(':')[-1].strip()
                start_stationId = all_stations[start_line].get_stationId_from_name(transfer_point.split(':')[1])
            # end of loop, path still lacks end station -> append it to the path
            path_to_end = Path_finding.find_station_path(start_stationId, end_stationId)
            for id in path_to_end:
                line.append('{}:{}'.format(start_line, id))
            path.append(line)
            # set the original requirements again to continue the big loop
            start_line, start_stationId = requirements.get_start_point()
            end_line, end_stationId = requirements.get_end_point()
        return path

    def display(self, turn, train_lst, all_stations, start_line, start_stationId, end_line, end_stationId, start_position, end_position):
        print('Turn {}\n=================================================='.format(turn))
        start = [train.label for train in train_lst if train.current_position == start_position]
        reached = [train.label for train in train_lst if train.current_position == end_position]
        if start:
            start_stationName = all_stations[start_line].get_stationName_from_id(start_stationId)
            print('{}({}:{})-{}'.format(start_stationName, start_line, start_stationId, ', '.join(start)))
        for train in train_lst:
            if train.label not in start and train.label not in reached:
                current_line = train.current_position.split(':')[0]
                current_station = train.current_position.split(':')[-1]
                current_name = all_stations[current_line].get_stationName_from_id(int(current_station))
                print('{}({}:{})-{}'.format(current_name, current_line, current_station, train.label))
        if reached:
            end_stationName = all_stations[end_line].get_stationName_from_id(end_stationId)
            print('{}({}:{})-{}'.format(end_stationName, end_line, end_stationId, ', '.join(reached)))
        print()

    def run_the_trains(self):
        all_stations = self.get_all_stations()
        # get the requirements
        requirements = self.get_requirements()
        N_trains = requirements.get_train_num()
        start_line, start_stationId = requirements.get_start_point()
        start_position = '{}:{}'.format(start_line, start_stationId)
        end_line, end_stationId = requirements.get_end_point()
        end_position = '{}:{}'.format(end_line, end_stationId)
        # get the path according to start and end requirements
        path = self.find_all_paths()[1]
        train_lst = [Train('T{}'.format(i), '{}:{}'.format(start_line, start_stationId))\
                     for i in range(1, int(N_trains)+1)]
        turn = 1
        while train_lst[-1].current_position != end_position:
            for train in train_lst:
                if train.current_position != end_position:
                    train.move_train(path, train_lst)
            self.display(turn, train_lst, all_stations, start_line, start_stationId, end_line, end_stationId, start_position, end_position)
            turn += 1
        print('path: {}\n'.format(path))
        return train_lst    

    def get_requirements(self):
        """ return the requirements """
        return self.requirements