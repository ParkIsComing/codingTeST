#맞음
n= int(input())
fear=list(map(int, input().split()))

fear.sort()
a=[]
num=0


for i in range(len(fear)):
    a.append(fear[i])
    if fear[i]==len(a):
        a.clear()
        num+=1
        continue
    

print(num)


