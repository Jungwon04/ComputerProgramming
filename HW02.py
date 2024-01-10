vowels = "aeiouAEIOU"
s = input("문자열 입력: ")
vowel_count = 0

for c in s:
    if c in vowels:
        vowel_count += 1

print("입력 문자열:", s, ", 모음의 수:", vowel_count)
