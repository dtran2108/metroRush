from graph import Graph

class Path_finding(Graph):

    @staticmethod    
    def find_all_paths(all_stations, start_line, start_stationId, end_line, end_stationId):
        """ return all the possible paths """
        # get all the transfer points
        transfer_points = Graph.get_transfer_points(all_stations)
        # save the original requirements
        ori_start_line, ori_start_stationId = start_line, start_stationId
        ori_end_line, ori_end_stationId = end_line, end_stationId
        # get the path from start line to end line through the transfer points
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
                start_stationId = all_stations[start_line].get_stationId_from_name(\
                                  transfer_point.split(':')[1])
            # end of loop, path still lacks end station -> append it to the path
            path_to_end = Path_finding.find_station_path(start_stationId, end_stationId)
            for id in path_to_end:
                line.append('{}:{}'.format(start_line, id))
            path.append(line)
            # set the original requirements again to continue the big loop
            start_line, start_stationId  = ori_start_line, ori_start_stationId
            end_line, end_stationId = ori_end_line, ori_end_stationId
        return path
    
    def find_transfer_points(stations, line1, line2):
        """ return the transfer points have to take when 
            go from line1 to line2 """
        all_path = []
        # traverse through all of the transfer point of the line
        for transferPoint in stations[line1]:
            path = [transferPoint]
            visited = [line1]
            visited.append(transferPoint.split(':')[-1].strip())
            start = path[-1]
            # loop until the destination line is found
            while start.split(':')[-1].strip() != line2:
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
            # get all the possible path
            all_path.append(path)
        return all_path

    def find_station_path(station1_id, station2_id):
        """ return the path from station to station on the same line """
        if station1_id < station2_id:
            return [i for i in range(station1_id, station2_id+1)]
        elif station1_id > station2_id:
            return [i for i in reversed(range(station2_id, station1_id+1))]
        else:
            return [station1_id]