import string
import sys

phonesPath = sys.argv[1]
phonesCTM = sys.argv[2]
phones = open(phonesPath + "/phones.txt", "r+")
newPhonesCTM = open(phonesCTM + "/newPhones.ctm", "w")

with open(phonesCTM + "/phones.ctm", "r+") as ctmFile:
    for line in ctmFile.readlines():
        data = []
        count = 0
        for word in line.split():
            count += 1
            if count != 5:
                data.append(word)
            if count == 5:
                # search for word in phones
                for eachLine in phones.readlines():
                    ct = 0
                    for eachWord in eachLine.split():
                        ct += 1
                        # print(ct,eachWord,word)
                        if ct == 1:
                            text = eachWord.casefold()
                        if ct == 2 and eachWord.casefold() == word.casefold():
                            print("Found ", word.casefold(), "\n")
                            data.append(word.casefold())
                            print("List: ", data)
            # save to file
            for d in data:
                newPhonesCTM.write("%s" % d)
phones.close()
newPhonesCTM.close()
