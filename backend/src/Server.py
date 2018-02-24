from http.server import BaseHTTPRequestHandler, HTTPServer
from json import JSONDecodeError
from PredictFakeness import predictFakeness
import ssl
import json
import requests
from ContentExtractor import *

# HTTPS server idea taken at http://www.piware.de/2011/01/creating-an-https-server-in-python/
# 
#GENERATING A SSL KEY:
#    openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes
#
# you might need to add it to your system keychain, on mac os X for instance, double-click on server.pem and do stuff.

# RequestHandler basic example taken on https://gist.github.com/bradmontgomery/2219997

class RequestHandler(BaseHTTPRequestHandler):
    
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('Access-Control-Allow-Origin', "*")
        self.end_headers()
        
    def do_POST(self):
        print("========================Request received========================")
        sentSize = int(self.headers['Content-Length'])
        sentData = self.rfile.read(sentSize).decode("utf-8")
        self._set_headers()
        parsed = json.loads(sentData)
        self._respond(self._prepareResponse(parsed))

    def _respond(self, text):
        print(text, type(text))
    	self.wfile.write(bytes(text, "utf-8"))

    def _prepareResponse(self, args):
        if "url" not in args:
            return "the JSON should contains key \"url\""
        else:
            website = Website(args["url"]).fetch()
            if not website.isArticle():
                return '{"isFake": 0, "message": "This is not an article!", "isArticle": 0}'
            print("1")
            images = website.getImages()
            print(images)
            print("2")
            imagesLinks = []
            print("3")
            for image in images:
                imagesLinks.extend(self._getLinksForImageURL(image))

            print("images:",imagesLinks)
            ###
            return json.dumps(predictFakeness(args["url"],imagesLinks))

    def _getLinksForImageURL(self, imageURL):
        url = 'http://localhost:5000/search'
        headers = {'Content-Type': 'application/json'}
        payload = '{ "image_url": "'+imageURL+'" }'
        r = requests.post(url, headers=headers, data=payload)
        try:
            parsed = json.loads(r.text)
        except Exception as e:
            print(e)
            return []

        print("parsed",parsed)
        return parsed["links"][:5]

if __name__ == "__main__":
	port = 8080
	httpd = HTTPServer(('localhost', port), RequestHandler)
	httpd.socket = ssl.wrap_socket(httpd.socket, certfile='/home/martin/Desktop/server.pem', server_side=True)
	print(" - Starting the server at address: https://localhost:" + str(port))
	print(" - Currently accepting POST requests")
	print(" - To shut-down the server, use ctrl + c")
	httpd.serve_forever()
