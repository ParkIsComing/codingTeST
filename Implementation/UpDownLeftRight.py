size=int(input())
route = list(map(str,input().split()))

x=1
y=1

for i in range (len(route)):
    temp=route[i]
    if temp=='U':
        if x<=1:
            continue
        x-=1
    elif temp=='D':
        if x>=size:
            continue
        x+=1
    elif temp=='L':
        if y<=1:
            continue
        y-=1
    else:
        if y>=5:
            continue
        y+=1

print(x, y)


#모범답안1
'''
size=int(input())
x,y=1,1
plans=input().split()

#L,R,U,D에 따른 이동방향
dx=[0,0,-1,1]
dy=[-1,1,0,0]
move_types =['L','R','U','D']

for plan in plans: #
    for i in range(len(move_types)): #이렇게 방향별 움직이는 방식을 다르게 함
        nx=x+dx[i] #변화된 x값과 y값
        ny=y+dy[i]
    if nx < 1 or ny<2 or nx > size or ny > size: #그 값이 조건에서 벗어나면 버림
        continue
    x,y=nx,ny

print(x,y)

'''
