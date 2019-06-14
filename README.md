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