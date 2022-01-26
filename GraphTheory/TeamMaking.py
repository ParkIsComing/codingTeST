#맞음
n, m= map(int, input().split())

def find_parent(parent, x):
    if parent[x]!=x:
        parent[x]=find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a=find_parent(parent, a)
    b=find_parent(parent, b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

parent=[0]*(n+1)

for i in range(1, n+1):
    parent[i]=i

result=[]

for i in range(m):
    read_input=list(map(int, input().split()))
    if  read_input[0]==0:
        union_parent(parent,  read_input[1],  read_input[2])
    else: #if input[0]==1
        if parent[ read_input[1]]==parent[read_input[2]]:
            result.append('YES')
        else:
            result.append('NO')


for i in result:
    print(i)