import string

phones = open("../phones.txt","r+")
newPhonesCTM = open("../newPhones.ctm","w+") 

with open("../phones_dup.ctm","r+") as ctmFile:
    for line in ctmFile.readlines():
        data = []
        count = 0
        for word in line.split():
            count += 1
            if (count != 5):
                data.append(word)   
            if (count == 5):
                # search for word in phones
                for eachLine in phones.readlines():
                    ct = 0
                    for eachWord in eachLine.split():
                        ct += 1
                        # print(ct,eachWord,word)
                        if (ct == 1):
                            text = eachWord
                        if (ct == 2 and eachWord == word):
                            print("Found ",text,"\n")
                            data.append(word)
            print("List: ",data)
                            #save to file
                            #for d in data:
                             #   newPhonesCTM.write("%s"d)
phones.close()
newPhonesCTM.close()
        
