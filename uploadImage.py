import requests
import webbrowser

filePath = '/Users/raphaelstrebel/Downloads/Hien-Nhon-gate.jpg'
searchUrl = 'http://www.google.ch/searchbyimage/upload'
multipart = {'encoded_image': (filePath, open(filePath, 'rb')), 'image_content': ''}
response = requests.post(searchUrl, files=multipart, allow_redirects=False)
fetchUrl = response.headers['Location']
webbrowser.open(fetchUrl)