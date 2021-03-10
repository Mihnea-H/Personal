
f = open("read.txt","r")
n = int(f.readline())
v = []
v.append([])
for x in range(1,n+1):   # initializare matrice muchii
    aux = f.readline().strip().split(",")
    v.append([])
    v[x] = []
    v[x].append(int(0))
    v[x].append(int(aux[0]))
    for y in range(1,n):
        v[x].append(int(aux[y]))
st = int(f.readline())
sp = int(f.readline())

f = open("write.txt", "w")

ls = []
viz = []
for x in range(1,n+2): # initializare lista de noduri
    ls.append(0)
    viz.append(0)
ls[1] = 1
viz[1] = 1
for i in range(1,n): # parcurgerea matrici si alegera muchiei cea mai scurta
    for j in range(1,n+1):
        if ( v[ls[i]][j] < v[ls[i]][ls[i+1]] or ls[i+1]==0 ) and viz[j] == 0 and j != 1 and j != ls[i]:
            ls[i+1] = j
    viz[ls[i+1]] = 1

f.write(str(n)+"\n") # print
for i in range(1,n):
    f.write(str(ls[i])+",")
f.write(str(ls[n])+"\n")

sumi = 0    # caluclare lungime drum
for i in range(1,n):
    sumi = sumi + v[ls[i]][ls[i+1]]
sumi = sumi + v[ls[n]][ls[1]]
f.write(str(sumi)+"\n")


ls = []     #re initializare
viz = []
for x in range(1,n+2):
    ls.append(0)
    viz.append(0)
ls[1] = st
viz[st] = 1
ok=0
for i in range(1,n):    # parcurgere a matrici si cautarea drumuiui cel mai scurt
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
for i in range(1,n+1): # caluclare lungime drum
    nr=nr+1
    if ls[i]==sp:
        break
    sumi = sumi + v[ls[i]][ls[i + 1]]
sumi = sumi + v[ls[i]][ls[st]]


f.write(str(nr)+"\n") # print

for i in range(1,nr):
    f.write(str(ls[i])+",")
f.write(str(ls[nr])+"\n")
f.write(str(sumi))