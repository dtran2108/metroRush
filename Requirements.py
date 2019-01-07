class Requirement:
    def __init__(self, requirements):
        self.start_point = requirements['START']
        self.end_point = requirements['END']
        self.train_num = requirements['TRAINS']
    
    def get_start_point(self):
        """ return the start line name and the station's id """
        startPoint = self.start_point.split(':')
        return startPoint[0], int(startPoint[-1])

    def get_end_point(self):
        """ return the end line name and the station's id """
        endPoint = self.end_point.split(':')
        return endPoint[0], int(endPoint[-1])

    def get_train_num(self):
        """ return number of trains """
        return self.train_num