import subprocess
import os
import sys
import shutil

# for language model generation


# arg 1: model path
# arg 2: audiofile path (.wav file)
# arg 3: transcript path (textfile containing utterance_ name <text>)
# arg 4: path to Kaldi, eg: /data/shreya/kaldi
# arg 5: output directory path

kaldiPath = sys.argv[1]
audioPath = sys.argv[2]
transcriptPath = sys.argv[3]
proto_dir = sys.argv[4]

modelPath = proto_dir + "/tdnn_7b_chain_online/graph_pp"
outputDir = proto_dir + "/feats"

# print(sys.argv[1])
print("Model Path: ", modelPath)
print("Audio Path: ", audioPath)
print("Transcript Path: ", transcriptPath)
print("Kaldi Path:", kaldiPath)
print("Output Dir: ", outputDir)
# os.chdir(model_path)
# print([i for i in os.listdir(path='.')])

# pick utterance_name from the transcript, place it in wav.scp file against the audiofile_path
# utt2spk: utterance_name <utterance_name>
# task 1: creating data dir and storing utt2spk, spk2utt and wav.scp files in there
try:
    # if os.path.exists(outputDir):
    #     shutil.rmtree(outputDir)
    # os.makedirs(outputDir, 0o777)
    # os.chmod(outputDir, 0o777)
    # # print("Directory created")

    # # create wav.scp
    # textFile = open(transcriptPath, "r")
    # wavFile = open(outputDir + "/wav.scp", "w+")
    # utt2spk = open(outputDir + "/utt2spk", "w+")

    # for line in textFile.readlines():
    #     count = 0
    #     for word in line.split():
    #         count += 1
    #         if count == 1:
    #             print(word)  # utterance_name
    #             wavFile.write(word)
    #             wavFile.write(" " + audioPath)
    #             wavFile.write("\n")
    #             utt2spk.write(word + " " + word + "\n")
    #             break
    # wavFile.close()
    # utt2spk.close()
    # os.chmod(outputDir + "/wav.scp", 0o777)
    # textFile.close()

    # # generating spk2utt using subprocess module
    # # response = subprocess.check_call(["ls", "-la"])
    # with open(outputDir + "/spk2utt", "w") as spk2utt:
    #     generateSpk2utt = subprocess.check_call(
    #         [
    #             kaldiPath + "/egs/gentle/utils/utt2spk_to_spk2utt.pl",
    #             outputDir + "/utt2spk",
    #         ],
    #         stdout=spk2utt,
    #     )

    # # # Generate language model
    # # #  call generateLM.py function with arguments or without.
    # # cmd = ['./utils/prepare_lang.sh','']
    # # langModel = subprocess.check_call(cmd, cwd = kaldiPath+'/egs/gentle/', stdout = subprocess.PIPE)

    # # task 2: calling only_decode.sh file with three arguments, exp/model_name/graph (look for graph dir, if it doesn't exist raise error), data/, exp/model_name/decode (create a decode dir)

    # cmd = [
    #     "./src/featbin/compute-mfcc-feats",
    #     "--config=" + kaldiPath + "/egs/gentle/conf/mfcc.conf",
    #     "scp,p:" + outputDir + "/wav.scp",
    #     "ark,scp:" + outputDir + "/feats.ark," + outputDir + "/feats.scp",
    # ]
    # mfcc = subprocess.check_call(cmd, cwd=kaldiPath, stdout=subprocess.PIPE)

    # cmd = [
    #     "./src/featbin/compute-cmvn-stats",
    #     "--spk2utt=ark:" + outputDir + "/spk2utt",
    #     "scp:" + outputDir + "/feats.scp",
    #     "ark,scp:" + outputDir + "/cmvn.ark," + outputDir + "/cmvn.scp",
    # ]
    # cmvnFeats = subprocess.check_call(cmd, cwd=kaldiPath, stdout=subprocess.PIPE)

    # # for this script
    # if os.path.exists(proto_dir + "/decode"):
    #     shutil.rmtree(proto_dir + "/decode")
    # os.mkdir(proto_dir + "/decode")

    # # temp for only_decode.sh
    # if os.path.exists(modelPath + "/../decode"):
    #     shutil.rmtree(modelPath + "/../decode")
    # os.mkdir(modelPath + "/../decode")

    # # cmd = ['./steps/only_decode.sh', modelPath + '/graph', outputDir, modelPath + '/decode']
    # # decode = subprocess.check_call(cmd, cwd = kaldiPath + '/egs/gentle/', shell = False, stdout = subprocess.PIPE)

    # apply-cmvn
    cmd = [
        "./src/featbin/apply-cmvn",
        "--utt2spk=ark:" + outputDir + "/utt2spk",
        "scp:" + outputDir + "/cmvn.scp",
        "scp:" + outputDir + "/feats.scp",
        "ark:" + outputDir + "/feats-cmvn.ark",
    ]
    apply_cmvn = subprocess.check_call(cmd, cwd=kaldiPath, stdout=subprocess.PIPE)

    # add-delta
    cmd = [
        "./src/featbin/add-deltas",
        "ark:" + outputDir + "/feats-cmvn.ark",
        "ark:" + outputDir + "/feats-delta.ark",
    ]
    add_deltas = subprocess.check_call(cmd, cwd=kaldiPath, stdout=subprocess.PIPE)

    # # splice-feat
    # cmd = [
    #     "./src/featbin/splice-feats",
    #     "ark:" + outputDir + "/feats-deltas.ark",
    #     "ark:" + outputDir + "/feats-splice.ark",
    # ]
    # # ./splice-feats scp:/data/shreya/kaldi/egs/recipes/voxforge_ru/transcript/feats.scp ark:/data/shreya/kaldi/egs/recipes/voxforge_ru/transcript/splice-feats.ark
    # splice_feats = subprocess.check_call(cmd, cwd=kaldiPath, stdout=subprocess.PIPE)

    # cmd = [
    #     "./src/featbin/transform-feats",
    #     modelPath + "/../final.mdl",
    #     "ark:" + outputDir + "/feats-splice.ark"
    #     "ark:" + outputDir + "/feats-transform.ark",
    # ]
    # tranform_feats = subprocess.check_call(cmd, cwd=kaldiPath, stdout=subprocess.PIPE)
    # # ./transform-feats /data/shreya/kaldi/egs/recipes/voxforge_ru/exp/tri3b/final.mat
    # # ark:/data/shreya/kaldi/egs/recipes/voxforge_ru/transcript/splice-feats.ark ark:/data/shreya/kaldi/egs/recipes/voxforge_ru/
    # # transcript/splice-transform.ark

    # ******************************LATTICE-GENERATION******************************************

    # gmm lattice generator
    cmd = [
        "./src/gmmbin/gmm-latgen-faster",
        "--max-active=7000",
        "--beam=16.0",
        "--lattice-beam=10.0",
        "--acoustic-scale=0.083333",
        "--allow-partial=true",
        "--word-symbol-table=" + modelPath + "/words.txt",
        modelPath + "/../final.mdl",
        modelPath + "/HCLG.fst",
        "ark:" + outputDir + "/feats-delta.ark",
        "ark:|gzip -c > " + proto_dir + "/decode/lat.1.gz",
        "ark,t:" + proto_dir + "/decode/words.1",
        "ark,t:" + proto_dir + "/decode/alignments.1",
    ]

    # cmd = [
    #     "./src/gmmbin/gmm-align-compiled",
    #     modelPath + "/../final.mdl",
    #     "ark:" + modelPath + "/HCLG.fst",
    #     "ark:" + outputDir + "/feats-deltas.ark",
    #     "ark,t:" + proto_dir + "/decode/alignments.1",
    # ]
    # # gmm-align-compiled 1.mdl ark:graphs.fsts scp:train.scp ark:1.ali

    latticeGen = subprocess.check_call(cmd, cwd=kaldiPath, stdout=subprocess.PIPE)

    # # phone alignments to ctm
    # cmd = [
    #     "./src/bin/ali-to-phones",
    #     "--ctm-output",
    #     modelPath + "/../final.mdl",
    #     "ark:" + proto_dir + "/decode/alignments.1",
    #     proto_dir + "/decode/phones.ctm",
    # ]
    # phnAlignments = subprocess.check_call(cmd, cwd=kaldiPath, stdout=subprocess.PIPE)

    # # word-alignment; instead of directly calling get_ctm.sh
    # # use cc functions instead
    # cmd = [
    #     "./src/latbin/lattice-1best",
    #     "--acoustic-scale=0.1",
    #     "ark: gunzip -c " + proto_dir + "/decode/lat.1.gz|",
    #     "ark:" + proto_dir + "/decode/bestLattice.lats",
    # ]
    # latticeBest = subprocess.check_call(cmd, cwd=kaldiPath, stdout=subprocess.PIPE)

    # ******************************************************************************************

    # cmd = [
    #     "./src/latbin/lattice-align-words",
    #     "--partial-word-label=4324",
    #     proto_dir + "/langdir/phones/word_boundary.int",
    #     modelPath + "/../final.mdl",
    #     "ark:" + proto_dir + "/decode/bestLattice.lats",
    #     "ark:" + proto_dir + "/decode/aligned.lats",
    # ]
    # # "--silence-label=4320",
    # # cmd = [
    # #     "./src/latbin/lattice-align-words-lexicon",
    # #     kaldiPath + "/egs/gentle/data/langdir/phones/align_lexicon.int",
    # #     modelPath + "/../final.mdl",
    # #     "ark:" + proto_dir + "/decode/bestLattice.lats",
    # #     "ark:" + proto_dir + "/decode/aligned.lats",
    # # ]
    # alignedLattice = subprocess.check_call(cmd, cwd=kaldiPath, stdout=subprocess.PIPE)

    # # lattice-align-words-lexicon $lang/phones/align_lexicon.int $model ark:- ark:- \

    # cmd = [
    #     "./src/latbin/nbest-to-ctm",
    #     "ark:" + proto_dir + "/decode/aligned.lats",
    #     proto_dir + "/decode/words.ctm",
    # ]
    # nBest = subprocess.check_call(cmd, cwd=kaldiPath, stdout=subprocess.PIPE)

    # # nbest-to-ctm --frame-shift=$frame_shift --print-silence=$print_silence ark:- - \| \
    # #   utils/int2sym.pl -f 5 $lang/words.txt \| \

    # # cmd = [
    # #     "./steps/get_ctm.sh",
    # #     outputDir,
    # #     kaldiPath + "/egs/gentle/data/langdir",
    # #     proto_dir + "/decode/",
    # # ]
    # # wordAlignments = subprocess.check_call(
    # #     cmd, cwd=kaldiPath + "/egs/gentle/", stdout=subprocess.PIPE
    # # )

except Exception as error:
    print(error)

    # You've modified the `decode.sh` script. Please package it
    # together with this file and provide a README that documents how
    # to run the decoder (ie. which files from Kaldi are needed, which
    # files from training a model are needed, and where everything
    # should be placed).
    #
    # Ideally, anyone who has the output of a similar Kaldi training
    # should be able to use this script.
    #
    # Please create a minimal zip file containing only the parts of
    # the trained model directory that you need. This should only
    # contain data (ie. files that you would find within /exp/tri*).
    #
    # Then, the instructions should cover how to decode a new audio
    # file, given:
    #
    # 1. Your code repository, with python and shell scripts. Either
    # your python code is responsible for placing the shell script in
    # the appropriate place, or you can provide documentation on where
    # the user should place it;
    #
    # 2. A pristine clone of the Kaldi repository (this contains the
    # egs/ directory with steps); and
    #
    # 3. The zipfile containing the model that you've trained.
    #
    # RM


# task 3: convert alignments.JOB file into a ctm file, word.JOB file into a ctm file

# task 4: convert alignments_integer.ctm into alignments_symbol.ctm file

# task 5: converting ctm files into json files

# task 6: linking with the visualization script. So, that it runs the viz on the browser.
