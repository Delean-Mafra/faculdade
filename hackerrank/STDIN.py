import re

if __name__ == '__main__':
    n = int(input())
    lines = [input() for _ in range(n)]

    for line in lines:
        # Substitui apenas ' && ' por ' and ' e ' || ' por ' or '
        line = re.sub(r'(?<= )&&(?= )', 'and', line)
        line = re.sub(r'(?<= )\|\|(?= )', 'or', line)
        print(line)
