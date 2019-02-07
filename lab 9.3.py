import urllib.request
import re

url = 'http://pythonprogramming.net/parse-website-using-regular-expressions-urllib/'

req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
respData = resp.read()

for eachP in paragraphs:
    print(eachP)
