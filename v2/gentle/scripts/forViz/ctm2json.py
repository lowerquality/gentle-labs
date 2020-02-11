import json
import os
import sys
import shutil

import forViz.process_json as pjson


def convToJSON(keyword, proto_dir, text_file):
    f = open(proto_dir + "/decode/aligned-" + keyword + ".ctm", "r")
    data_json = {}
    full_data_json = []
    index = 0
    try:
        json_file = open(proto_dir + "/json/" + keyword + ".json", "w")
        for line in f.readlines():
            count = 0
            for word in line.split():
                count += 1
                # print(count,word)
                if count == 1:
                    data_json["utterance"] = word  # utterance/speaker
                    # continue
                if count == 2:
                    continue  # no
                if count == 3:
                    data_json["start"] = word  # start
                if count == 4:
                    data_json["end"] = str(
                        round(float(data_json["start"]) + float(word), 2)
                    )  # dur
                if count == 5:
                    data_json["text"] = word  # text
            # print(data_json)
            index += 1
            data_json["id"] = index
            full_data_json.append(data_json.copy())
            # print(full_data_json)
        json.dump(
            full_data_json,
            json_file,
            separators=(",", ":"),
            ensure_ascii=False,
            indent=2,
        )
        # print("\n")
        # print(json_file.readlines())
        f.close()
        json_file.close()

        # call process_json.py
        json_file = proto_dir + "/json/" + keyword + ".json"
        pjson.process(json_file, keyword, proto_dir + "/json")

    except Exception as error:
        print("exception: ", error)


if __name__ == "__main__":
    keyword = ["word", "phoneme"]  # <phones> or <words>
    proto_dir = sys.argv[1]  # proto_dir/decode/aligned-phones(words).ctm resides here
    text_file = sys.argv[2]  # path to transcript text file
    if os.path.exists(proto_dir + "/json"):
        pass
    else:
        os.makedirs(proto_dir + "/json")
    for key in keyword:
        convToJSON(key, proto_dir, text_file)
