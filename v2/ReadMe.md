### Overview

This documentation allows you to align a Russian-language text file to a Russian-language audio file.


### Instructions to run the code:


1. Install Kaldi:
	
	`git clone https://github.com/kaldi-asr/kaldi.git`
	Then follow the installation instructions at http://jrmeyer.github.io/asr/2016/01/26/Installing-Kaldi.html 
	Once you have run `make -j numJobs` successfully, return to this page.
	
2. Install Gentle:

	`git clone https://github.com/lowerquality/gentle.git`
	Then follow installation instruction(#3) at https://github.com/lowerquality/gentle for OS X & Linux systems.
	
3. Getting this repo on your system: 

	`git clone https://github.com/shreya2111/gentle-labs.git`. After this you have a `gentle` directory inside `gentle-labs/v2`

4. Stiching it all together:
	
	kaldi_path: path to pristine copy of Kaldi
	gentle_path: path to pristine copy of Gentle
	
	on shell execute following lines, 
	```
	`cd gentle-labs/v2/gentle/`
	`python3 scripts/main.py path/audio.wav /path/utterance.txt kaldi_path gentle_path path/kaldi/egs/gentle/data /path/kaldi/egs/gentle/trained_model+lexicon /path/kaldi/egs/gentle/trained_model+lexicon/lexicon.txt`
	```	
	to better understand the args in the python call above: 
	`python3 scripts/main.py audio_path utterance_path kaldi_path gentle_path data_dir path_pre-trained_model lexicon_for_the_langauge`
	
	OR 
	
	Option 1: use singularity recipe placed [here](https://github.com/shreya2111/gentle-singularity) to build the image and run it on singualrity shell following commands given in the ReadMe. 
	Option 2: directly use pre-built Singularity image here on drive [Singularity image](https://drive.google.com/drive/folders/1tt6xWZBODXElJm7aijcRDDTvglDYCHCF?usp=sharing)
	
5. More on `singularity pull` and `singularity bind` coming up! [TO DO]
6. Training German ASR & building custom language model to do automated time-alignment coming up soon [TO DO]

**This directory contains the work done under GSoC 2019 towards extending Gentle to more languages.**
