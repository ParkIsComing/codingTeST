#맞음
import sys
array=list(map(int, sys.stdin.readline().rstrip()))

result=array[0]

for i in range(1,len(array)):
    result= max(result+array[i], result*array[i])

print(result)
