import './index.css';
import { E } from "./div.js";

const TIMESCALE = 200;

class TimedTextPlayer {
  constructor($parent, data, sample_id) {
    // Create a wrapping div that shows the passage of time
    this.$el = E.div($parent, {class: "timed-text"});

    // Create an audio element
    this.$audio = E.audio($parent, {controls: true, src: `/data/wav/${sample_id}.wav`})

    // Next step is to connect audio playback to the timing
    // visualization.  You can either use the `ontimeupdate` callback
    // from this.$audio, or set up a `window.requestAnimationFrame` in
    // the browser, which will be fired more frequently.  Then, you
    // can check `this.$audio.currentTime` to see where the audio
    // element is and adjust the position of a "razor" line (similar
    // to how the `tick` lines are display below.
    //
    // this.$audio.currentTime = 3
    //
    // will seek the audio to three seconds in. This could be used in
    // a click handler on `this.$el` to allow direct manipulation
    // playback control.

    // Make a tick for every second
    // XXX: Estimate duration from the end of text
    let duration = data[data.length-1].end;
    for(let t=0; t<duration; t+=1) {
      let $tick = E.div(this.$el, {class: "tick"});
      let $num = E.div(this.$el, {class: "number"}, t + "s");
      $tick.style.left = TIMESCALE * t + "px";
      $num.style.left = TIMESCALE * t + "px";
    }

    // Loop through the data and place every word based on its time offset
    data.forEach(({text, start, end}) => {

      let $wd = E.div(this.$el, {class: "word"}, text);

      $wd.style.left = start * TIMESCALE + "px";
      $wd.style.width = (end-start) * TIMESCALE + "px";

      $wd.onclick = () => {
        this.$audio.currentTime = start;
      }

    });
  }

}

function start() {
  E.h1(document.body, {}, "Russian Timing Visualization");

  // Fetch metadata
  fetch("/data/json/meta.json")
    .then((x) => x.json())
    .then((ret) => {
      console.log("Got metadata", ret);

      // Loop through and display ground truth

      ret.forEach(({ground_truth, sample}) => {

        // Create an element for timing
        let $samp = E.div(document.body);

        // Put in the sample name
        E.h2($samp, {}, sample);
        E.div($samp, {}, ground_truth);

        // Fetch word timing data
        fetch(`/data/json/${sample}_word.json`)
          .then((x) => x.json())
          .then((data) => {
            let tt = new TimedTextPlayer($samp, data, sample);
          })
      });

    });

}

window.onload = start;
