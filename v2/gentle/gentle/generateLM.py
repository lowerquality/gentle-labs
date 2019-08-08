import gentle.language_model as lm
import gentle.metasentence as ms
import gentle.createLexicon as lx
import gentle.prepare_lang as lang

import subprocess
import shutil
import os
import sys


# createLexicon() -> creates a subset of the lexicon or calls g2p
# prepare_lang.sh -> takes argument1: data/dict[lexicon, phones], argument2: data/temp_lang, argument3: data/lang


if __name__ == "__main__":
    # print(lm("Hello World!".split(" "), '/Users/shreya/Documents/GitHub/gentle/protoDir/'))

    # path to the textfile containing the utterance is in sys.argv[1]
    text = sys.argv[1]
    # proto_langdir is sys.argv[2]
    # - it must contain
    proto_dir = sys.argv[2]
    # # path to original/exhaustive lexicon path is sys.argv[3] ex: originalLex/lexicon.txt
    # lexicon = sys.argv[3]
    # sys.argv[4]: path to a pristine copy of kaldi_root (pre-compiled)
    kaldi_path = sys.argv[3]

    # Creating lexicon, phones, L.fst etc: inputs for generating HCLG.fst
    lx.generateLexicon(text, proto_dir)

    # call prepare_language.sh c functions here
    lang.create_fst(kaldi_path, proto_dir)

    # Generating HCLG.fst (using Gentle here)
    txt_in = open(text).read()

    vocab_in = ms.load_vocabulary(
        open(proto_dir + "/tdnn_7b_chain_online/graph_pp/words.txt")
    )

    print("My Vocab", vocab_in)

    source_words_list = txt_in.split(" ")[1:]

    # We must supply a version of `words_in` that only has words within our vocabulary (ie. proto_langdir/words.txt)
    new_wdlist = []
    for wd in source_words_list:
        if wd not in vocab_in:
            new_wdlist.append(lm.OOV_TERM)
        else:
            new_wdlist.append(wd)

    print("Supplying these words", new_wdlist)

    HCLGFile = lm.make_bigram_language_model([new_wdlist], proto_dir)
    print(HCLGFile)

    # saving HCLG.fst in proto_langdir
    # renaming temp_HCLG.fst to HCLG.fst
    # storing it in proto_langdir (argv[2])
    shutil.move(HCLGFile, proto_dir + "/tdnn_7b_chain_online/graph_pp/HCLG.fst")

