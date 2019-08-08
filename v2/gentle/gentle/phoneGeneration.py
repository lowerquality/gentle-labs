import sys
import os


def generatePhones(proto_dir):

    # proto_dir = sys.argv[1]
    count = 0
    silPhones = open(proto_dir + "/dict/silence_phones.txt", "w")
    nonSilPhones = open(proto_dir + "/dict/nonsilence_phones.txt", "w")
    optionalPhones = open(proto_dir + "/dict/optional_silence.txt", "w")
    allLetters = set()
    with open(proto_dir + "/dict/lexicon.txt", "r") as lex:
        for lines in lex.readlines():
            count += 1
            words = lines.split(" ", 1)
            # print(words)
            if count < 3:
                # silence_phones.txt
                # print(words[0], " & ", words[1])
                silPhones.write(words[1])
            else:
                # # nonsilence_phones.txt
                new_words = words[1].split(" ")
                # new_words = new_words.strip("\n")
                # print(new_words)
                for letter in new_words:
                    letter = letter.strip("\n")
                    # print("*", letter, "*")
                    if letter not in allLetters:
                        allLetters.add(letter)
                    else:
                        pass
    allLetters = sorted(allLetters)
    # print(allLetters)
    for letter in allLetters:
        nonSilPhones.write(letter)
        nonSilPhones.write("\n")
    nonSilPhones.close()
    silPhones.close()
    os.chmod(proto_dir + "/dict/silence_phones.txt", 0o777)
    os.chmod(proto_dir + "/dict/nonsilence_phones.txt", 0o777)
    # optional_phones.txt with SIL
    optionalPhones.write("SIL")
    optionalPhones.write("\n")
    optionalPhones.close()
    os.chmod(proto_dir + "/dict/optional_silence.txt", 0o777)


if __name__ == "__main__":
    generatePhones(sys.argv[1])
    # sys.argv[1] provides path to proto_data directory where all input files will be stored
    # for ex: lexicon.txt, L.fst, oov.txt etc
