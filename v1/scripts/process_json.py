import json


sample_names = []
text = 'phoneme'
# phoneme_file = open("phoneme.json","r")
with open(text + ".json","r") as main_file:
    
    main_data = json.load(main_file)
    # print(phoneme_data)
    
    for record in main_data:

        if record['utterance'] not in sample_names:
            # print(record['utterance'])
            sample_names.append(record['utterance'])
# print("List \n")
print(sample_names)


# saving separate sample json files

for name in sample_names:
    all_records = []
    file_json = open(name + "_" +text +".json","w+")
    count = 0
    with open(text + ".json","r") as main_file:
        main_data = json.load(main_file)
        for record in main_data:
            if name == record['utterance']:
                count += 1
                record['id'] = count
                all_records.append(record.copy())
    json.dump(all_records, file_json, separators = (',',':'), indent = 2, ensure_ascii = False)
    file_json.close()
