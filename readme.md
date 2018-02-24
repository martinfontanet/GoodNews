To run the backend server:
  
  1) Get language tool on https://languagetool.org
  2) Run the language tool server: java -cp languagetool-server.jar org.languagetool.server.HTTPServer --port 8082
  3) Run the GoodNews analyzer server: python3 Server.py


The reverse image search uses MRISA (Meta Reverse Image Search API).

  link: http://mrisa.mage.me.uk/
  
  You first need to install the dependencies
  
  `pip install certifi flask pycurl beautifulsoup4`
  
  To launch the server:
    1) Download the compressed file from MRISA webpage and uncompress it.
    2) Launch it as follows
    
  `python mrisa/server.py`
  
  To perform a research, type
  
  `curl -X POST http://localhost:5000/search
    -H "Content-Type: application/json"
    -d '{
        "image_url":
            "http://placehold.it/350x150.png"
        }'`
        
   in a terminal. It returns a JSON containing the results for the reverse image search.
    

