from collections import deque


v,e = map(int, input().split()) 
indegree= [0]*(v+1) #모든 노드의 진입차수는 0으로 초기화
graph=[[] for i in range(v+1)] #각 노드에 연결된 간선 정보를 담는 연결 리스트 초기화

for _ in range(e):
    a, b= map(int, input().split())
    graph[a].append(b) #정점 a에서 b로 이동가능하다는 뜻
    indegree[b]+=1 #정점 b의 진입차수 +1

def topology_sort():
    result = [] #알고리즘 수행 결과를 담을 리스트
    q=deque() #큐를 사용하기 위한 deque 

    for i in range(1, v+1): #처음에는 진입차수가 0인 노드를 큐에 삽입
        if indegree[i]==0:
            q.append(i)

    while q: #큐가 빌때까지 
        now=q.popleft() #큐에서 원소 꺼내기 ->  해당 원소와 열결된 노드의 진입차수 -1 -> 새롭게 진입차수가 0인 노드를 큐에 삽입 반복
        result.append(now)
        for i in graph[now]:
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)
    
    for i in result: #위상 정렬 수행의 결과 출력
        print(i, end=' ')

topology_sort()
