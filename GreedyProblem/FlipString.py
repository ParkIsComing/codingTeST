#맞음
import sys
array=list(map(int, sys.stdin.readline().rstrip()))


a=array[0]
count=1

for i in range(1, len(array)):
    if a!=array[i]:
        a=array[i]
        count+=1
        print(count)

print(count//2)   

