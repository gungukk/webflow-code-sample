import http.client
from datetime import datetime

conn = http.client.HTTPSConnection("api.webflow.com")

payload = "{\"domains\":[\"gunguks-marvelous-site.webflow.io\"]}"

headers = {
    'Authorization': "259a50776eb293ce1bc4d7e26858cd8d6729834fe7c37f0bee5679b9ed1849dc",
    'content-type': "application/json"
    }

conn.request("POST", "/sites/62aed8234580ec58e79e3f32/publish", payload, headers)

res = conn.getresponse()
data = res.read()

if res.status == 200: 
	print("Site has been successfully published at:", datetime.now())
else: 
	print (data.decode("utf-8"))

