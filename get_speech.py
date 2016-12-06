#!/usr/bin/env python3

import speech_recognition as sr

def get_speech():
	# obtain audio from the microphone
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)

	# recognize speech using Sphinx
	try:
		return r.recognize_sphinx(audio)
	except:
		return "Error"