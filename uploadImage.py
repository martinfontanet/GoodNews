import requests
import webbrowser
import urllib.request
from bs4 import BeautifulSoup
filePath = '/home/emilio/Desktop/test.jpg'

#filePath = '/Users/raphaelstrebel/Downloads/Hien-Nhon-gate.jpg'

searchUrl = 'http://www.google.ch/searchbyimage/upload'
multipart = {'encoded_image': (filePath, open(filePath, 'rb')), 'image_content': ''}
response = requests.post(searchUrl, files=multipart, allow_redirects=False)
fetchUrl = response.headers['Location']
#webbrowser.open(fetchUrl)
with open("https://www.google.ch/search?tbs=sbi:AMhZZiv-OVkc_1op5Dmtxmc1AduKJGgKkk_1O1sZesqUWom7OcBSItxkC58ACuBnoM8w96A_1NwpFVtq2u9bmUO7Nv1Z3vOjuI-ofo6Hy6yoFxbb8hMMuXpc1si5XCTCskDzMFG0E7n0q2qdUEnd8ViXLxNsVfeDdgUIGWvF0nYDYQTJk8B4MHl2Q0lkvrGMBZcndwKRQPmoihkinkMc933rLxqBVQkdMs_1WQcax9JcaITRa0rUU5gwY5qKhyqGHFFTUlp1p9eVZho33f78RzUljrCQfX8qAb29xMLvs2lHTFtc6EAF8-OIIBKJCAMNtHqmRmSVF8eVLueX.html") as fp:
    soup = BeautifulSoup(fp)

print(soup)

