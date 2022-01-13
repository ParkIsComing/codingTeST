#반올림 round
#첫번째 인자는 실수형 데이터, 두번째 인자는 반올림하고자하는 위치-1
from collections import deque
from typing import Deque

a=123.456
print(round(a,2)) #123.456을 소수점 셋째 자리에서 반올림
print(round(a)) #두번째 인자 안 넣으면 소수점 첫째 자리에서 반올림


###리스트 자료형###

##빈 리스트 선언
a=list() #방법1
print(a)

a=[] #방법2
print(a)


##크기가 n이고 모든 값이 0으로 같은 리스트 초기화
n=10
a=[0]*n
print(a)


##리스트 인덱싱
a=[1,2,3,4,5]
print(a[-1]) #뒤에서 첫번째 원소 출력
print(a[-3]) #뒤에서 세번째 원소 출력


##리스트 슬라이싱
a=[1,2,3,4,5,6]
print(a[1:4]) #a[1]부터 a[3]까지 / [2, 3, 4]로 출력됨


##리스트 컴프리헨션
array=[i for i in range (20) if i %2 ==1] #0부터 19까지의 수 중에서 홀수만 포함하는 리스트
print(array)

array1=[i * i for i in range(1,10)] #1부터 9까지의 수의 제곱값을 포함하는 리스트
print(array) #결과: [1, 4, 9, 16, 25, 36, 49, 64, 81]

n, m =3, 4 #n*m 크기의 2차원 리스트 초기화
array = [[0]* m for _ in range (n)]
print(array) #결과: [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

'''
array=[[0]*m]*n은 잘못된 방법

'''


##리스트 관련 메소드
a=[1,4,3]
a.append(2) #a=[1, 4, 3, 2,]

a.sort() #오름차순 정렬
a.sort(reverse=True) #내림차순 정렬

a.reverse() #원소 뒤집기

a.insert(2,3) #인덱스 2에 3추가

print(a.count(1)) #리스트 원소 개수

a.remove(1) #값이 1인 데이터 하나 삭제


#425페이지

##인접행렬
INF= 999999999 #연결되지 않은 노드는 가중치를 INF로
graph=[[0,7,5], [7,0,INF],[5,INF,0]]
print(graph)

##인접리스트
graph=[[] for _ in range(3)]
graph[0].append((1,7))
graph[0].append((2,5))
graph[1].append((0,7))
graph[2].append((0,5))  #graph==[[1,7,[2,5]],[0,7],[0,5]]

##DFS(Depth Fisrt Search)
#1. 탐색 시작 노드를 스택에 삽입 후 방문 처리
#2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 노드를 스택에 넣고 방문처리, 없다면 스택에서 최상단 노드 꺼냄
#3. 2번의 과정을 더 이상 수행할 수 없을 때까지 방문
def dfs(graph, v, visited):
    visited[v]=True
    print(v, end=' ')
    for i in graph[v]:#노드 v와 연결된 노드를 다 확인하면서
        if not visited[i]: #False인 노드가 있으면 재귀
            dfs(graph, i, visited)

graph=[[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

visited=[False]*9

dfs(graph, 1, visited) #정의된 dfs함수 호출



##BFS(Breadth First Search)
#1. 탐색 시작 노드를 큐에 삽입하고 방문처리
#2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리
#3. 2번을 더 이상 수행할 수 없을 때까지 반복
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

#split, sep
s='3:10'
a,b=input().split(':') #콜론 ':' 기호를 기준으로 자른다.
print(a, b, sep=':') # 콜론 ':' 기호를 사이에 두고 값을 출력한다. sep = 분류기호(seperator)

s = 'abcd'
print(s[0:2]) #문자열 0번째 문자부터 1번째 문자까지 출력 -> ab
print(s[2:4]) #문자열 2번째 문자부터 3번째 문자까지 -> cd


#진수
a=20
print('%x'%a) #20이 16진수로 출력됨
n = int(input(), 16)      #입력된 값을 16진수로 인식해 변수 n에 저장
print('%o' % n)  #n 값을 8진수(octal) 형태 문자열로 출력

#유니코드
#chr()는 정수->문자(유니코드 문자), ord()는 문자->정수(유니코드 값)