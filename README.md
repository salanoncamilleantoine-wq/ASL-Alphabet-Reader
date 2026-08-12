# ASL Alphabet Recognition on NVIDIA Jetson Orin

## Why I Made This Project

I chose this project because it looked challenging and interesting. I wanted to create something that used AI and computer vision in real time instead of only testing a model on saved images.

My goal was to make a system that could recognize ASL hand signs through a webcam, display the predicted letter, and say the letter out loud.

## About the Project

This project is a real-time American Sign Language alphabet recognition system built on an NVIDIA Jetson Orin.

It uses:

* ResNet-18
* Transfer learning
* Python
* NVIDIA Jetson Inference
* Docker
* TensorRT
* A webcam
* eSpeak NG for text-to-speech

The model was trained on ASL alphabet images and recognizes A-Z plus a `nothing` class.
## The Video link on Youtube is https://youtu.be/o0UU1oxS8IU
## How It Works

1. The webcam captures the user's hand.
2. The program focuses on the center area of the camera.
3. The ResNet-18 model predicts the ASL letter.
4. The predicted letter and confidence are displayed.
5. When the same prediction stays stable, the letter is sent to the text-to-speech system.
6. eSpeak NG says the detected letter aloud.

## Training

I used transfer learning with ResNet-18 and combined multiple ASL datasets.

I also improved the training data by using:

* Different lighting
* Brightness changes
* Contrast changes
* Shadows
* Real webcam images
* More examples of different ASL letters

The trained model was exported to ONNX so it could run efficiently on the Jetson using TensorRT.

# How to Run the Project

## Step 1 — Connect the Webcam

Connect the webcam to the NVIDIA Jetson Orin.

The project normally uses:

`/dev/video0`

## Step 2 — Open Linux / NoMachine

Open the Jetson desktop through NoMachine and open a Linux terminal.

Run:

```bash id="op8e3q"
xhost +local:root
cd ~/ASL_AI_COMPLETE_BACKUP/jetson-inference
DISPLAY=:0 docker/run.sh
```

When the prompt starts with `root@nvidia-desktop`, you are inside Docker.

## Step 3 — Start the AI Program

Inside Docker, run:

```bash id="b4r8of"
cd /opt/jetson-inference/python/training/classification
python3 data/asl/asl_tts_crop.py
```

Keep this terminal running.

## Step 4 — Start the Voice

Open a second normal Linux / NoMachine terminal.

Do not enter Docker in this terminal.

Run:

```bash id="py5p47"
cd ~/ASL_AI_COMPLETE_BACKUP/jetson-inference/python/training/classification
tail -n0 -F data/asl/tts_queue.txt | while read -r letter; do espeak-ng -v en-us -s 140 "$letter"; done
```

Keep this terminal running.

## Step 5 — Test the Project

Place your hand in front of the webcam and make an ASL letter.

**Important:** Your hand needs to be **close to the webcam and near the middle of the screen** for the model to work best.

For better recognition:

* Keep your hand in the center of the camera.
* Move your hand fairly close to the webcam.
* Make sure your whole hand is visible.
* Hold the sign still for a moment.
* Use good lighting.
* Try to avoid a very busy background.

If your hand is too far away or outside the center area, the model may predict the wrong letter.

The system will then:

1. Detect your hand sign.
2. Predict the ASL letter.
3. Display the letter and confidence.
4. Wait for the prediction to stay stable.
5. Speak the letter aloud.

## Stopping the Project

Press `Ctrl + C` to stop the camera program or voice listener.

To exit Docker:

```bash id="sfo1sk"
exit
```

## What I Learned

This project taught me how to:

* Train an AI image classification model
* Use transfer learning
* Prepare and improve datasets
* Use Docker and Linux
* Export a model to ONNX
* Run AI on an NVIDIA Jetson
* Use a live webcam with computer vision
* Add text-to-speech
* Debug real-world AI problems

## Final Goal

The main goal of this project was to challenge myself and understand how a real AI computer vision system is created from training all the way to a working real-time application.

