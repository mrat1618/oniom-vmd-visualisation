#! /usr/bin/env python3

import os, sys
sys.path.append(os.getcwd()+"/../")
import utils.GaussianParser as gp 

com = gp.Gaussian('case1.com')

print("keywords:", com._keywords)
print("title:", com._tittle)
print("spin and multiplicity:", com._spinMulti)
print("coordinates:", com._coordinates)
print("footer:", com._footer)
#print("input file:", com._inpuFile)
print("blank lines:", com._blanklines)
