# parse and extract the comment counts from the XML data, compute the sum of
# the numbers in the file
# http://py4e-data.dr-chuck.net/comments_863164.xml
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter - ')
source = urllib.request.urlopen(url).read()
tree = ET.fromstring(source)

counts = tree.findall('.//count')
total = 0
for count in counts:
    total += int(count.text)

print(total)
