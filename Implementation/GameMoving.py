#무한룹..
n,m=map(int, input().split()) #맵 크기 받기

x, y, direction = map(int, input().split()) # 좌표, 보고있는 현방향 받기
# 북0, 동1, 남2, 서3

map=[[0]*m for _ in range(n)] #m*n
visited=[[0]*m for _ in range(n)] #방문하지 않았으면 0, 방문했으면 1

for i in range(n):
    map.append(list(map(int, input().split())))


move=[(-1,0), (0,-1), (1,0), (0,1)]
global count
count=0
while True:
    turn_count=0
    
    for i in range (4):
        turn_count+=1
        next_x= x+move[i]
        next_y= y+move[i]

        if next_x!=1 and next_y!=1 and visited[next_x][next_y]!=1:
            x= next_x
            y=next_y
            visited[x][y]=1
            direction=i
            count+=1
            continue

        back_x=x-move[direction[0]]
        back_y=y-move[direction[1]]

        if map[back_x][back_y]==1:
            print(visited.count(1))
            break

print(count)


#모범 답안
n,m=map(int, input().split()) #행, 열 바꾸지말기..
d=[[0]*m for _ in range(n)] #d[]는 방문한 좌표를 처리하기 위한 리스트(방문시 1)
x, y, direction = map(int, input().split())
d[x][y]=1 #시작좌표 방문 처리

array=[] #바다인지 육지인지 맵정보 저장
for i in range(n):
    array.append(list(map(int, input().split())))#이렇게 행렬 받음

dx=[-1,0,1,0] #서, 남, 동, 북 순 x좌표 변화값
dy=[0, 1, 0, -1] #서, 남, 동, 북 순 y좌표 변화값

def turn_left():
    global direction
    direction-=1 #왼쪽으로 90도 회전해서 바라보기
    if direction==-1:
        direction=3


count= 1 #방문한 칸 수
turn_time=0
while True:
    turn_left()
    nx=x+dx[direction]
    ny=y+dy[direction]

    #방문한 적 없고 육지인 경우
    if d[nx][ny]!=1 and array[nx][ny]!=1:
        d[nx][ny]=1 #방문 처리
        x=nx #좌표값 변경
        y=ny 
        count +=1 
        turn_time=0 #돈 횟수 리셋
        continue
    #방문한 적 있거나 바다인 경우
    else:
        turn_time+=1

    if turn_time==4: #현재 보는 방향에서 네 방향 다 못가는 거 확인한 경우
        nx=x-dx[direction] #뒤로 가야
        ny=y-dy[direction]
        if array[nx][ny]==0:
            x=nx
            y=ny
        else:#뒤로 가는게 바다일 때 -> 실행 끝내는 시점
            break
        turn_time=0

    
print(count)