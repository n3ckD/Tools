#!/usr/bin/python

# Simple bot to monitor if a website has changed. Great for ticket sales ;)

import time
import requests
import hashlib

# URL to check
URL = 

# Get initial hash of the page
response = hashlib.md5(requests.get(url = URL).text.encode('utf-8').strip()).hexdigest()

m1 = response
print(time.asctime( time.localtime(time.time())), m1)

# Forever check if the hash of the site has changed. Indicating an update
while 1:
	m2 = hashlib.md5(requests.get(url = URL).text.encode('utf-8').strip()).hexdigest()
	print(time.asctime(time.localtime(time.time())), m2)
	if m1 != m2:
		print(time.asctime(time.localtime(time.time())), "SITE HAS CHANGED.")
	time.sleep(10)