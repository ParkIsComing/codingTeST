import heapq
import sys
input=sys.stdin.readline
INF=int(1e9)

n, m=map(int, input().split()) #노드 개수, 간선 개수 입력받기
start=int(input()) #시작 노드 입력받기
graph=[[] for i in range(n+1)] #각 노드와 연결되 있는 노드 정보 담는 리스트
distance=[INF]*(n+1) #거리는 모두 무한으로 초기화

for _ in range(m): #모든 간선 정보 받기
    a,b,c=map(int, input().split()) #노드 a에서 노드 b까지 거리 c
    graph[a].append((b,c)) 

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start)) #큐에 시작 노드를 거리 0으로 넣기 첫번째 원소가 거리, 두번째 원소가 노드임
    distance[start]=0
    while q: #큐가 비어있지 않은 한
        dist, now= heapq.heappop(q) #최단거리 노드 빼내기 (거리, 노드)로 담았었음
        if distance[now] < dist: #이게 True면 이미 처리된 노드라는 것. 그러면 이 노드는 무시
            continue
        for i in graph[now]: #현재 노드와 연결된 인접 노드 확인
            cost= dist+i[1]
            if cost< distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q, (cost,i[0]))

dijkstra(start)

for i in range(n+1):
    if distance[i]==INF:
        print("INFINITY")
    else:
        print(distance[i])
