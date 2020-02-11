import json
import os

def findSampleNames(textFile):
    sample_names = []
    for line in textFile.readlines():
        count = 0
        for word in line.split(" ", 1):
            # print(word)
            count += 1
            if count == 1:
                if word not in sample_names:
                    sample_names.append(word)
    return sample_names
path = '/data/shreya/kaldi/egs/recipes/voxforge_ru/transcript/text'
try:
    os.remove("meta.json")
except OSError:
    pass
finally:
    file_json = open("meta.json","w")
record = {}
all_records = []
with open(path,"r") as textFile:
    sample_names = findSampleNames(textFile)

    
for name in sample_names:
    textFile = open(path, 'r')    
    for line in textFile.readlines():
        count = 0
        flag = 0
        record = {}
        for word in line.split(" ", 1):
            
            count += 1
            if name == word:
                print("word: ", word)
                record['sample'] = word
                flag = 1
            if flag == 1 and count > 1:
                print("text: ", word)
                record['ground_truth'] = str(word)

        if bool(record) == True:
            all_records.append(record.copy())

    textFile.close()
json.dump(all_records,file_json,separators = (',',':'), indent = 2, ensure_ascii = False)
file_json.close()
                        
