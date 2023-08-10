name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
m = dict()
for line in handle:
    if line.startswith('From') and not line.startswith('From:'):
        tmp = line.split()
        m[tmp[1]] = m.get(tmp[1], 0) + 1

committer = None
times = None

for k, v in m.items():
    if committer == None or v > times:
        committer = k
        times = v
print(committer, times)