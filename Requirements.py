class Requirement:
    def __init__(self, requirements):
        self.start_point = requirements['START']
        self.end_point = requirements['END']
        self.train_num = int(requirements['TRAINS'])