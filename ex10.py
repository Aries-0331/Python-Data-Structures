name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
m = dict()
for line in handle:
    if line.startswith('From') and not line.startswith('From:'):
        lst = line.split()
        time = lst[5]
        lst_time = time.split(':')
        m[lst_time[0]] = m.get(lst_time[0], 0) + 1
tup_lst = m.items()
for k, v in sorted(tup_lst):
    print(k, v)

    