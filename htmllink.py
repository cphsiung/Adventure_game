# Find the link at position 18 (the first name is 1).
# Follow that link. Repeat this process 7 times. The answer is the last name
# that you retrieve.
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
repeat = int(input('Enter times to repeat:'))
start = int(input('Enter link position:'))

for i in range(repeat):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    count = 0
    for tag in tags:
        count = count + 1
        if count > start:
            break
        url = tag.get('href', None)

print(url)
