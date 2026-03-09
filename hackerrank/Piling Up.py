from collections import deque
import sys

def can_stack(blocks):
    dq = deque(blocks)
    last = 10**18
    while dq:
        left = dq[0]
        right = dq[-1]
        # both ends are valid choices (not larger than last)
        if left <= last and right <= last:
            # choose the larger to keep pile non-increasing
            if left >= right:
                dq.popleft()
                last = left
            else:
                dq.pop()
                last = right
        elif left <= last:
            dq.popleft()
            last = left
        elif right <= last:
            dq.pop()
            last = right
        else:
            return False
    return True

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    t = int(next(it))
    out_lines = []
    for _ in range(t):
        n = int(next(it))
        blocks = [int(next(it)) for _ in range(n)]
        out_lines.append("Yes" if can_stack(blocks) else "No")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()
