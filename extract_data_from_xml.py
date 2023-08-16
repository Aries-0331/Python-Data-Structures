import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

uh = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_1872140.xml", context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
print(data.decode())
tree = ET.fromstring(data)

sum = 0
results = tree.findall("./comments/comment/count")
for item in results:
    sum = sum + int(item.text)
print(sum)