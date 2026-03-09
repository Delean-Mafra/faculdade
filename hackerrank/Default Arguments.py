class EvenStream:
    def __init__(self):
        self.current = 0

    def get_next(self):
        val = self.current
        self.current += 2
        return val


class OddStream:
    def __init__(self):
        self.current = 1

    def get_next(self):
        val = self.current
        self.current += 2
        return val


def print_from_stream(n, stream=None):
    if stream is None:
        stream = EvenStream()
    for _ in range(n):
        print(stream.get_next())


if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        name, n = input().split()
        n = int(n)
        if name == "even":
            print_from_stream(n)
        else:
            print_from_stream(n, OddStream())
