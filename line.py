class Station:
    def __init__(self, station_lst):
        self.station_lst = station_lst

    def get_station_name_from_id(self, id):
        """ return the name of the station from 
            its id """
        return self.station_lst[id-1].split(':', 1)[-1]

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