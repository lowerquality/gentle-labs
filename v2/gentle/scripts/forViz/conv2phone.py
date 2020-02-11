import os
import sys

# if word.ctm or output.ctm exists then copy it to output/ dir

phnDict = {}
phones = open(
    sys.argv[1] + "/phones.txt", "r+"
)  # path to langdir where phones.txt resides
try:
    os.remove(sys.argv[2] + "/updatedPhones.ctm")
except OSError:
    pass
finally:
    newPhone = open(sys.argv[2] + "/updatedPhones.ctm", "a+")

for line in phones:
    sym, val = line.strip().split(" ")
    phnDict[val.strip()] = sym.strip()

# print(phnDict)

with open(
    sys.argv[2] + "/phones.ctm", "r+"
) as ctmFile:  # path to phones.ctm file that is generated
    for line in ctmFile.readlines():
        data = []
        count = 0
        for word in line.split():
            count += 1
            if count != 5:
                data.append(word)
            else:
                if word in phnDict:
                    #                    print("Sym: ",phnDict[word],"\n")
                    data.append(phnDict[word])
        #        print(data)
        for d in data:
            newPhone.write("%s " % d)
        newPhone.write("\n")
newPhone.close()
phones.close()
