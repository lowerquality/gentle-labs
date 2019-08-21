## Project Overview:
 > The project is about extending an existing text-to-speech forced aligner to more languages. The tool that I am working on, known as Gentle, is a forced aligner for speech; it is an open source tool developed by a number of people from all around the world. One main author is Robert M. Ochshorn, my mentor for the project. The tool takes a sentence as input along with its audio data, utilizes the audio data in an automatic speech recognition (ASR) model to predict a transcription as well as time-aligns the words to the time when those were spoken in the speech.



## Gentle Experiments

This is a scratch pad for visualizations and working process scripts
for extensions to Gentle.

* Russian Timing Visualization

```sh
cd timing-viz/
yarn
yarn start
```

This script expects a `data` directory in `timing-viz/public/` containing

```js
data/
    - wav/
            * [sample_name].wav
            * …
    - json/
            * meta.json
                    #Should contain an object with the following mapping:
                    {sample_name: {
                            ground_truth: <transcript string>
                     }, …}
            * [sample_name].words.json
                    #Something like:
                    [{text: <str>,
                      start_time: <float>,
                      end_time: <float> }, …]
            * [sample_name].phonemes.json
                    #Something like:
                    [{text: <str>,
                      start_time: <float>,
                      end_time: <float> }, …]
```
