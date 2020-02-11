import os
import subprocess


# if word.ctm or output.ctm exists then copy it to output/ dir

phnDict = {}
phones = open("../exp/tri2a/phones.txt","r+")
try:
    os.remove("../output/phones.ctm")
except OSError:
    pass
finally:
    newPhone = open("../output/phones.ctm","a+")

for line in phones:
    sym, val = line.strip().split(" ")
    phnDict[val.strip()] = sym.strip()

# print(phnDict)

with open("../exp/tri2a/decode/1.ctm","r+") as ctmFile:
    for line in ctmFile.readlines():
        data = []
        count = 0
        for word in line.split():
            count += 1
            if(count != 5):
                data.append(word)
            else:
                if (word in phnDict):
#                    print("Sym: ",phnDict[word],"\n")
                    data.append(phnDict[word])
#        print(data)             
        for d in data:
            newPhone.write("%s " % d)
        newPhone.write("\n")
newPhone.close()
phones.close()
    
