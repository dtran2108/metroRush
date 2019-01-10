class Train:
    def __init__(self, train_label, current_line, current_station):
        self.train_label = train_label
        self.current_line = current_line
        self.current_station = current_station

    def __repr__(self):
        return '{}: {}:{}'.format(self.train_label, self.current_line, self.current_station)

    def move_train(self, new_line, new_station):
        self.current_line = new_line
        self.current_station = new_station