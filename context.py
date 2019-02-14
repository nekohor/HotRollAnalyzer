from directory import Directory


class Context():

    def __init__(self, data_dir):
        self.dir = Directory(data_dir)
