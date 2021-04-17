fname=input("Enter file name:")
fhand=open(fname)
counts=dict()
for line in fhand:
    if line.startswith("From "):
        stuff=line.split()
        stuff2=stuff[5].split(':')
        counts[stuff2[0]]=counts.get(stuff2[0],0)+1
for x,y in sorted(counts.items()):
    print(x,y)
