from line import Station
from Requirements import Requirement
from train import Train
from time import sleep


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

    @staticmethod
    def get_transfer_points(stations):
        """ get all the transfer points of all the lines """
        transfer_point = {}
        for line in stations.keys():
            transfer_point[line] = stations[line].get_all_transfer_points()
        return transfer_point

    def print_result(self, stationName, line, stationId, trainLabel):
        """ print the result """
        print('{}({}:{})-{}'.format(stationName, line, stationId, trainLabel))
    
    def check_and_print(self, lst, all_stations, line, station_id):
        """ check if the list is not empty and print the results """
        if lst:
            stationName = all_stations[line].get_stationName_from_id(station_id)
            self.print_result(stationName, line, station_id, ', '.join(lst))
    
    def print_train_location(self, trains, start, end, stations):
        """ print all the trains' locations """
        for train in trains:
            if train.label not in start and train.label not in end:
                current_line = train.current_position.split(':')[0]
                current_station = int(train.current_position.split(':')[-1])
                current_name = stations[current_line].get_stationName_from_id(current_station)
                self.print_result(current_name, current_line, current_station, train.label)
    
    def position_parse(self, position):
        """ get the line name and station Id 
            of a position """
        position = position.split(':')
        return position[0], int(position[1])

    def get_trains(self, trains, point):
        """ get all the trains which is at a point """
        return [train.label for train in trains if train.current_position == point]

    def display(self, turn, train_lst, all_stations, start_position, end_position):
        """ display the trains' location at each turn """
        print('Turn {}\n'.format(turn))
        # get start position
        start_line, start_stationId = self.position_parse(start_position)
        # get end position
        end_line, end_stationId = self.position_parse(end_position)
        # get all the train which is at the start point
        start = self.get_trains(train_lst, start_position)
        # get all the train which is at the destination
        reached = self.get_trains(train_lst, end_position)
        # if there are trains at the start point
        self.check_and_print(start, all_stations, start_line, start_stationId)
        # print all the trains' locations
        self.print_train_location(train_lst, start, reached, all_stations)
        # if there are trains at the end point
        self.check_and_print(reached, all_stations, end_line, end_stationId)
        print('-'*70)
    
    def move_trains(self, trains, path, endPoint):
        """ check valid move and move each train in the train list """
        for train in trains:
            # if the train hasn't reached the destination yet
            if train.current_position != endPoint:
                train.move(path, trains, endPoint)

    def run_the_trains(self):
        """ run the trains """
        all_stations = self.get_all_stations()
        # get all the requirements
        N_trains = self.requirements.train_num
        start_position = self.requirements.start_point
        end_position = self.requirements.end_point
        # get the path according to start and end requirements
        from path_findingMethods import Path_finding
        path = Path_finding.find_all_paths(all_stations, start_position, end_position)[1]
        # turn all the trains into Train objects
        train_lst = [Train(str(i), start_position) for i in range(1, N_trains+1)]
        turn = 1
        # while the last train hasn't reached the destination yet
        while train_lst[-1].current_position != end_position:
            # move each train in the train list
            self.move_trains(train_lst, path, end_position)
            # display the train at each turn
            self.display(turn, train_lst, all_stations, start_position, end_position)
            sleep(0.1)
            turn += 1