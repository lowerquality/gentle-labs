import sys
import os
import shutil
import subprocess

import phoneGeneration as phones


def filterUtterance(textFile, proto_dir):
    # extract entire utterance,
    # break words into lines,
    # create a new file utterance.txt
    utterance = open(proto_dir + "/dict/utterance.txt", "w")

    with open(textFile, "r") as text:
        count = 0
        for lines in text.readlines():
            # because first line is the name of the sample
            print(lines)
            wordSet = lines.split(" ")
            for word in wordSet:
                count += 1
                if count > 1:
                    # print(word)
                    utterance.write(word)
                    utterance.write("\n")
    utterance.close()


def generateLexicon(textFile, proto_dir, pathToOriginalLexicon):
    # lexicon related

    if os.path.exists(proto_dir + "/dict"):
        shutil.rmtree(proto_dir + "/dict")
    os.makedirs(proto_dir + "/dict", 0o777)

    filterUtterance(textFile, proto_dir)  # utterance
    utterances = open(proto_dir + "/dict/utterance.txt", "r")
    utterance = []

    for utt in utterances.read().splitlines():
        utterance.append(utt)
    utterances.close()
    # print(utterance)
    phonemes = []
    subsetLexicon = open(
        proto_dir + "/dict/lexicon.txt", "w"
    )  # lexicon.txt that will be created

    string1 = "!SIL SIL"
    subsetLexicon.write(string1)
    subsetLexicon.write("\n")
    string2 = "<UNK> SPN"
    subsetLexicon.write(string2)
    subsetLexicon.write("\n")

    for utt in utterance:
        # print([i for i in utt.casefold()])
        subsetLexicon.write(str(utt))
        with open(pathToOriginalLexicon, "r") as lexicon:  # bigger lexicon
            for lines in lexicon.readlines():
                words = lines.split(" ")
                if utt.casefold() == words[0].casefold():
                    phonemes = [i.casefold() for i in words[1:]]

                    for phn in phonemes:
                        subsetLexicon.write(" ")
                        subsetLexicon.write(phn)

    subsetLexicon.close()

    # phones related
    os.chmod(proto_dir + "/dict/lexicon.txt", 777)

    # generating phones related files: nonsilence_phones.txt etc
    phones.generatePhones(proto_dir)
