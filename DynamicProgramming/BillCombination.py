#못품

n, m= map(int, input().split()) #n가지 종류 화폐, 구성하려는 금액 m원
array=[]

for i in range(n):
    array.append(int(input())) #화폐 종류 배열 array로 입력받기

d=[10001]*(m+1) #0원부터 m원까지 DP테이블의 각 원소로

d[0]=0
for i in range(n):
    for j in range(array[i], m+1):
        if d[j-array[i]]!=10001:
            d[j]=min(d[j], d[j-array[i]]+1) #사실 항상 저 min함수는 d[j]를 반환함

if d[m]!=10001:
    print(-1)
else:
    print(d[m])