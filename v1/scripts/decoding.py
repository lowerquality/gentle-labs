import subprocess
import os
import sys
import shutil

# arg 1: model path
# arg 2: audiofile path (.wav file)
# arg 3: transcript path (textfile containing utterance_ name <text>)
# arg 4: output directory path
modelPath = sys.argv[1]
audioPath = sys.argv[2]
transcriptPath = sys.argv[3]
outputDir = sys.argv[4]

# print(sys.argv[1])
print("Model Path: ",modelPath)
print("Audio Path: ",audioPath)
print("transcriptPath: ",transcriptPath)
print("Output Dir: ", outputDir)
#os.chdir(model_path)
# print([i for i in os.listdir(path='.')])

# pick utterance_name from the transcript, place it in wav.scp file against the audiofile_path
# utt2spk: utterance_name <utterance_name>
# task 1: creating data dir and storing utt2spk, spk2utt and wav.scp files in there
try:
    if os.path.exists(outputDir):
        shutil.rmtree(outputDir)
    os.makedirs(outputDir,0o777)
    os.chmod(outputDir, 0o777)
    # print("Directory created");

    # create wav.scp
    textFile = open(transcriptPath, 'r')
    wavFile = open(outputDir + '/wav.scp','w+')
    utt2spk = open(outputDir + '/utt2spk', 'w+')

    for line in textFile.readlines():
        count = 0;
        for word in line.split():
            count += 1
            if count == 1:
                print(word) # utterance_name
                wavFile.write(word)
                wavFile.write(' ' + audioPath)
                wavFile.write('\n')
                utt2spk.write(word + ' ' + word + '\n')
    wavFile.close()            
    utt2spk.close()
    os.chmod(outputDir + '/wav.scp', 0o777)
    textFile.close()

    # generating spk2utt using subprocess module
    # response = subprocess.run(['ls', '-la'])
    with open(outputDir + '/spk2utt','w') as spk2utt:
        generateSpk2utt = subprocess.run(['/data/shreya/kaldi/egs/recipes/voxforge_ru/utils/utt2spk_to_spk2utt.pl', outputDir +'/utt2spk'], stdout = spk2utt)

    #task 2: calling only_decode.sh file with three arguments, exp/model_name/graph (look for graph dir, if it doesn't exist raise error), data/, exp/model_name/decode (create a decode dir)
    
    cmd = ['./src/featbin/compute-mfcc-feats', '--config=/data/shreya/kaldi/egs/recipes/voxforge_ru/conf/mfcc.conf','scp,p:'+ outputDir +'/wav.scp', 'ark,scp:'+ outputDir +'/feats.ark,'+ outputDir +'/feats.scp']
    mfcc = subprocess.run(cmd, cwd = '/data/shreya/kaldi', stdout = subprocess.PIPE)

    cmd = ['./src/featbin/compute-cmvn-stats','--spk2utt=ark:'+ outputDir +'/spk2utt', 'scp:'+ outputDir +'/feats.scp', 'ark,scp:'+ outputDir +'/cmvn.ark,'+ outputDir +'/cmvn.scp'] 
    cmvnFeats = subprocess.run(cmd, cwd = '/data/shreya/kaldi', stdout = subprocess.PIPE)

    cmd = ['./steps/only_decode.sh', modelPath + '/graph', outputDir, modelPath + '/decode']
    decode = subprocess.run(cmd, cwd = '/data/shreya/kaldi/egs/recipes/voxforge_ru/', shell = False, stdout = subprocess.PIPE)

    # alignments to ctm
    cmd = ['./src/bin/ali-to-phones', '--ctm-output', modelPath + '/final.mdl', 'ark:'+ modelPath + '/decode/alignments.1', modelPath + '/decode/1.ctm'] 
    phnAlignments = subprocess.run(cmd, cwd = '/data/shreya/kaldi', stdout = subprocess.PIPE)
    
    cmd = ['./steps/get_ctm.sh', outputDir, '/data/shreya/kaldi/egs/recipes/voxforge_ru/data/lang', modelPath + '/decode/']
    wordAlignments = subprocess.run(cmd, cwd = '/data/shreya/kaldi/egs/recipes/voxforge_ru/', stdout = subprocess.PIPE)
        
except Exception as error:
    print(error);

    
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

   

#task 3: convert alignments.JOB file into a ctm file, word.JOB file into a ctm file

#task 4: convert alignments_integer.ctm into alignments_symbol.ctm file

#task 5: converting ctm files into json files

#task 6: linking with the visualization script. So, that it runs the viz on the browser.
