#반올림 round
#첫번째 인자는 실수형 데이터, 두번째 인자는 반올림하고자하는 위치-1
from cmath import pi
from collections import deque
import imp
from typing import Deque

a=123.456
print(round(a,2)) #123.456을 소수점 셋째 자리에서 반올림 이건 만약에 값이 0.00이면 0.0으로 나옴
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

#heapq - 우선순위큐(최소힙) 구현
import heapq

def heapsort(iterable):
    h=[]
    result=[]
    for value in iterable:
        heapq.heappush(h, value) #힙에 value를 차례대로 삽입
    for i in range(len(h)):
        result.append(heapq.heappop(h)) # 힙에 삽입된 거 차례대로 빼서 리스트 삽입
    return result

result= heapsort([1,3,5,7,9,2,4,6,8,0])
print(result) #디폴트는 최소힙이라서 결과는 [0,1,2,3,4,5,6,7,8,9]

#heapq- 우선순위큐(최대힙) 구현
def heapsort2(iterable):
    h=[]
    result=[]
    for value in iterable:
        heapq.heappush(h, -value) #힙에 원소를 삽입하기 전 잠시 부호를 반대로 바꿨다가
    for i in range(len(h)):
        result.append(-heapq.heappop(h)) #뺄때 원래 부호로 되돌림
    return result

result= heapsort([1,3,5,7,9,2,4,6,8,0])
print(result) 


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
a,b=s.split(':') #콜론 ':' 기호를 기준으로 자른다.
print(a, b, sep=':') # 콜론 ':' 기호를 사이에 두고 값을 출력한다. sep = 분류기호(seperator)

s = 'abcd'
print(s[0:2]) #문자열 0번째 문자부터 1번째 문자까지 출력 -> ab
print(s[2:4]) #문자열 2번째 문자부터 3번째 문자까지 -> cd


#진수
a=20
print('%x'%a) #20이 16진수로 출력됨
print('%o' % a)  #n 값을 8진수(octal) 형태 문자열로 출력

#유니코드
#chr()는 정수->문자(유니코드 문자), ord()는 문자->정수(유니코드 값)

#반올림
#format(수,".2f") 소수점 아래 2번째짜리까지 
#정수값 0은 False(거짓)로 평가되고, 그 외의 값들은 모두 True(참)로 평가된다.
n=True
print(bool(n)) #n==0이면 False 아니면 True

##정렬
#선택 정렬
array=[7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index=i
    for j in range(i+1, len(array)):
        if array[min_index]>array[j]:
            min_index=j
    array[min_index], array[i]= array[i], array[min_index]

print(array)

#삽입 정렬
array=[7,5,9,0,3,1,6,2,4,8]
for i in range(1, len(array)):#첫번째꺼는 처음부터 정렬 되어있음
    for j in range(i, 0, -1):#인덱스 i부터 1까지 감소하며 반복
        if array[j] < array[j-1]:
            array[j], array[j-1]= array[j-1], array[j]
        else:#자기보다 작은 데이터를 만나면 거기서 멈춤
            break

print(array)

#퀵 정렬1
array=[7,5,9,0,3,1,6,2,4,8]
def quick_sort(array):
    if len(array)<=1:
         return array
        
    pivot=array[0]#첫번째 원소를 피봇으로 함
    tail=array[1:] #array[1]~ 즉 리스트에서 피봇을 제외한 모든 요소들
    
    left_side = [x for x in tail if x<= pivot]
    right_side=[x for x in tail if x>pivot]

    return quick_sort(left_side)+[pivot]+quick_sort(right_side) #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고 전체 리스트를 반환


print(quick_sort(array))

#퀵정렬2
array=[7,5,9,0,3,1,6,2,4,8]

def quick_sort2(array, start, end):
    if start >=  end:#원소가 1개면 종료
        return
    pivot= start
    left=start+1
    right=end
    while left <= right:
        while left <= end and array[left]<= array[pivot]:
            left+=1
        while right>  start and array[right] >=array[pivot]:
            right-=1
        if left >right:
            array[right], array[pivot]= array[pivot],array[right]
        else:
            array[left],array[right]=array[right],array[left]
        
    quick_sort2(array, start, right-1)
    quick_sort2(array, right+1, end)


quick_sort2(array, 0, len(array)-1)
print(array)

#계수 정렬
array=[7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
count=[0]* (max(array)+1) #정렬할 배열의 모든 요소의 범위를 포함하는 리스트 선언

for i in range(len(array)):
    count[array[i]]+=1 #각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)):#리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end=' ')#띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력

#파이썬의 정렬 라이브러리
array=[7,5,9,0,3,1,6,2,4,8]
result= sorted(array) #sorted()는 리스트 자료형으로 반환
print(result)

array=[7,5,9,0,3,1,6,2,4,8]
array.sort()#정렬된 리스트 별도로 반환x 내부 원소가 바로 정렬됨
print(array)

#sorted()나 sort()는 key를 매개변수로 입력받을 수 있음
array=[('banana', 2), ('사과',5),('당근',3)]
def setting(data):
    return data[1]
result= sorted(array, key=setting)
print(result)

#빠르게 입력받기 readline()
import sys
input_data=sys.stdin.readline().rstrip()
print(input_data)

#3항연산
a,b,c=1,2,3
biggest= (a if a>b else b) if ((a if a>b else b)>c) else c