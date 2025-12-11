import cv2
from playsound import playsound
import requests
import threading
import os

boot_sound_path = "./assets/bootup_sound.mp3"
def playsound_async(sound_path):
	thread = threading.Thread(target=playsound,args=(sound_path,),daemon=True)
	thread.start()
	return thread

# play boot sound on a different thread to indicate that program as started
playsound(boot_sound_path)
playsound_async('./assets/lulu_activate_effect.mp3')
playsound('./assets/lulu_activate.wav')
playsound('./assets/lulu_ready.mp3')
playsound_async('./assets/lulu_greet.wav')
print("running on main thread")
camera = cv2.VideoCapture(1)
def capture_and_send():
	success, frame = camera.read()
	cv2.imwrite("./assets/scene.jpg",frame)
	files = {"file": open('./assets/scene.jpg','rb')}
	playsound_async('./assets/lulu_analysis.mp3')
	response = requests.post('https://mai-unvisceral-finickily.ngrok-free.dev/send_data',files=files)
	with open("./assets/output.wav",'wb') as file_object:
		file_object.write(response.content)
	print(response.status_code)
	# play audio description of the environment
	playsound_async("./assets/output.wav")

while(True):
	input()
	capture_and_send()

