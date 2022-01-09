#배열의 크기:n, 숫자가 더해지는 횟수:m, 연속으로 더할 수 있는 최대 횟수:k
n,m,k=map(int,input().split())
data=list(map(int,input().split()))

data.sort()
first=data[n-1]
second=data[n-2]


#count는 큰 수를 더하는 횟수
count=int(m/(k+1)*k)
count+=m%(k+1)

result=0
result=first*count
result+=second*(m-count)

print(result)