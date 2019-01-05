class Station:
    def __init__(self, station_lst):
        self.station_lst = station_lst

    def get_station_name_from_id(self, id):
        """ return the name of the station from 
            its id """
        return self.station_lst[id-1].split(':', 1)[-1]