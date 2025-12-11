# **README – Lulu**

## **Problem**
Lulu is a wearable device built on a Raspberry Pi with a camera that helps visually impaired people understand their surroundings. The device captures images and sends them to a powerful AI backend running in Google Colab, which describes the scene and returns a spoken audio file to the wearable.

People with visual impairments often rely on sound, touch, or assistance from others to understand what is happening around them.
Simple tasks such as identifying objects on a table, reading a sign, checking what’s in front of them, crossing the streets or interpreting a scene can require extra effort or help from someone else.

A small, portable, and automatic way to capture and describe visual information could make everyday tasks easier and more independent.

## **Goal**

Lulu is designed to give quick, spoken descriptions of the world around the user.
The system focuses on being:

* **wearable**
* **simple to operate**
* **low-cost**
* **lightweight**
* **open and hackable**

The aim is to demonstrate how a Raspberry Pi and a remote AI model can work together to provide instant visual descriptions whenever the user triggers the device.

---

# **How Lulu Works**

### **Backend (Google Colab)**

The backend handles all the heavy processing:

* Runs a Flask server
* Receives an uploaded image
* Uses a vision model to generate a description
* Converts the text to speech
* Returns the audio file

Each time it starts, it prints an ngrok URL that the Raspberry Pi can connect to.

### **Client (Raspberry Pi Wearable)**

The client acts as the capture-and-play device:

* Takes a picture using the Pi Camera
* Sends the image to the backend
* Receives an audio file
* Plays the audio through a speaker

You provide the backend URL through the command line:

```
python3 lulu.py https://your-ngrok-url/send_data
```

---

# **Installation (Raspberry Pi Client)**

### System packages

```
sudo apt update
sudo apt install python3-opencv -y
```

### Python packages

Add this to `requirements.txt`:

```
playsound
requests
```

Install:

```
pip install -r requirements.txt
```

---

# **Running Lulu**

1. Start the backend in Google Colab.
2. Copy the ngrok URL it prints.
3. On the Raspberry Pi, run:

```
python3 lulu.py <YOUR_BACKEND_URL>
```

Lulu will then:

1. capture an image
2. send it to the backend
3. receive the audio description
4. play it aloud

---

# **Purpose**

Lulu is a simple prototype showing how a small device can give real-time audio descriptions on demand.
It is meant for experimenting, learning, and building accessible tools using:

* a Raspberry Pi
* a basic camera
* a remote AI model

You can extend it with buttons, wearable mounts, microphones, or more advanced models depending on your needs.

---

If you'd like, I can put this into a perfectly formatted GitHub Markdown style with sections, code blocks, and examples.
