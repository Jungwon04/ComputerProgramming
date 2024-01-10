s = input("문자열 입력: ")

for i in range(len(s)):
    rotated_s = s[i:] + s[:i]
    print(rotated_s)
