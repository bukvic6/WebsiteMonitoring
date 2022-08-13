import time
import hashlib
from urllib.request import urlopen, Request

url = Request('https://www.blockchain.com/explorer',headers={'User-Agent': 'Mozilla/5.0'})

response = urlopen(url).read()

curHash = hashlib.sha224(response).hexdigest()
print("running")
time.sleep(10)
while True:
    try:
        response = urlopen(url).read()
        
        curHash = hashlib.sha224(response).hexdigest()
        
        time.sleep(30)
        
        response = urlopen(url).read()

        newHash = hashlib.sha224(response).hexdigest()
        
        if newHash == curHash:
            continue
    
        else:
            print("something shanged")

            response = urlopen(url).read()
            curHash = hashlib.sha224(response).hexdigest()
            time.sleep(30)
            continue
    
    except Exception as e:
        print("error")
