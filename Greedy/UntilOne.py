# 나뉘는 수 n, 나누는 수 k
n,k=map(int,input().split())

count=0

while n!=1:
    if n%k==0:
        n=n//k
    else:
        n-=1
    count+=1


print(count)