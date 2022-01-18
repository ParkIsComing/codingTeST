n= int(input())
array=[]

for i in range(n):
    input_data= input().split() #이름은 input_data[0] 점수는 input_data[1]로 들어감
    array.append((input_data[0], int(input_data[1])))

array=sorted(array, key=lambda student: student[1]) #key를 이용해 점수 기준으로 정렬

for student in array:
    print(student[0], end=' ')


