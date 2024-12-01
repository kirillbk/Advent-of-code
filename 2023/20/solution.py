from sys import stdin
from collections import deque
from itertools import count
from copy import deepcopy
from math import lcm


def part1(graph: dict[str, list[str]], ff: dict[str, bool], conj: dict[str, dict[str, bool]]) -> int:
    hi = lo = 0
    q = deque()

    for _ in range(1000):
        lo += 1
        for dest in graph['broadcaster']:
            q.append((dest, False))

        while q:
            module, signal = q.popleft()

            if signal:
                hi += 1
            else:
                lo += 1

            if module in ff:
                if signal:
                    continue
                new_signal = not ff[module]
                ff[module] = new_signal
            elif module in conj:
                new_signal = not all(conj[module].values())
            else:
                continue

            for dest in graph[module]:
               if dest in conj:
                   conj[dest][module] = new_signal
               q.append((dest, new_signal))

    return lo * hi


def part2(graph: dict[str, list[str]], ff: dict[str, bool], conj: dict[str, dict[str, bool]]) -> int:
    # suppose conjunction module(last_module) connected to 'rx'
    for m, dests in graph.items():
        if 'rx' in dests:
            last_module = m
            break

    cycles = {}
    q = deque()

    for i in count(1):
        if len(cycles) == len(conj[last_module]):
            return lcm(*cycles.values())

        for dest in graph['broadcaster']:
            q.append((dest, False))

        while q:
            module, signal = q.popleft()

            if module in ff:
                if signal:
                    continue
                new_signal = not ff[module]
                ff[module] = new_signal
            elif module in conj:
                new_signal = not all(conj[module].values())

            for dest in graph.get(module, []):
                if dest in conj:
                    conj[dest][module] = new_signal
                if dest == last_module and new_signal and module not in cycles:
                    cycles[module] = i
                q.append((dest, new_signal))


graph: dict[str, list[str]] = {}
ff: dict[str, bool] = {}
conj: dict[str, list[str]] = {}

for line in stdin:
    module, dests = line.rstrip().split('->')
    module = module.rstrip()
    dest = map(str.strip, dests.split(','))

    if module.startswith('%'):
        module = module[1:]
        ff[module] = False
    elif module.startswith('&'):
        module = module[1:]
        conj[module] = {}
    graph[module] = list(dest)

for module, dests in graph.items():
    for dest in dests:
        if dest in conj:
            conj[dest][module] = False

print(part1(graph, ff.copy(), deepcopy(conj)))
print(part2(graph, ff.copy(), deepcopy(conj)))
