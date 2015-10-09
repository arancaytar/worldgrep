from nbt import nbt
import sys

def blockIDs(worldDir):
  x = nbt.NBTFile(worldDir + '/level.dat')
  return {
	y['V'].value : y['K'].value[1:]
	for y in x['FML']['ItemData']
	if y['K'].value[0] == "\x01"
  }
    
print(blockIDs(sys.argv[1]))
