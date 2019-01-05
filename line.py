class Station:
    def __init__(self, station_lst):
        self.station_lst = station_lst

    def get_stationName_from_id(self, id):
        """ return the station's name from its id """
        return self.station_lst[id-1].split(':', 1)[-1]

    def get_stationId_from_name(self, name):
        """ return the station's id from its name """
        for station in self.station_lst:
            if self.check_transfer(int(station.split(':')[0])):
                if station.split(':')[1] == name:
                    return int(station.split(':')[0])
            else:
                if station.split(':')[-1] == name:
                    return int(station.split(':')[0])

    def check_transfer(self, id):
        """ check if the station has a transfer point """
        station = self.station_lst[id-1]
        if ":Conn:" in station:
            return True
        return False

    def get_transfer(self, id):
        """ return the line name the station transfers with """
        station = self.station_lst[id-1]
        if self.check_transfer(id):
            return station.split(':Conn:')[-1]