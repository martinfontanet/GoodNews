# The project
This simple Firefox add-on detects for you fake news article. You can verify this for any article in any language.

# How to make it run
Since it was a hackaton project, the run process is quite tedious. It involves running three servers in local.

## Server 1
This one is located in backend/src/Server.py. Before anything, you want to create a certificate. In a terminal, type in ```openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes```. Modify Server.py at line 82 to the path of your newly created certificate. Make your system and firefox accept the certificate. Once this is done, simply run ```python3 Server.py"```.

## Server 2
This one is located in backend/mrisa-master/src/server.py. Simply run ```python3 server.py```.

## Server 3
1) Get language tool on https://languagetool.org (download the "Stand-alone for your Desktop" version)
2) Run the language tool server: ```java -cp languagetool-server.jar org.languagetool.server.HTTPServer --port 8082```

## Actually making it run
Open Firefox, go to about:debugging, select "Load temporary Add-on" and choose the file frontend/Firefox Addon/goodnews.js. Go to any article page, you should see a "Fake News Scan". You can start analyzing.

# Tips, about etc.
Don't hesitate to try satirical website like theonion.com or plain conspirationist website. The model behind this fake news detection is to parse an article, get all of its image and find other article sharing the same images on the web. If their content match then we might think that the information is truthfull, else that it is some fake news. Together with that, other features are engineered and some regression tree is applied at the hand (hand coded for now ;-))
