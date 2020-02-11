import subprocess
import sys
import argparse

# move contents of gentle/gentle to gentle/gentle directory
# call initialize.py
def initialize(proto_dir, model_dir, lex_dir):
    cmd = ["python3", "scripts/initialize.py", proto_dir, model_dir, lex_dir]
    initial = subprocess.check_call(cmd, cwd=proto_dir + "/../", stdout=subprocess.PIPE)
    print("cleaning done? {0}".format(initial))


def generateLM(utterance, proto_dir, kaldi_path, gentle_path):
    # call generateLM.py
    cmd = ["python3", "generateLM.py", utterance, proto_dir, kaldi_path]
    generate_lang = subprocess.check_call(
        cmd, cwd=gentle_path + "/gentle/", stdout=subprocess.PIPE
    )
    print("language model done? {0}".format(generate_lang))


def decode(kaldi_path, audio, utterance, proto_dir):
    # decoding the utterance using the customized language model
    cmd = [
        "python3",
        "scripts/automateDecoding.py",
        kaldi_path,
        audio,
        utterance,
        proto_dir,
    ]
    decoding = subprocess.check_call(
        cmd, cwd=proto_dir + "/../", stdout=subprocess.PIPE
    )
    print("decoding worked? {0}".format(decoding))


# call automateDecoding.py
if __name__ == "__main__":
    audio = sys.argv[1]  # audio file path
    utterance = sys.argv[2]  # utterance path
    kaldi_path = sys.argv[3]  # kaldi_path
    gentle_path = sys.argv[4]  # gentle_path
    proto_dir = sys.argv[5]  # proto_dir
    model_dir = sys.argv[6]  # model_dir
    lex_dir = sys.argv[7]  # lexicon.txt: main dictionary

    # cleaning up, placing models & lexicon in correct dirs
    initialize(proto_dir, model_dir, lex_dir)

    # generating HCLG.fst
    generateLM(utterance, proto_dir, kaldi_path, gentle_path)

    # decoding
    decode(kaldi_path, audio, utterance, proto_dir)
