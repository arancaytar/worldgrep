import sys
from common import *

x = loadBlockData(sys.argv[1])
print(printBlockData(filterBlocks(x, sys.argv[2])))

