#방법1-min함수 이용
#첫번째줄에서 행이 개수 n, 열의 개수 m 입력 받음
n, m=map(int, input().split())

result=0

for i in range (n):
    row=list(map(int,input().split()))
    min_value=min(row)
    #현재 result랑 min_value 비교해서 큰 걸 result로
    result=max(result, min_value)

print(result)
    

'''
#방법2
n,m=map(int, input().split())
result=0
for i in range(n):
    data=list(map(int, input().split()))
    min_value=10001
    for a in data:
        min_value= min(min_value, a)
    result= max(min_value, result)

print(result)
'''
