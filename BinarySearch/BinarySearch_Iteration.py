def binary_search(array, target, start, end):
    while start <= end:
        mid=(start+end)//2
        if array[mid]==target:
            return mid
        elif array[mid]>target:
            end= mid-1
        else:
            start= mid+1
    return None #while loop 나올 때까지 return 없으면 그냥 찾는 값이 없는 경우
n, target=list(map(int, input().split()))
array= list(map(int,input().split()))

result=binary_search(array, target, 0, n-1)
if result==None:
    print('찾는 값이 없음')
else:
    print(result+1)