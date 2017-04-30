happylist=[]

with open('happynumbers.txt') as h:
    line = h.readline()
    while line:
        happylist.append(int(line))
        line = h.readline()


primeslist=[]

with open('primenumbers.txt') as p:
    line=p.readline()
    while line:
        primeslist.append(int(line))
        line = p.readline()

overlap=[]

for item in happylist:
    if item in primeslist:
        overlap.append(item)

print(overlap)