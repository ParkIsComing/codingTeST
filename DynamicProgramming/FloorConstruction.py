n= int(input())

d=[0]*1001 

d[1]=1 #2*1 타일만 가능
d[2]=3 

for i in range(3, n+1): 
    d[i]=(d[i-1]+2*d[i-2])%79676

print(d[n])