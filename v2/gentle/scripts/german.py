# script for generating language model and
# decoding graph specific to German utterances

import subprocess
import sys
import os

def generate_lang(kaldi_path,proto_dir):

    # lm.arpa
    # ~/kaldi/tools/srilm/lm/bin/i686-m64/ngram-count -text corpus.txt -order 3 -limit-vocab -vocab data/dict/lexicon.txt -lm lm.arpa
    if not os.path.exists(proto_dir + '/lang'):
        os.mkdir(proto_dir + '/lang')
    cmd = [
        "./tools/srilm/lm/bin/i686-m64/ngram-count",
        "-text",
        proto_dir + "/dict/corpus.txt",
        "-order",
        "3",
        "-limit-vocab",
        "-vocab",
        proto_dir + "/dict/lexicon.txt",
        "-lm",
        proto_dir + "/lang/lm.arpa"
    ]
    prepare_lm = subprocess.check_call(
        cmd, cwd=kaldi_path, stdout=subprocess.PIPE
    )
    if not os.path.exists(proto_dir + "/lang_test"):
        os.mkdir(proto_dir + '/lang_test')
    # L.fst and other langauge files
    cmd = [
        "./utils/prepare_lang.sh",
        "--phone-symbol-table",
        proto_dir + "/dict/phones.txt",
        proto_dir + "/dict",
        '<UNK>',
        proto_dir + "/lang_test",
        proto_dir + "/lang"
    ]
    langauge_files = subprocess.check_call(cmd, cwd = kaldi_path + "/egs/gentle", stdout = subprocess.PIPE)

    # building grammar
    # gzip lm.arpa
    cmd = [
        "gzip",
        "-f",
        "lang/lm.arpa"
    ]
    grammar = subprocess.check_call(cmd, cwd = proto_dir, stdout = subprocess.PIPE)

    cmd = [
        "./utils/format_lm.sh",
        proto_dir + "/lang",
        proto_dir + "/lang/lm.arpa.gz",
        proto_dir + "/dict/lexicon.txt",
        proto_dir + "/lang/grammar" # G.fst
    ]
    grammar = subprocess.check_call(cmd, cwd = kaldi_path + '/egs/gentle', stdout = subprocess.PIPE)

    # # copying grammar to lang dir to sit with L.fst and stuff
    # cmd = [
    #     "cp",
    #     proto_dir + "/lang/grammar/*",
    #     proto_dir + "/lang"
    # ]

    # compiling HCLG.fst
    #   german/model german/
    cmd = [
        "./utils/mkgraph.sh",
        "--self-loop-scale",
        "1.0",
        proto_dir + "/lang/grammar", #G.fst
        proto_dir + "/../model",
        proto_dir + "/../model/"
    ]
    fst = subprocess.check_call(cmd,cwd = kaldi_path + '/egs/gentle', stdout = subprocess.PIPE)

def lexicon_and_phones():
    return 0

if __name__=="__main__":

    kaldi_path = sys.argv[1] # Root_kaldi/
    proto_dir = sys.argv[2] # german/data

    # generate lexicon and phones
    # assumes that you have a lexicon.txt for
    # an utterance

    # call for language model generation
    # and for fst creation
    generate_lang(kaldi_path, proto_dir)
