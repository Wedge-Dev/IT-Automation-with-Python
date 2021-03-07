#Edit the function check_connectivity so that it returns true if the function returns 200 status_code.

#!/usr/bin/env python3
import requests
import socket

def check_localhost():
  localhost = socket.gethostbyname('localhost')
  if localhost == "127.0.0.1":
    return True
  else:
    return False

def check_connectivity():
  request = requests.get("http://www.google.com")
  response = request.status_code
  if response == 200:
    return True
  else:
    return False