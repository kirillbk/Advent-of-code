# https://adventofcode.com/2024/day/22
# --- Day 22: Monkey Market ---

from collections import defaultdict
from sys import stdin

MOD = 16777216


def next_secret(n: int) -> int:
    a = ((n << 6) ^ n) % MOD
    b = ((a >> 5) ^ a) % MOD
    c = ((b << 11) ^ b) % MOD

    return c


def solution1(numbers: list[int]) -> int:
    ans = 0
    for n in numbers:
        for _ in range(2000):
            n = next_secret(n)
        ans += n

    return ans


def solution2(numbers: list[int]) -> int:
    buyers = []
    for n in numbers:
        price = [
            n % 10,
        ]
        change = [
            0,
        ]
        for _ in range(2000):
            nn = next_secret(n)
            price.append(nn % 10)
            change.append(nn % 10 - n % 10)
            n = nn
        buyers.append((price, change))

    seq_hash = defaultdict(int)
    for price, change in buyers:
        viewed = set()
        for i in range(1, len(change) - 3):
            window = tuple(change[i] for i in range(i, i + 4))
            if window not in viewed:
                seq_hash[window] += price[i + 3]
                viewed.add(window)

    return max(seq_hash.values())


numbers = [int(line) for line in stdin]
print(solution1(numbers))
print(solution2(numbers))
