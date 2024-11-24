**Step 1: Set up hardware** \
We connected the Arduino to our computer and installed all necessary software. We cloned the project into our EdgeImpulse repository and were able to connect to our board. We were then able to upload data to our Arduino for use in training the model. A screenshot of our custom keyword ("Hey_Jarvis") training using our own different voices is included as "audioSplit.png" in this folder. \
 \

We've gathered abundant audio files for our trigger words 'Hey Jarvis', our command words 'turn on the lights' and 'turn off the lights', and background/unknown noise to use to train our model.
 
**Step 2: Identify/Train the model** \
After building dataset, we designed our impulse using MFCC signal processing block. We configured and trained our neural network.
\

**Step 3: Program your hardware** \
With the impulse designed, trained and verified we deployed this model back to the Arduino Nano 33 BLE by flashing it.
\

**Step 4: Run the first iterations** \
We connected to the board's newly flashed firmware over serial and ran first testing using "edge-impulse-run-impulse --continuous" to capture audio from the microphone, run the MFCC code, and then classify the spectrogram to either "hey jarvis", "turn on the lights", "turn off the lights", noise, and unknown. 
\

