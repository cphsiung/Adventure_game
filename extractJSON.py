# parse and extract the comment counts from the JSON data, compute the
# sum of the numbers in the file
# http://py4e-data.dr-chuck.net/comments_863165.json
import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter - ')
source = urllib.request.urlopen(url).read()
info = json.loads(source)

sum = 0
i = 0
while i < len(info['comments']):
    sum += info['comments'][i]['count']
    i += 1
print(sum)
