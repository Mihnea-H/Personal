
f = open("read.txt","r")
n = int(f.readline())
v = []
v.append([])
for x in range(1,n+1):
    aux = f.readline().strip().split(",")
    v.append([])
    v[x] = []
    v[x].append(int(0))
    v[x].append(int(aux[0]))
    for y in range(1,n):
        v[x].append(int(aux[y]))
st = int(f.readline())
sp = int(f.readline())
ls = []
viz = []
for x in range(1,n+2):
    ls.append(0)
    viz.append(0)
ls[1] = 1
viz[1] = 1
for i in range(1,n):
    for j in range(1,n+1):
        if ( v[ls[i]][j] < v[ls[i]][ls[i+1]] or ls[i+1]==0 ) and viz[j] == 0 and j != 1 and j != ls[i]:
            ls[i+1] = j
    viz[ls[i+1]] = 1

print(str(n))
for i in range(1,n):
    print(str(ls[i])+",",end="")
print(str(ls[n]))
sumi = 0
for i in range(1,n):
    sumi = sumi + v[ls[i]][ls[i+1]]
sumi = sumi + v[ls[n]][ls[1]]
print(sumi)


ls = []
viz = []
for x in range(1,n+2):
    ls.append(0)
    viz.append(0)
ls[1] = st
viz[st] = 1
ok=0
for i in range(1,n):
    j = 0
    for j in range(1,n+1):
        if ( v[ls[i]][j] < v[ls[i]][ls[i+1]] or ls[i+1]==0 ) and viz[j] == 0 and j != ls[i]:
            ls[i+1] = j
            if j == sp:
                ok=1
                break
    viz[ls[i + 1]] = 1
    if j == sp and ok == 1:
        break
nr=0
sumi=0
i=0
for i in range(1,n+1):
    nr=nr+1
    if ls[i]==sp:
        break
    sumi = sumi + v[ls[i]][ls[i + 1]]
sumi = sumi + v[ls[i]][ls[st]]
print(nr)

for i in range(1,nr):
    print(str(ls[i])+",",end="")
print(str(ls[nr]))
print(sumi)