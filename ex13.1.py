import urllib.request
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

data = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_1872141.json", context=ctx).read()
js = json.loads(data)
sum = 0
for item in js["comments"]:
    sum = sum + int(item["count"])
    
print(sum)