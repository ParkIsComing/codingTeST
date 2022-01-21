import heapq
import sys

input=sys.stdin.readline

INF=int(1e9)
n, m, start= map(int, input().split()) #도시개수 n, 통로 개수 m, 메시지 보내는 도시 c

graph=[[] for i in range(n+1)]
distance=[INF] * (n+1)


for _ in range(m):
    a,b,c=map(int, input().split())
    graph[a].append((b,c))

def dijkstra(c):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist, now=heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

time=0
count=0

for d in distance:
    if d!= INF:
        count+=1
        time=max(time, d)
    


print(count-1, time) #메시지 받는 도시 수에서 자기 자신이 받는 경우 제외