def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid]==target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)


n=int(input())
array=list(map(int,input().split()))
array.sort()
print(array)
m=int(input())
finding_array=list(map(int, input().split()))

for i in finding_array:
    result = binary_search(array, i, 0, n-1)
    if result==None:
        print('no', end=' ')
    else:
        print('yes', end=' ')



#맞음

#방법2 - 계수정렬 활용
n=int(input())
array=[0]*1000000

for i in input().split(): #이렇게 input 바로 쓸 수도 있다!
    array[int(i)]=1

m=int(input())
x=list(map(int, input().split()))
for i in x:
    if array[i]==1:
        print('yes', end='')
    else:
        print('no', end=' ')

#방법3-set함수 활용
#단순히 array set에 x의 요소가 있는지 if i in array 검사하면 된다 
#이렇게 단순히 특정 데이터가 존재하는지 검사할 때 set() 사용
n= int(input())
array=set(map(int, input().split()))

m=int(input())
x=list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')