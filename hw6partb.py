# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')

count = int(input("Enter count: "))
position = int(input("Enter position: "))

def find_url(url):
	html = urllib.request.urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	names = []
	tags = soup('a')
	for tag in tags:
		names.append(tag.get('href', None))
	return names

for x in range(count):
	url = find_url(url)[position - 1]
print(url[30:-10])