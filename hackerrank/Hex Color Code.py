# Enter your code here. Read input from STDIN. Print output to STDOUT


import re
import sys

n = int(sys.stdin.readline())
hex_re = re.compile(r'#[0-9A-Fa-f]{3}(?:[0-9A-Fa-f]{3})?\b')

inside = False
for _ in range(n):
    line = sys.stdin.readline()
    i = 0
    L = len(line)
    while i < L:
        if not inside:
            # find next opening brace
            open_idx = line.find('{', i)
            if open_idx == -1:
                # no opening brace on the rest of the line; nothing to do
                break
            # move to the character after '{' and enter block
            i = open_idx + 1
            inside = True
        else:
            # we are inside a block; find closing brace
            close_idx = line.find('}', i)
            if close_idx == -1:
                # no closing brace on this line: search from i to end
                segment = line[i:]
                for m in hex_re.findall(segment):
                    print(m)
                # remain inside for next line
                break
            else:
                # search between i and close_idx
                segment = line[i:close_idx]
                for m in hex_re.findall(segment):
                    print(m)
                # move past '}' and exit block
                i = close_idx + 1
                inside = False

