import json
import os

# f = open("../score_5/transcript.ctm","r")
f = open("../newPhone.ctm","r")

data_json = {}
full_data_json = []
index = 0
try:
    # os.remove("word.json")
    os.remove("phoneme.json")
    # os.rmdir("json")
except OSError:
    pass
except FileExistsError:
    pass
finally:
    # os.mkdir("json")
    # file_json = open("word.json","w+")
    file_json = open("phoneme.json","w+")
for line in f.readlines():
    count = 0
    for word in line.split():
        count+=1
        # print(count,word)
        if (count == 1):
            data_json['utterance'] = word # utterance/speaker
            # continue
        if (count == 2):
            continue # no 
        if (count == 3):
            data_json['start'] = word #start
        if (count == 4):
            data_json['end'] = str(round(float(data_json['start']) + float(word),2)) # dur
        if (count == 5):
            data_json['text'] = word  #text 
    # print(data_json)
    index += 1
    data_json['id'] = index
    full_data_json.append(data_json.copy())
    print(full_data_json)
json.dump(full_data_json, file_json, separators = (',',':') ,ensure_ascii = False, indent = 2)
print("\n")
# print(file_json.readlines())
f.close()
file_json.close()    
    
