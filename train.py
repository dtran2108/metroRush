class Train:
    def __init__(self, train_label, current_position):
        self.label = train_label
        self.current_position = current_position

    def __repr__(self):
        return '{}:{}'.format(self.label, self.current_position)

    def check_next_position(self, path, train_lst):
        """ return the next possible position """
        # get the next position
        next_position = path[path.index(self.current_position) + 1]
        occupied = False
        # check if there is any train at the next position
        for train in train_lst:
            if train.current_position == next_position and train.label != self.label and next_position != 'Blue Line:36':
                occupied = True
        if not occupied:
            return next_position

    def move_train(self, path, train_lst):
        """ move the train to the next position """
        new_position = self.check_next_position(path, train_lst)
        # if there is next position found
        if new_position:
            self.current_position = new_position