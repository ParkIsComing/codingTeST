def find_parent(parent, x): #특정 원소가 속한 집합 찾아 루트노드 리턴
    if parent[x]!= x:
        parent[x]=find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b): #두 원소가 속한 집합 합치기
    a=find_parent(parent, a)
    b=find_parent(parent, b)

    if a<b:
        parent[b]=a
    else:
        parent[a]=b

v, e=map(int, input().split()) #노드, 간선 수 받기
parent=[0]*(v+1)    

edge=[] #모든 간선을 담을 리스트
result=0 #최종 비용을 담을 변수

for i in range(1, v+1): #처음에는 루트노드를 자기 자신으로 초기화
    parent[i]=i

for _ in range(e):#모든 간선에 대한 정보 받기
    a, b, cost=map(int, input().split())
    edge.append((cost, a, b)) #간선을 비용순으로 정렬하기 위해서 튜플의 첫 원소를 비용으로 설정

edge.sort()#간선을 비용순으로 정렬

for edge in edge: #간선을 하나씩 확인하면서 사이클을 형성하지 않는 경우에만 집합에 포함시키고 전체비용 증가시키기
    cost, a, b=edge
    if find_parent(parent, a)!= find_parent(parent,b):
        union_parent(parent, a,b)
        result+=cost
    
print(result)

    
     
     
     
