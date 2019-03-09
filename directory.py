import os
import sys


class Directory(object):

    def __init__(self, root_dir):
        self.program_dir = os.path.split(sys.argv[0])[0]
        self.root_dir = root_dir.replace('\\', '/')
        # 数据所在的文件夹，所有数据放在一个文件夹内
        self.data_dir = root_dir + "/" + "data"
        self.pond_dir = ""
        self.rsu_dir = ""
        self.fsu_dir = ""
        self.ssu_dir = ""
        self.process(self.data_dir)

    def process(self, data_dir):
        for parent, dirnames, filenames in os.walk(data_dir):
            for dirname in dirnames:
                dir_name = dirname.upper()
                if dir_name == "POND":
                    self.pond_dir = parent + "/" + dirname
                elif dir_name == "RSU":
                    self.rsu_dir = parent + "/" + dirname
                elif dir_name == "FSU":
                    self.fsu_dir = parent + "/" + dirname
                elif dir_name == "SSU" or dir_name == "GSM":
                    self.ssu_dir = parent + "/" + dirname

        if (self.pond_dir == "" or
                self.rsu_dir == "" or
                self.fsu_dir == "" or
                self.ssu_dir == ""):
            raise Exception("'raw data dir doesn't exist!")
