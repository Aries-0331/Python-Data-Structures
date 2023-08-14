import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urllib.request.urlopen("http://py4e-data.dr-chuck.net/known_by_Emilija.html", context=ctx).read()
times = 7
while times > 0:
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    html = urllib.request.urlopen(tags[17].get('href', None), context=ctx).read()
    times -= 1
print(tags[17].contents[0])