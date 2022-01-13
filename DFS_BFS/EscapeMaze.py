from collections import deque

##BFS(Breadth First Search)
#1. 탐색 시작 노드를 큐에 삽입하고 방문처리
#2. 큐에서 노드를 꺼내(v) 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리
#3. 2번을 더 이상 수행할 수 없을 때까지 반복

'''
idea
(1,1)지점에서부터 bfs를 수행하여 모든 노드의 값을 거리 정보를 넣고
마지막에 maze[n-1][m-1] return

'''

'''
#bfs

from collections import deque
def bfs(graph, start, visited):
    queue=deque([start])
    visited[start]=True
    while queue:
        v=queue.popleft() #큐에서 원소 하나를 뽑아 출력
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

graph=[[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

visited=[False]*9
bfs(graph,1,visited)
'''

n, m=map(int, input().split())

maze=[]

for i in range(n):
    maze.append(list(map(int, input()))) #미로 정보 입력

dx=[0,0,-1,1]
dy=[1,-1,0,0]

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        for i in range(4): #큐에서 꺼낸 노드의 상하좌우 체크
            nx=x+dx[i]
            ny=y+dy[i]
            if 0>nx or nx>=n or 0>ny or ny>=m: #미로 밖은 제외. 0~n-1 0~m-1 범위에서 움직여야
                continue
            if maze[nx][ny]==0: #괴물이 있는 부분도 피해서
                continue
            if maze[nx][ny]==1:
                maze[nx][ny]=maze[x][y]+1 #다음 나아갈 곳에 현재의 최단거리 +1 값 넣기
                queue.append((nx,ny))

    return maze

print(bfs(0,0))


'''
maze[][] 최종 상태
[[3, 0, 5, 0, 7, 0], 
 [2, 3, 4, 5, 6, 7], 
 [0, 0, 0, 0, 0, 8],
 [14, 13, 12, 11, 10, 9], 
 [15, 14, 13, 12, 11, 10]]

'''




