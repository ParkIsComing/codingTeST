from gettext import find


def find_parent(parent, x): #특정 원소가 들어있는 집합 찾아 루트노드 리턴
    if parent[x]!=x: #루트노드가 아니면 재귀적으로 호출
        parent[x]= find_parent(parent, parent[x]) 
    return parent[x]

def union_parent(parent, a, b): #두 원소가 속한 집합을 합치기
    a=find_parent(parent, a)
    b=find_parent(parent, b)
    if a<b: #두 루트노드 중 더 작은 걸 부모노드로
        parent[b]=a
    else:
        parent[a]=b

v,e=map(int, input().split()) #v는 노드 개수, e는 간선 개수
parent=[0]*(v+1) #노드0은 빼고 쓰니까 v+1개

for i in range(1, v+1): #처음엔 부모노드를 자기자신으로
    parent[i]=i

for i in range(e): #union 연산 수행
    a, b=map(int, input().split())
    union_parent(parent, a, b)

print('각 원소가 속한 집합:', end=' ') #각 원소가 속한 집합 출력
for i in range(1, v+1): 
    print(find_parent(parent, i), end=' ')

print()

print('부모 테이블:', end=' ') #부모 테이블 출력
for i in range(1, v+1):
    print(parent[i], end=' ')    
    
