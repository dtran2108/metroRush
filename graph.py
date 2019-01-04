class Graph:
    def __init__(self, map):
        self.map = map[0]
        self.requirements = Requirement(map[1])

    def __repr__(self):
        return str(self.map)
    
    def get_requirements(self):
        return self.requirements.get_end_point()


class Line:
    def __init__(self, lines_lst):
        pass


class Requirement:
    def __init__(self, requirement_lst):
        self.start_point = requirement_lst[0]['START']
        self.end_point = requirement_lst[1]['END']
        self.train_num = requirement_lst[2]['TRAINS']
    
    def get_start_point(self):
        """ return the start station """
        return self.start_point

    def get_end_point(self):
        """ return the end station """
        return self.end_point

    def get_train_num(self):
        """ return number of trains """
        return self.train_num