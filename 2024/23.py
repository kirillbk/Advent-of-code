# https://adventofcode.com/2024/day/23#part2
# --- Day 23: LAN Party ---

from collections import defaultdict
from sys import stdin


def solution1(network: defaultdict[set[str]]) -> int:
    triples = set()
    for u, links in network.items():
        for v in links:
            for x in network[v]:
                if x in links and (
                    u.startswith("t") or v.startswith("t") or x.startswith("t")
                ):
                    t = tuple(sorted((u, v, x)))
                    triples.add(t)

    return len(triples)


def solution2(network: defaultdict[set[str]]) -> str:
    # Bron–Kerbosch algorithm
    def _extend(clique: set[str], candidates: set[str], used: set[str]):
        if not candidates and not used:
            nonlocal max_clique
            if len(clique) > len(max_clique):
                max_clique = clique.copy()
        while candidates:
            v = candidates.pop()
            clique.add(v)

            neighbors = network[v]
            _extend(
                clique, candidates.intersection(neighbors), used.intersection(neighbors)
            )

            used.add(v)
            clique.remove(v)

    max_clique = set()
    _extend(set(), set(network.keys()), set())

    return ",".join(sorted(max_clique))


network = defaultdict(set)
for line in stdin:
    a, b = line.rstrip().split("-")
    network[a].add(b)
    network[b].add(a)

print(solution1(network))
print(solution2(network))
