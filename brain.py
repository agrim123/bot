import random
import os
import platform

greetings = ["hello","hi","yo"]
greetings_response = ["whats up?","how u doing?","how's day going?","yoo!!"]
exit_command = ["exit","quit","close","leave"]
sys_command = ["sysinfo"]

def sys_response(command):
	sys_command_list[command]()

def sysinfo():
	print os.getlogin()
	print platform.machine()
	print platform.version()
	print platform.system()
	print platform.processor()

sys_command_list = {
	"sysinfo": sysinfo
}

def brain(command):
	if any(command in s for s in greetings):
		return random.choice(greetings_response)
	elif any(command in s for s in sys_command):
		return sys_response(command)
	elif any(command in s for s in exit_command):
		return 0
	else:
		return "Unkown Command"
