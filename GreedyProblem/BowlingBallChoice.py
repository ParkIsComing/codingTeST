#맞음
n, m=map(int, input().split())
array=list(map(int, input().split()))

array.sort()
array1=list(set(array))
result=0
for i in array:
    if i==array[-1]:
        break
    n= array.count(i)
    result+=n*(len(array)-n)
    array.remove(i)

print(result)
