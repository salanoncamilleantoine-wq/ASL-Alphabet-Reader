# ASL-Alphabet-Reader
# ASL Alphabet Recognition on NVIDIA Jetson Orin

## Why I Made This Project

I chose to make an ASL alphabet recognition project because it looked challenging and different from a basic AI project.

I wanted to build something that could actually use a camera in real time instead of only testing AI on saved images. I also wanted to challenge myself by working with computer vision, machine learning, Docker, Linux, and NVIDIA Jetson hardware.

Another reason I chose this project was because I wanted to understand the full process of creating an AI system. This included finding datasets, cleaning the data, training a model, fixing errors, testing it with a real webcam, and making the final program speak the detected letter.

My goal was to create a system where I could show an ASL letter with my hand, have the AI recognize it, display the letter on screen, and say the letter out loud.

## About the Project

This project is a real-time American Sign Language alphabet recognition system built on an NVIDIA Jetson Orin.

It uses:

* ResNet-18
* Transfer learning
* PyTorch
* NVIDIA Jetson Inference
* CUDA
* TensorRT
* Docker
* Python
* A USB webcam
* eSpeak NG for text-to-speech

The trained model recognizes ASL hand signs and predicts which letter is being shown.

## How It Works

The project follows this process:

1. A webcam captures the user's hand.
2. The camera image is sent to the trained ResNet-18 model.
3. The model predicts the ASL letter.
4. The program displays the predicted letter and its confidence.
5. The program waits until the same letter stays stable.
6. The detected letter is sent to a text-to-speech queue.
7. eSpeak NG reads the letter aloud.

## Training the AI

I used transfer learning with ResNet-18 instead of training a neural network completely from scratch.

I combined multiple ASL image datasets so the model could see more examples of each hand sign.

I also improved the dataset by:

* Removing corrupted images
* Adding more images from different datasets
* Adding real webcam images
* Changing brightness
* Changing contrast
* Changing saturation
* Adding different lighting conditions
* Adding shadows
* Changing sharpness

The model was trained to recognize 27 classes:

* A-Z
* `nothing`

After training, the PyTorch model was exported to ONNX so it could run efficiently with TensorRT on the NVIDIA Jetson.

# Running the Project

Follow these steps in order.

## Step 1 — Connect the Webcam

Connect a webcam to the NVIDIA Jetson Orin.

The project normally uses:

`/dev/video0`

## Step 2 — Open Linux / NoMachine

Open the Jetson desktop through NoMachine.

Then open a Linux terminal.

Run:

```bash
xhost +local:root
```

Go to the project folder:

```bash
cd ~/ASL_AI_COMPLETE_BACKUP/jetson-inference
```

Start the Jetson Inference Docker container:

```bash
DISPLAY=:0 docker/run.sh
```

When Docker starts, the terminal prompt should begin with:

`root@nvidia-desktop`

This means you are now inside Docker.

## Step 3 — Go to the Classification Folder

Inside Docker, run:

```bash
cd /opt/jetson-inference/python/training/classification
```

## Step 4 — Start the ASL Recognition Program

Run:

```bash
python3 data/asl/asl_tts_crop.py
```

The webcam window should open.

The program will now:

1. Capture the webcam image.
2. Focus on the hand area.
3. Send the image to the ResNet-18 model.
4. Predict an ASL letter.
5. Display the predicted letter.
6. Display the confidence percentage.

Leave this terminal running.

## Step 5 — Start the Voice System

Open a **second Linux / NoMachine terminal**.

Do not enter Docker in this terminal.

Run:

```bash
cd ~/ASL_AI_COMPLETE_BACKUP/jetson-inference/python/training/classification
```

Then start the text-to-speech listener:

```bash
tail -n0 -F data/asl/tts_queue.txt | while read -r letter; do espeak-ng -v en-us -s 140 "$letter"; done
```

Leave this terminal running.

## Step 6 — Test the AI

You should now have two terminals running.

**Terminal 1**

Docker running the webcam and AI model.

**Terminal 2**

Linux running the text-to-speech system.

Now place your hand in front of the webcam and make an ASL letter.

The system should:

1. See your hand.
2. Predict the letter.
3. Show the result on screen.
4. Wait for a stable prediction.
5. Speak the letter aloud.

## Stopping the Project

To stop the webcam program, press:

`Ctrl + C`

To stop the voice program, press:

`Ctrl + C`

To leave Docker, run:

```bash
exit
```

## Challenges I Faced

One of the hardest parts of the project was getting the model to work with a real webcam.

A model can perform well on validation images but still struggle with live camera images because of differences such as:

* Backgrounds
* Lighting
* Hand size
* Camera quality
* Distance from the camera
* Hand position

I also had to fix problems with:

* Docker
* CUDA
* Model exporting
* Dataset folders
* Corrupted images
* Incorrect predictions
* Confidence thresholds
* Webcam input
* Text-to-speech
* Training accuracy

## What I Learned

This project taught me how the different parts of an AI system work together.

I learned how to:

* Train an image classification model
* Use transfer learning
* Work with ResNet-18
* Prepare large datasets
* Remove corrupted images
* Add image augmentation
* Use Docker
* Use Linux
* Use NVIDIA Jetson Inference
* Use CUDA and TensorRT
* Export a model to ONNX
* Run AI using a live webcam
* Add text-to-speech
* Debug machine learning problems

## Future Improvements

In the future, I would like to improve the project by:

* Improving accuracy for similar hand signs
* Collecting more real webcam images
* Automatically detecting the hand
* Improving recognition under different backgrounds
* Supporting moving signs such as J and Z
* Recognizing full words
* Recognizing complete sentences
* Creating a better graphical interface
* Turning the project into a complete ASL translator

## Final Goal

The main reason I made this project was to challenge myself and learn how a real AI computer vision project is built from beginning to end.

Instead of only training a model, I wanted to create something that could actually run in real time, interact with a person, and combine computer vision with speech.

This project helped me understand that building AI requires much more than training a neural network. It also requires data collection, testing, debugging, optimization, and making the system work in the real world.
