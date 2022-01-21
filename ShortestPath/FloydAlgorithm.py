INF=int(1e9)

n=int(input())
m=int(input())

graph=[[INF]*(n+1) for _ in range(n+1)]
for a in range(1, n+1): #자기 자신에서 자기 자신으로 가는 노드는 비용 0으로 세팅
    for b in range(1, n+1):
        if a==b:
            graph[a][b]=0

for _ in range(m):
    a, b, c=map(int, input().split())
    graph[a][b]=c #시작 a 도착 b 비용 c

for k in range(1, n+1): #노드 k를 거쳐가는 경우
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b]= min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b]==INF:
            print("INFINITY",end=" ")
        else:
            print(graph[a][b], end=" ")
    print()
