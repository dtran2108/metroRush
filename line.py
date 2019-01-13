class Station:
    def __init__(self, station_lst):
        self.station_lst = station_lst

    def get_stationName_from_id(self, id):
        """ return the station's name from its id """
        return self.station_lst[id-1].split(':')[1]

    def get_stationId_from_name(self, name):
        """ return the station's id from its name """
        for station in self.station_lst:
            if self.check_transfer(station) and station.split(':')[1] == name:
                return int(station.split(':')[0])
            elif station.split(':')[-1] == name:
                return int(station.split(':')[0])

    def check_transfer(self, station):
        """ check if the station has a transfer point """
        if ":Conn:" in station:
            return True

    def get_all_transfer_points(self):
        """ return all the transfer points of a line """
        return [transfer_point for transfer_point in self.station_lst\
                if self.check_transfer(transfer_point)]
