n, k=map(int, input().split())

array_A=list(map(int, input().split()))
array_B=list(map(int, input().split()))

array_A=sorted(array_A)
array_B=sorted(array_B, reverse=True)

for i in range(k):
    if array_A[i]<array_B[i]:
        array_A[i], array_B[i]=array_B[i],array_A[i]
    else:
        break

print(sum(array_A))