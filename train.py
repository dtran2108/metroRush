class Train:
    def __init__(self, train_label, current_line, current_station):
        self.train_label = train_label
        self.current_line = current_line
        self.current_station = current_station

    def __repr__(self):
        return '{}:{}:{}'.format(self.train_label, self.current_line, self.current_station)

    def move_train(self, new_line, new_station):
        self.current_line = new_line
        self.current_station = new_station

    def find_path(self, train_lst, path):
        end_line = path[-1].split(':')[0]
        end_station = path[-1].split(':')[1]
        try:
            next_position = path[path.index('{}:{}'.format(self.current_line, self.current_station))+1]
        except IndexError:
            # next_position = '{}:{}'.format(self.current_line, self.current_station)
        next_line = next_position.split(':')[0]
        next_station = next_position.split(':')[1]
        occupied = False
        if self.current_line != end_line and self.current_station != end_station:    
            for train in train_lst:
                if train.current_line == next_line and train.current_station == next_station:
                    occupied = True
        if not occupied:
            self.move_train(next_line, next_station)            