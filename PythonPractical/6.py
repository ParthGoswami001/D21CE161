from collections import OrderedDict
d = OrderedDict()
n = int(input())
for i in range(n):
    name = input()
    if name in d.keys():
        d[name] += 1
    else:
        d[name] = 1

print(len(d.keys()))
for x,y in d.items():
    print(y, end = ' ')