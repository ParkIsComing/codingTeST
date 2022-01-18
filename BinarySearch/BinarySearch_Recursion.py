from lib2to3.pytree import Node
from unittest import result


def binary_search(array, target, start, end):
    if start>end:
        return None
    mid = (start+end)//2
    if array[mid]==target:
        return mid
    elif array[mid]>target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

n, target= map(int, input().split()) #n은 원소개수, target은 찾고자하는 문자열
array=list(map(int, input().split()))

result=binary_search(array, target,0, n-1)
if result==None:
    print('원소가 존재하지 않습니다.')
else:
    print(str(result+1)+'번째')#인덱스가 0부터 시작이니까 return+1번째에 있는 target