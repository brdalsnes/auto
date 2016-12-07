#!/usr/bin/env python3

import speech_recognition as sr

def get_speech():
	# obtain audio from the microphone
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)

	# recognize speech using Google
	return r.recognize_google(audio)

#Returns the accepted word of a string, if any
#Necessary because there might be extra words
def get_word(accepted, string):
	for i in range(0, len(accepted)):
		if accepted[i] in string:
			return accepted[i]
	return ""

#Ask for answers until the user gets it right
def answer(accepted):
	ans = get_speech()
	word = get_accepted_word(accepted, ans)
	while word not in accepted:
		os.system("mpg123 repeat.mp3")
		ans = get_speech()
		word = get_accepted_word(accepted, ans)
	return word

	