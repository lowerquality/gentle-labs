import json
import sys


def process(textFile, type, outputPath):
    sample_names = []
    # phoneme_file = open("phoneme.json","r")
    with open(textFile, "r") as main_file:

        main_data = json.load(main_file)
        # print(phoneme_data)

        for record in main_data:

            if record["utterance"] not in sample_names:
                # print(record['utterance'])
                sample_names.append(record["utterance"])
    # print("List \n")
    print(sample_names)

    # saving separate sample json files
    for name in sample_names:
        all_records = []
        file_json = open(outputPath + "/" + name + "_" + type + ".json", "w+")
        count = 0
        with open(textFile, "r") as main_file:
            main_data = json.load(main_file)
            for record in main_data:
                if name == record["utterance"]:
                    count += 1
                    record["id"] = count
                    all_records.append(record.copy())
        json.dump(
            all_records, file_json, separators=(",", ":"), indent=2, ensure_ascii=False
        )
        file_json.close()


if __name__ == "__main__":
    textFile = sys.argv[1]  # json filename
    type = sys.argv[2]  # phoneme or word
    outputPath = sys.argv[3]  # proto_dir/json/
    process(textFile, type, outputPath)
