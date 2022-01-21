#top-down은 큰 문제를 해결하기 위해 작은 문제를 호출
#재귀함수를 이용해 다이나믹 프로그래밍 소스 코드 작성

d=[0]*100

def pibo(x):
    print('f(' + str(x) + ')', end=' ') #호출되는 함수 확인하는 코드
    if x==1 or x==2:
        return 1
    if d[x]!=0:
        return d[x]
    d[x]=pibo(x-1)+pibo(x-2)
    return d[x]

pibo(6)