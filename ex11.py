import re
try:
    fd = open("regex.txt", "r")
except:
    print('open file failed')
data = fd.read()
fd.close()
lst = re.findall('[0-9]+', data)
print(lst)
sum = 0
for num in lst:
    sum = sum + int(num)
print(sum)