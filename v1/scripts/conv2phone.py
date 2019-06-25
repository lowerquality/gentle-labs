import os


phnDict = {}

phones = open("../phones.txt","r+")
try:
    os.remove("../newPhone.ctm")
except OSError:
    pass
finally:
    newPhone = open("../newPhone.ctm","a+")

for line in phones:
    sym, val = line.strip().split(" ")
    phnDict[val.strip()] = sym.strip()

# print(phnDict)

with open("../phones_dup.ctm","r+") as ctmFile:
    for line in ctmFile.readlines():
        data = []
        count = 0
        for word in line.split():
            count += 1
            if(count != 5):
                data.append(word)
            else:
                if (word in phnDict):
                    print("Sym: ",phnDict[word],"\n")
                    data.append(phnDict[word])
        print(data)             
        for d in data:
            newPhone.write("%s " % d)
        newPhone.write("\n")
newPhone.close()
phones.close()
    
