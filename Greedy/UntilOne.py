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


#모범답안1
'''
n,k=map(int, input().split())
result=0

#n이 k이상이면 최대한 k로 나눠버리기 아니면 1빼고 계속 나누기
while n>=k:
    while n%k!=0:
        n-=1
        result+=1
    n//=k
    result+=1

#k보다 작아진 수는 n==1이 될 때까지 계속 1로 빼기
while n>1:
    n-=1
    result+=1

print(result)
'''


#모범답안2
'''
n,k=map(int, input().split())
result=0

while True:
    #n이 k로 나눠떨어지는 수 될 때까지 1씩 빼기
    target =(n//k)*k 
    #n-target만큼의 값은 1로 계속 빼야하는 부분이니까 그냥 result에 더해버리기
    result += (n-target) 
    n=target
    #n이 k보다 작을 때 while loop 탈출
    if n<k:
        break
    #n이 k로 나눠떨어지는 수가 됐으니 k로 나누기
    result+=1
    n//=k

result +=(n-1)
print(result)
'''



