import sys
input=sys.stdin.readline
INF=int(1e9)#무한으로 씀

n, m=map(int, input().split()) #노드 개수 n, 간선 개수 m받기
start=int(input()) #시작 노드 번호 받기
graph=[[] for i in range(n+1)] # 각 노드와 연결되어 있는 노드에 대한 정보 담는 리스트. 1부터 담음
visited=[False]*(n+1) #처음엔 다 미방문으로
distance=[INF]*(n+1) #처음엔 최단거리 테이블을 다 무한으로

for _ in range(m):
    a,b,c=map(int, input().split()) #노드 a에서 노드 b로 가는 비용이 c다
    graph[a].append((b,c))

print(graph)

def get_smallest_node():
    min_value=INF
    index=0 #가장 최단 거리가 짧은 노드를 저장하는 index
    for i in range(1, n+1): #노드 1부터 n까지 돌면서
        if distance[i] < min_value and not visited[i]: #노드 i의 거리가 min_value보다 작고 노드 i가 방문하지 않은 노드이면
            min_value=distance[i] #min_value를 distance[i]로 갱신하고
            index=i #가장 최단거리가 짧은 노드(index)를 i로 갱신
    return index #for loop 다 돌면 indext리턴

def dijkstra(start):
    distance[start]=0
    visited[start]=True #시작노드 방문처리
    for j in graph[start]:
        distance[j[0]]=j[1]
    for i in range(n-1): #시작노드를 제외한 n-1개의 노드에 대해 for loop
        now=get_smallest_node() # 최단거리가 가장 짧은 노드를 꺼내 방문 처리
        visited[now]=True
        for j in graph[now]: #현재 노드와 연결된 다른 노드 확인
            cost=distance[now]+j[i]
            if cost < distance[j[0]]: #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                distance[j[0]]=cost

dijkstra(start) #다익스트라 알고리즘 수행

for i in range(1, n+1):
    if distance[i]==INF: #도달할 수 없는 경우
        print("INFINITY")
    else: #도달할 수 있는 경우 거리 출력
        print(distance[i])