# #틀림-아직 문법이 미숙함
n= int(input())

count=0

for i in range (n+1):
    for j in range (60):
        for k in range (60):
            if '3' in str(i) or str(j) or str(k): #틀림
                count+=1

print(count)

#모범답안
'''
h=int(input())
count=0

for i in range(h+1):
    for j in range (60):
        for k in range (60):
            if '3' in str(i) + str(j) + str(k): #문자열 그냥 이어서 확인. 문자열로 확인하니까 '3' 주의
                count+=1

print(count)

'''
