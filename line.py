class Line:
    def __init__(self, lines_lst):
        self.line_name = lines_lst[0]
        self.stations = lines_lst[1:]

    def get_line_name(self):
        """ return the name of the line """
        return self.line_name

    def get_all_stations(self):
        """ return all of the stations of the line """
        return self.stations