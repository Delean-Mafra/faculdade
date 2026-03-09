import re
import sys

n = int(sys.stdin.readline())
pattern = re.compile(r'^[789]\d{9}$')

for _ in range(n):
    s = sys.stdin.readline().strip()
    print("YES" if pattern.match(s) else "NO")
