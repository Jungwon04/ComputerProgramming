a = int(input("a를 입력해주세요."))
b = int(input("b를 입력해주세요."))
c = int(input("c를 입력해주세요."))
r1 = (-b + (b**2-4*a*c)**0.5)/(2*a)
r2 = (-b - (b**2-4*a*c)**0.5)/(2*a)

def root_calc(a, b, c):
    d = (b ** 2) - (4 * a * c)
    if d > 0:
        r1 = (-b + (d) ** 0.5) / (2 * a)
        r2 = (-b - (d) ** 0.5) / (2 * a)
        print(f"{r1:.4f} 또는 {r2:.4f} 입니다.")
    elif d == 0:
        r1 = -b / (2 * a)
        print(f"중근인 해는 {r1:.4f} 입니다.")
    else:
        print("허근입니다.")

root_calc(a, b, c)