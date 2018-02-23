import requests
import webbrowser
import urllib.request
filePath = '/home/emilio/Desktop/test.jpg'
searchUrl = 'http://www.google.ch/searchbyimage/upload'
multipart = {'encoded_image': (filePath, open(filePath, 'rb')), 'image_content': ''}
response = requests.post(searchUrl, files=multipart, allow_redirects=False)
fetchUrl = response.headers['Location']
webbrowser.open(fetchUrl)

opener = urllib.request.FancyURLopener({})
f = opener.open(fetchUrl)
content = f.read()
print(content)
