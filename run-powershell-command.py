import subprocess


def run(command):
	result = {}
	result = subprocess.run(["powershell", "-Command", command], capture_output=True)
	return result.stdout.decode('utf-8').splitlines()