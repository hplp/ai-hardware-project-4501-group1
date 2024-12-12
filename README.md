# AI_Hardware_Project_Template

https://studio.edgeimpulse.com/public/551144/live

## Team Name: 
**LumineSCent**

## Team Members:
- Kyle Clemente
- Daniel Sarria
- Phi Lu

## Project Title:
** Hey Jarvis, Turn the Lights On**

## Project Description:

***Voice-Controlled LED Toggle with Edge Impulse***

This project demonstrates how to use the Arduino Nano 33 BLE Sense with Edge Impulse to toggle an LED in response to the keyword "Hey Jarvis." The goal is to showcase the integration of machine learning and embedded systems. It provides accessible use of lights for those with disabilities. 

![Arduino BLE](https://github.com/hplp/ai-hardware-project-4501-group1/blob/main/FinalProjectReport/arduinoBLE.jpg)

The system features voice recognition and LEDs.
It recognizes voice commands and executes them to control a lighting system with the execution of each command.

## Key Objectives:
- Train a machine learning model to recognize the keyword "Hey Jarvis."
- Deploy the model to an Arduino Nano 33 BLE Sense.
- Toggle an LED on pin 9 when the keyword is detected.

## Technology Stack:
Hardware platform: Arduino Nano 33 BLE Sense  
Software tools: Edge Impulse Studio, Arduino IDE  
Languages: C++, Python

## Tutorial
1. Set Up the Device \
Edge Impulse contains descriptive and helpful guides to assist users when setting up the device properly, installing
the correct firmware, and running the device to collect data.

Here is the guide for the Arduino board: https://docs.edgeimpulse.com/docs/edge-ai-hardware/mcu/arduino-nano-33-ble-sense

2. Data Acquisition and Training the Model \
Edge Impulse makes it easy to upload and gather data samples for training the model. Following the steps in this video
(https://youtu.be/ckD3InrSXo0), it was easy to gather data, view MFCCs, train the model, and view data cluster representations.

3. Deployment to Arduino \
To deploy the device to Arduino, the proper Arduino library must be downloaded from Edge Impulse and uploaded to the
Arduino IDE. Also, after training the model, the proper firmware must be uploaded to the device also from Edge Impulse.

4. Set up the Circuit \
Set up the circuit on a breadboard using a 330-ohm resistor in series with an LED connected to pin 9 of the Arduino board. Connect
the device to your computer in the desired port.

6. Developing Arduino Code \
Now that the Arduino IDE is set up, run the code from the 'nano_33ble_sense_microphone.ino' file. Once running, open the
'Serial Monitor' in the IDE to view what the device is hearing, displayed in the demo video 'JarvisOutput.mp4' located inside the repository.

## Expected Results
- Say "Hey Jarvis" and observe the LED toggling.
- Here is a demo example for the LED: https://drive.google.com/file/d/1v56EXrp1sznGvh6LEekcjANxnNL9UzKR/view?usp=drive_link
- Serial monitor should display the detected keyword with confidence.
- Here is what the serial monitor should display: https://drive.google.com/file/d/1dQ4PPbfzu6OgpTedZ8HtvWB5OeYeskQq/view?usp=drive_link
  
## Known Issues and Solutions

1. _Issue:_ System currently only recognizes keyword "Hey Jarvis." \
_Solution:_ Include additional training data for new possible keywords, balance training dataset to account for new training data, and implement new keyword's functionality on the embedded hardware.

2. _Issue:_ System currently can only toggle LED with recognized keyword. \
_Solution:_ Add to embedded code to include additional functionalities, map new functionalities to potential additional recognized keywords.

## Timeline:
November 4 - November 7 === Create and present our project introduction/proposal  
November 8 - November 15 === Receive hardware, download software, and gather audio files to train the model  
Novemeber 18 - Novemeber 22 === Train the model, start initial testing  
November 25 - November 27 === Week of Thanksgiving, dedicated to debugging and fixes  
December 2 - December 5 === Finalize prototype, create and give presentation/demo on our project
