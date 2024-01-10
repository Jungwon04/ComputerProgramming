num = input("양의 정수를 입력하세요: ")
reversed_num = ""

for d in num:
    reversed_num = d + reversed_num

print("입력 값:", num, ", 역순의 값:", int(reversed_num))
