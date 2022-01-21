#맞음
INF=int(1e9)

n,m=map(int, input().split()) #회사 개수 n, 경로 개수 m

graph=[[INF]*(n+1) for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

for _ in range(m): #경로 수만큼 for loop 돌리기
    a, b= map(int, input().split())
    graph[a][b]=1
    graph[b][a]=1
x,k=map(int, input().split()) #최종목적지 x, 거쳐갈 장소 k

for k in range(1, n+1):
    for a in range(1,n+1):
        for b in range(1, n+1):
            graph[a][b]=min(graph[a][b], graph[a][k]+graph[k][b])

if graph[1][k]+graph[k][x]>INF:
    print(-1)
else:
    print(graph[1][k]+graph[k][x])



