n, m=list(map(int, input().split()))
array=list(map(int, input().split()))
start=0
end=max(array)

result=0
while(start<=end):
  total=0
  mid=(start+end)//2
  for i in array:
    if i > mid:
      total+= i-mid
  if total < m: # 더 잘라야하는 경우
    end=mid-1
  else: #충분히 자른 경우
    result= mid #일단 이게 최대인지 모르니까 킵
    start=mid+1
  
print(result)



