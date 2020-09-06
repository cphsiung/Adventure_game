# You are to find all the <span> tags in the file and
# pull out the numbers from the tag and sum the numbers.
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

sum = 0
# Retrieve all of the spans
tags = soup('span')
for tag in tags:
    sum = sum + int(tag.contents[0])
print(sum)
