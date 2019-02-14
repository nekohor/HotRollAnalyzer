import os


class Directory(object):

    def __init__(self, data_dir):
        self.pond_dir = ""
        self.rsu_dir = ""
        self.fsu_dir = ""
        self.ssu_dir = ""
        self.process(data_dir)

    def process(self, data_dir):
        for parent, dirnames, filenames in os.walk(data_dir):
            for dirname in dirnames:
                if dirname.upper() == "POND":
                    self.pond_dir = os.path.join(parent, dirname)
                elif dirname.upper() == "RSU":
                    self.rsu_dir = os.path.join(parent, dirname)
                elif dirname.upper() == "FSU":
                    self.fsu_dir = os.path.join(parent, dirname)
                elif dirname.upper() == "SSU" or dirname.upper() == "GSM":
                    self.ssu_dir = os.path.join(parent, dirname)

        if (self.pond_dir == "" or
                self.rsu_dir == "" or
                self.fsu_dir == "" or
                self.ssu_dir == ""):
            print("'!!!!!!!!!!!!!!raw data doesn't exist!!!!!!!!!!!!!!")
