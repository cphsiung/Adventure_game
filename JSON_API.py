# The program will prompt for a location, contact a web service and retrieve
# JSON for the web service and parse that data, and retrieve the first place_id
# from the JSON.
import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://py4e-data.dr-chuck.net/json?'
address = 'National Institute of Technology Jalandhar'

url = serviceurl + urllib.parse.urlencode({"address": address, 'key': 42})
source = urllib.request.urlopen(url)
data = source.read().decode()
js = json.loads(data)
print(js['results'][0]['place_id'])
