from nbt import nbt
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

x = loadBlockData(sys.argv[1])
print(printBlockData(filterBlocks(x, sys.argv[2])))
