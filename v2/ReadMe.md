**This directory contains the work done under GSoC 2019 towards extending Gentle to more languages.**

## Project Overview:
 > The project is about extending an existing text-to-speech forced aligner to more languages. The tool that I am working on, known as Gentle, is a forced aligner for speech; it is an open source tool developed by a number of people from all around the world. One main author is Robert M. Ochshorn, my mentor for the project. The tool takes a sentence as input along with its audio data, utilizes the audio data in an automatic speech recognition (ASR) model to predict a transcription as well as time-aligns the words to the time when those were spoken in the speech.
	

### Instructions to run the code:


1. Install Kaldi

2. Place gentle/ as a recipe inside Kaldi/egs

3. The scripts placed inside gentle/scripts/ and gentle/gentle need to be executed to get the language model files, decoding graph and audio file speech features.

	-> Start with keeping:
	
		1. audio.wav and audio.txt files inside gentle/initial/
		2. final.mdl and tree inside gentle/model
		3. lexicon.txt inside gentle/lexicon/
		
	-> run gentle/scripts/initialize.py with correct arguments (look into the script for usage)[TO DO: usage info]
	
	-> Automated language model generation
	
	run gentle/gentle/generateLM.py with correct arguments.[TO DO: usage info]
	
	your proto_dir will be 'gentle/data'

	Steps are:

		1. inside proto_dir/dict : Lexicon and phones files get created

		2. prep_lang.py which will use proto_dir/dict/ files to generate L.fst etc inside proto_dir/langdir 

		# validate_dict_dir
		# this call expects that all the language, dictionary, input, steps and utils will reside in 'gentle'
		# 'gentle' will reside in kaldi/egs as a recipe


		3. Used gentle language_model codebase to generate HCLG.fst inside proto_dir/tdnn_7b_chain_online/graph_pp
		4. Also, copy final.mdl, tree to gentle/model/ and HCLG.fst to gentle/model/graph
		5. Also copies proto_dir/langdir/* to proto_dir/tdnn_7b_chain_online/graph_pp


	-> Automate decoding process: 
	run automatedDecoding.py with correct args [TO DO: usage info]

	Steps are:

	1. Generate inputs like utt2spk, wav.scp etc inside proto_dir/feats/
	2. Generate feats.scp etc inside proto_dir/feats/
	3. Gmm-latgen output goes in proto_dir/tdnn_7b_chain_online/decode and proto_dir/decode
	4. Produce CTM files for words and phoneme alignments inside 
	proto_dir/tdnn_7b_chain_online/decode and proto_dir/decode
	5. Produce JSON files for the CTM files inside proto_dir/json

