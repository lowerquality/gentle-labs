import json
import os
import sys
import shutil

# what does this script do?


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


def wavDir(audio_path, proto_dir):
    if os.path.exists(proto_dir + "/wav"):
        shutil.rmtree(proto_dir + "/wav")
    os.makedirs(proto_dir + "/wav")
    shutil.copy2(audio_path, proto_dir + "/wav/")


def create_meta(text_path, audio_path, proto_dir):

    # creating proto_dir/wav and copying content to it
    wavDir(audio_path, proto_dir)

    try:
        os.remove(proto_dir + "/json/meta.json")
    except OSError:
        pass
    finally:
        file_json = open(proto_dir + "/json/meta.json", "w")
    record = {}
    all_records = []
    with open(text_path, "r") as textFile:
        sample_names = findSampleNames(textFile)

    print("sample name: ", sample_names)
    for name in sample_names:
        textFile = open(text_path, "r")
        for line in textFile.readlines():
            count = 0
            flag = 0
            record = {}
            for word in line.split(" ", 1):

                count += 1
                if name == word:
                    print("word: ", word)
                    record["sample"] = word
                    flag = 1
                if flag == 1 and count > 1:
                    print("text: ", word)
                    record["ground_truth"] = str(word)

            if bool(record) is True:
                all_records.append(record.copy())

        textFile.close()
    json.dump(
        all_records, file_json, separators=(",", ":"), indent=2, ensure_ascii=False
    )
    file_json.close()


if __name__ == "__main__":
    text_path = sys.argv[1]  # path to text transcription file (ground truth)
    proto_dir = sys.argv[2]  # proto_dir/json/; location where to save .json file
    # path to the audio file; ex: proto_dir/../initial/sample_1.wav
    audioPath = sys.argv[3]

    # generate meta.json and create proto_dir/wav
    create_meta(text_path, audioPath, proto_dir)
