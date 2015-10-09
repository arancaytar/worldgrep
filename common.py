from nbt import nbt
from nbt.chunk import Chunk
import sys

def loadBlockData(worldDir):
  x = nbt.NBTFile(worldDir + '/level.dat')
  return {
	y['V'].value : y['K'].value[1:]
	for y in x['FML']['ItemData']
	if y['K'].value[0] == "\x01"
  }

def filterBlocks(blockData, keyword):
  return {a:b for a,b in blockData.items() if keyword in b}

def printBlockData(blockData):
  return "\n".join("{:5}\t{}".format(a,b) for a,b in blockData.items())

def countBlocks(worldFolder, id):
  count = 0
  for region in worldFolder.iter_regions():
    print("Searching through {}".format(region.filename))
    for chunk in region.get_metadata():
      #print("Searching through {},{}".format(chunk.x, chunk.z))
      x = Chunk(region.get_chunk(chunk.x, chunk.z))
      for i, section in zip(range(16), x.sections):
        if not section:
          continue
        for yzx, (block, add, data) in zip(range(16*16*16), section.get_all()):
          if (add << 8 | block) == id:
            count += 1
            print(count, i*16 + yzx // 256)
  return count
