from directory import Directory


class Context():

    def __init__(self, root_dir):
        self.dir = Directory(root_dir)
