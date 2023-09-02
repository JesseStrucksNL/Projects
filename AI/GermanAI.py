import speech_recognition as sr
import pyttsx3

import os
from dotenv import load_dotenv
load_dotenv()
OPENAI_KEY = os.getenv('')

import openai
openai.api_key = OPENAI_KEY

def SpeakText(command):

	engine = pyttsx3.init()
	engine.say(command)
	engine.runAndWait()

r = sr.Recognizer()

def record_text():

	while(1):
		try:

			with sr.Microphone() as source2:

				r.adjust_for_ambient_noise(source2, duration=0.2)
				print ("Listening")

				audio2 = r.listen(source2)

				MyText = r.recognize_google(audio2)

				return MyText

		except sr.Requesterror as e:
			print("Could not procces reuqested results; {0}".format(e))

		except sr.UnkownValueError:
			print("Unknown error please contact @Jesse")

def send_to_chatGPT(messages, model="gpt-3.5-turbo"):

	response = openai.ChatCompletion.create(
		model=model,
		messages=messages,
		max_tokens=255,
		n=1,
		stop=None,
		temperature=0.5,
	)

	message = response.choises[0].message.content
	messages.append(response.choises[0].message)
	return message

messages = [{"role": "user", "content": "Behave like a german soldier in the year 1940 whenever a user asks a question. Your name is kevin"}]
while(1):
	text = recort_text
	messages.append({"role": "user", "content": text})
	response = send_to_chatGPT(messages)
	SpeakText(response)

	print(response)
