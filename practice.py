a = []
sum = 0
for i in range(7) : 
    i = int(input("정수를 입력하세요."))
    a.append(i)
    sum += i
average = sum/len(a)
print(average)