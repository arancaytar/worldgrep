import sys
from common import *
import nbt

world = nbt.world.AnvilWorldFolder(sys.argv[1])
print(countBlocks(world, int(sys.argv[2])))
