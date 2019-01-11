class Train:
    def __init__(self, train_label, current_position):
        self.label = train_label
        self.current_position = current_position

    def check_next_position(self, path, train_lst, destination):
        """ return the next possible position """
        # get the next position
        next_position = path[path.index(self.current_position) + 1]
        occupied = False
        # check if there is any train at the next position
        for train in train_lst:
            # and the next position isn't the destination
            if train.current_position == next_position and train.label != self.label\
               and next_position != destination:
                occupied = True
        if not occupied:
            return next_position

    def move_train(self, path, train_lst, destination):
        """ move the train to the next position """
        # check for the next position
        new_position = self.check_next_position(path, train_lst, destination)
        # if there is next position found
        if new_position:
            # move the train to the next position
            self.current_position = new_position