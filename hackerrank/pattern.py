import re

if __name__ == "__main__":
    n = int(input())
    pattern = re.compile(r'^[789]\d{9}$')  # começa com 7,8 ou 9 e tem 10 dígitos

    for _ in range(n):
        number = input().strip()
        if pattern.match(number):
            print("YES")
        else:
            print("NO")
