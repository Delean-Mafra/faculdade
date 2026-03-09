import re
import email.utils

# regex para validar o e-mail
pattern = re.compile(r'^[a-zA-Z][\w\.-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$')

n = int(input())
for _ in range(n):
    line = input().strip()
    name, addr = email.utils.parseaddr(line)
    if pattern.match(addr):
        print(email.utils.formataddr((name, addr)))
