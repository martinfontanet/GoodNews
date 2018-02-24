import requests
import webbrowser
import urllib.request
from bs4 import BeautifulSoup
filePath = '/home/emilio/Desktop/test.jpg'
searchUrl = 'http://www.google.ch/searchbyimage/upload'
multipart = {'encoded_image': (filePath, open(filePath, 'rb')), 'image_content': ''}
response = requests.post(searchUrl, files=multipart, allow_redirects=False)
fetchUrl = response.headers['Location']
#webbrowser.open(fetchUrl)


with open("testurl.html") as fp:
    soup = BeautifulSoup(fp)

print(soup)
#url = requests.get(fetchUrl)
#htmltext = url.text
#print(htmltext)
