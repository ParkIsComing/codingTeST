#행은 1~8, 열은 a~h
status = input()
row = int(status[1])
columm= int(ord(status[0])-ord('a'))#'a'도 아스키로 바꿔서 형변환

#경우의 수 (2,1),(-2,1),(2,-1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2) (row, columm)조합
steps=[(2,1),(-2,1),(2,-1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]

result=0

for step in steps: #in range로 하면 x
    row_now= row+steps[0]
    columm_now= columm+steps[1]
    if row_now>=1 and row_now<=8 and columm_now>=1 and columm_now<=8: #변화시킨 위치가 조건에 맞는지 확인
        result+=1

print(result)

#모범답안

input_data= input()
row=int(input_data[1]) #행 받기
column= int(ord(input_data[0]))-int(ord('a'))+1

steps=[(2,1),(-2,1),(2,-1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]

result=0
for step in steps: 
    next_row = row+step[0] #계속 위치 확인하고 걸러주는 for-loop 형태
    next_column=column+step[1]

    if 1<=next_row<=8 and 1<=next_column<=8:
        result+=1

print(result)