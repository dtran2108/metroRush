class Requirement:
    def __init__(self, requirements):
        self.start_point = requirements['START']
        self.end_point = requirements['END']
        self.train_num = int(requirements['TRAINS'])

    def get_start_point(self):
        """ get the start point """
        start_position = self.start_point
        start_line = start_position.split(':')[0]
        start_stationId = int(start_position.split(':')[1])
        return start_position, start_line, start_stationId

    def get_end_point(self):
        """ get the end point """
        end_position = self.end_point
        end_line = end_position.split(':')[0]
        end_stationId = int(end_position.split(':')[1])
        return end_position, end_line, end_stationId