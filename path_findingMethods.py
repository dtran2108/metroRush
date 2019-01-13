from graph import Graph

class Path_finding(Graph):

    @staticmethod
    def get_full_path(all_stations, path, result, line_name):
        """ return the full path in the form <line_name>:<stationId> """
        for id in path:
            stationName = all_stations[line_name].get_stationName(id)
            result.append('{}:{}'.format(line_name, stationName))
        return result

    @staticmethod
    def get_path(all_stations, line, id, new_id, start_line):
        path_to_new_id = Path_finding.find_station_path(id, new_id)
        line = Path_finding.get_full_path(all_stations, path_to_new_id,
                                          line, start_line)
        return line

    @staticmethod
    def parse_position(position):
        """ return line name and station id """
        return position[0], int(position[1])

    @staticmethod
    def find_all_paths(all_stations, start_position, end_position):
        """ return all the possible paths """
        transfer_points = Graph.get_transfer_points(all_stations)
        # save the original start point and end point
        ori_start_line, ori_start_stationId = Path_finding.parse_position(start_position)
        ori_end_line, ori_end_stationId = Path_finding.parse_position(end_position)
        start_line, start_stationId  = ori_start_line, ori_start_stationId
        end_line, end_stationId = ori_end_line, ori_end_stationId
        transfer_point_paths = Path_finding.find_transfer_points(
                               transfer_points, start_line, end_line)
        path = []
        for transfer_point_path in transfer_point_paths:
            line = []
            for transfer_point in transfer_point_path:
                """ find the path from start station id to the id of
                    transfer point on the same line """
                new_id = int(transfer_point.split(':')[0])
                line = Path_finding.get_path(all_stations, line,\
                        start_stationId, new_id, start_line)
                start_line = transfer_point.split(':')[-1].strip()
                start_stationId = all_stations[start_line].get_stationId(transfer_point.split(':')[1])
            line = Path_finding.get_path(all_stations, line, start_stationId, end_stationId, start_line)
            path.append(line)
            start_line, start_stationId  = ori_start_line, ori_start_stationId
            end_line, end_stationId = ori_end_line, ori_end_stationId
        return path

    @staticmethod
    def path_to_destination(stations, start, end_line):
        while start.split(':')[-1].strip() != end_line:
            # get the name of the line
            line_name = start.split(':')[-1].strip()
            # check each transfer point in the line
            for transfer_point in stations[line_name]:
                # if it hasn't been visited yet
                if transfer_point.split(':')[-1].strip() not in visited:
                    path.append(transfer_point)
                    visited.append(transfer_point.split(':')[-1].strip())
                    break
            start = path[-1]

    @staticmethod
    def find_transfer_points(stations, line1, line2):
        """ return the transfer points have to take when
            go from line1 to line2 """
        global path, visited
        all_path = []
        for transferPoint in stations[line1]:
            path = [transferPoint]
            visited = [line1]
            visited.append(transferPoint.split(':')[-1].strip())
            start = path[-1]
            Path_finding.path_to_destination(stations, start, line2)
            all_path.append(path)
        return all_path

    @staticmethod
    def find_station_path(station1_id, station2_id):
        """ return the path from station to station on the same line """
        if station1_id < station2_id:
            return [i for i in range(station1_id, station2_id+1)]
        elif station1_id > station2_id:
            return [i for i in reversed(range(station2_id, station1_id+1))]
        else:
            return [station1_id]
