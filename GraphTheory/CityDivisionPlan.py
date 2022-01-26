#틀린 부분 체크(line 39)

def find_parent(parent, x):
    if parent[x]!=x:
        parent[x]=find_parent(parent, parent[x])
    return parent[x]
def union_parent(parent, a,b):
    a=find_parent(parent, a)
    b=find_parent(parent, b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b


n, m=map(int, input().split()) #n은 집의 개수, m은 길의 개수
parent=[0]*(n+1)

edges=[]
result=0 #최종 비용 담는 변수

for i in range(1, n+1):
    parent[i]=i

for _ in range(m):
    a, b, cost= map(int,input().split())
    edges.append((cost, a,b)) #간선을 비용순으로 정렬하기 위해 cost를 맨앞에

    edges.sort()

highest_cost=0
for edge in edges:
    cost, a, b= edge
    if find_parent(parent, a)!= find_parent(parent, b):
        union_parent(parent, a,b)
        result+=cost
        highest_cost=cost

# highest_cost=edges[m-1][0]
# 최소 신장 트리에 포함되는 간선 중에서! 가장 비용이 큰 간선!이니까
# 이렇게 구하면 안되고 위의 if문 아래로 넣어야함.

print(result-highest_cost)

