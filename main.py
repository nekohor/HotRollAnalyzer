import sys
import os

from context import Context


#  mill line tag as string
line = sys.argv[1]

# dir definition
root_dir = sys.argv[2].replace("\\", "/")
data_dir = os.path.join(root_dir, "data")

ctx = Context(data_dir)
