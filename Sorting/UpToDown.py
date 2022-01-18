number=int(input())
array=[]
for i in range(number):
    array.append(int(input())) #자꾸 다른 언어할 때처럼 배열에 넣지말고 append!!

array=sorted(array,reverse=True)

for i in array: #배열 순서대로 출력할 거면 in range 안쓰고 그냥 in 배열
    print(i, end=' ')