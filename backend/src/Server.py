from http.server import BaseHTTPRequestHandler, HTTPServer
from json import JSONDecodeError
from PredictFakeness import predictFakeness
import ssl
import json

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
        self.end_headers()
        
    def do_POST(self):
        sentSize = int(self.headers['Content-Length'])
        sentData = self.rfile.read(sentSize).decode("utf-8")
        
        self._set_headers()
        try:
        	parsed = json.loads(sentData)
        	self._respond(self._prepareResponse(parsed))
        except JSONDecodeError:
        	self._respond("The body you sent doesn't look like valid json.")
        except Exception as e:
        	print(e)
        	self._respond("Internal error")

    def _respond(self, text):
    	self.wfile.write(bytes(text, "utf-8"))

    def _prepareResponse(self, args):
    	if "imagePath" not in args or "url" not in args:
    		return "the JSON should contains keys \"imagePath\" and \"url\""
    	else:
    		return predictFakeness(args["imagePath"], args["url"])

if __name__ == "__main__":
	port = 8080
	httpd = HTTPServer(('localhost', port), RequestHandler)
	httpd.socket = ssl.wrap_socket(httpd.socket, certfile='/Users/gilbert/Programming/hackatons/starthack2018/server.pem', server_side=True)
	print(" - Starting the server at address: https://localhost:" + str(port))
	print(" - Currently accepting POST requests")
	print(" - To shut-down the server, use ctrl + c")
	httpd.serve_forever()
