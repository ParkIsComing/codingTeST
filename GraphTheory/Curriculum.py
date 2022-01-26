#틀림

from collections import deque
import copy

n=int(input()) #노드 개수 받기
indegree= [0]*(n+1) #진입차수 모두 0으로 초기화
graph=[[] for i in range(n+1)] # 각 노드에 연결된 edge 정보를 담기 위한 연결 리스트

time=[0]*(n+1) # 각 강의 시간을 0으로 초기화 time[1]~time[n]만 사용

for i in range(1, n+1):
    data=list(map(int, input().split()))
    time[i]=data[0] #첫번째는 강의 시간
    #그다음 숫자부터 -1 나오기 전까지는 그 강의를 듣기 위해 선수학습 해야하는 강의 번호가 공백으로 구분되어 입력됨
    for x in data[1:-1]: 
        indegree[i]+=1
        graph[x].append(i)


def topology_sort():
    result=copy.deepcopy(time) #리스트 값을 복제할 때는 deepcopy()
    q=deque()

    for i in range(1, n+1):
        if indegree[i]==0:
            q.append(i) #큐를 사용하기 위한 deque 라이브러리

    while q: #큐가 빌때까지
        #큐에서 원소 꺼내기 ->  해당 원소와 열결된 노드의 진입차수 -1 -> 새롭게 진입차수가 0인 노드를 큐에 삽입 반복
        now=q.popleft()
        for i in graph[now]: #큐에서 꺼낸 노드와 연결된 간선들을 forloop 돌리면서 
            result[i]= max(result[i], result[now]+time[i]) #?
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)

    for i in range(1, n+1):
        print(result[i])

topology_sort()




