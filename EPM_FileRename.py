#!/usr/bin/python3.5

import os
import sys

def main(argv):
	if len(argv) != 3:
		if len(argv) < 2:
			print ("Command inputting error! Please input 'EPM_FileRename.py --h' for help.")
		elif argv[1] != "--h":
			print ("Command inputting error! Please input 'EPM_FileRename.py --h' for help.")
		elif argv[1] == "--h":
			print ("Usage: Rename_Mark2.py [argv1] [argv2]")
			print ("    [argv1] -- Series EPM file Folder Path.")
			print ("    [argv2] -- New file name.")
	else:
		path = argv[1]
		FileName = os.listdir(path)
		NumofRenamefile = 0
		for i in range(len(FileName)):
			subPath = str(path) + str(FileName[i])
			if os.path.isdir(subPath):
				subPathFlName = os.listdir(subPath)
				for j in range(len(subPathFlName)):
					if str(subPathFlName[j])[-4:] == "emp4":
						ClipFlname = str(subPathFlName[j])[:20] + str(argv[2]) + ".emp4"
						OldPath = subPath + "/" + str(subPathFlName[j])
						NewPath = subPath + "/" + str(ClipFlname)
						os.rename(OldPath, NewPath)
					NewClipFolder = str(FileName[i])[:20] + str(argv[2]) + str(FileName[i])[-5:]
					print (NewClipFolder)
					print (path)
					NewsubPath = str(path) + NewClipFolder
				NumofRenamefile = NumofRenamefile + 1
				os.rename(subPath , NewsubPath)
		print("%d files has been renamed. Total files: %d"%(NumofRenamefile, len(FileName)))

if __name__ == "__main__":
	main(sys.argv)
