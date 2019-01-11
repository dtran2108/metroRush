class Path_finding:
    
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