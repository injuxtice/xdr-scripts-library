import subprocess


def run(commands_list):
	result = {}
	for command in commands_list:
		result = subprocess.run(["powershell", "-Command", command], capture_output=True)
	return result