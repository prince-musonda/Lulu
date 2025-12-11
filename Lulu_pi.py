import pickle
import cv2
from playsound import playsound
import requests
from gpiozero import Button
from signal import pause
import threading
import time, os

time.sleep(5)

Base = "/home/prince/Desktop/projects"
def asset(path):
	return os.path.join(Base, path)
boot_sound_path = asset("assets/bootup_sound.mp3")
def playsound_async(sound_path):
	thread = threading.Thread(target=playsound,args=(sound_path,),daemon=True)
	thread.start()
	return thread

# play boot sound on a different thread to indicate that program as started
playsound(boot_sound_path)
playsound_async(asset('assets/Lulu_analysis.mp3'))
playsound(asset('assets/lulu_activate.wav'))
playsound(asset('assets/lulu_ready.mp3'))
playsound_async(asset('assets/lulu_greet.wav'))
print("running on main thread")
camera = cv2.VideoCapture(0)
def capture_and_send():
	success, frame = camera.read()
	cv2.imwrite(asset("assets/scene.jpg"),frame)
	files = {"file": open(asset('assets/scene.jpg'),'rb')}
	playsound_async(asset('assets/Lulu_analysis.mp3'))
	response = requests.post('https://mai-unvisceral-finickily.ngrok-free.dev/send_data',files=files)
	with open(asset("assets/output.wav"),'wb') as file_object:
		file_object.write(response.content)
	print(response.status_code)
	# play audio description of the environment
	playsound_async(asset("assets/output.wav"))


button = Button(12)

button.when_pressed = capture_and_send
pause()
