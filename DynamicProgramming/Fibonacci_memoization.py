#memoization은 top-down 방식에 국한되어 사용
d=[0]*100 #한번 계산된 결과를 memoization하기 위한(다시 계산하지 않기 위한) 리스트, 0으로 초기화

def fibo(x):
    if x==1 or x==2:
        return 1
    if d[x]!=0:
        return d[x]
    d[x]=fibo(x-1)+fibo(x-2) #한번 계산한 값은 넣어주기!
    return d[x]

print(fibo(99))
