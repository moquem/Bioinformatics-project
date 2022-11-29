import os
import sys
from minimal_crossing import OTCM
from newick_parse import *

currentFolder = os.path.abspath(os.path.dirname(sys.argv[0]))
inputFile = os.path.join(currentFolder,'input.txt')
outputFile = os.path.join(currentFolder,'output.txt')

with open(inputFile) as fd:
   i=0
   for line in fd.readlines():
      i += 1
      if i==1:
         # read the first line which should contain a tree in the Newick format
         t = stringToNewick(line)
   fd.close()

   
   nbOfCrossings,tree = OTCM(t)

   outputFile.writelines("Best ordered dendrogram:\n"+newickToString(t)+"\n")
   outputFile.writelines("Nb of conflicts: "+str(nbOfCrossings)+"\n")