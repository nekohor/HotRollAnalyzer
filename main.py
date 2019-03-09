import sys
import os
# from multiprocessing import Pool

from context import Context
from export import Exporter

# program file dir


#  mill line tag as string
line = sys.argv[1]
#  dir definition 传入的 %cd% 即为root dir
root_dir = sys.argv[2].replace("\\", "/")
print(root_dir)
# context init
ctx = Context(root_dir)
# exporter
exporter = Exporter(ctx)


exporter.pond_export()


# if __name__ == '__main__':
# print('Parent process {}.'.format(os.getpid()))
# p = Pool(4)

# p.apply_async(exporter.pond_export, args=("pond",))
# print('Waiting for all subprocesses done...')

# p.close()
# p.join()
# print('All subprocesses done.')
