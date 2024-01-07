from sys import stdin
from operator import mul
from functools import reduce


class Rule:
    def __init__(self, dest: str, key: str = None, op: str = None, val: int = None) -> None:
        self._dest = dest
        self._key = key
        self._value = val

        match op:
            case '>':
                self._rule = lambda part: part[self._key] > self._value
                self._range = self._value + 1, 4001
            case '<':
                self._rule = lambda part: part[self._key]  < self._value
                self._range = 1, self._value
            case _:
                self._rule = lambda _: True

    def apply(self, part: dict[str, int]) -> str | None:
        if self._rule(part):
            return self._dest
        return None

    def apply_range(self, part_range: dict[str, tuple[int, int]]) -> tuple[str | None, dict[str, tuple[int, int]] | None]:
        if self._key is None:
            rule_range = part_range.copy()
            for c in 'xmas':
                part_range[c] = 0, 0
            return self._dest, rule_range

        # l, r - intersection of rule range and part range
        x1, x2 = self._range
        y1, y2 = part_range[self._key]
        l = max(x1, y1)
        r = min(x2, y2)
        if l >= r:
            return None, None

        # range applied by rule
        rule_range = part_range.copy()
        rule_range[self._key] = l, r

        # range not applied by rule
        part_range[self._key] = 0, 0
        if l > y1:
            part_range[self._key] = y1, l
        elif r < y2:
            part_range[self._key] = r, y2

        return self._dest, rule_range


def part1(workflows: dict[str, list[Rule]], parts: list[dict[str, int]]) -> int:

    def apply_rules(workflow: str, part: dict[str, int]) -> bool:
        if workflow == 'A':
            return True
        if workflow == 'R':
            return False

        for rule in workflows[workflow]:
            next_workflow = rule.apply(part)
            if next_workflow:
                return apply_rules(next_workflow, part)

    answer = 0
    for part in parts:
        if apply_rules('in', part):
            answer += sum(part.values())

    return answer


def part2(workflows: dict[str, list[Rule]]) -> int:
    def solve(
            workflow: str,
            part_range: dict[str, tuple[int, int]],
            workflows: dict[str, list[Rule]]
        ) -> int:
        if workflow == 'A':
            ranges = (r - l for l, r in part_range.values())
            return reduce(mul, ranges)
        if workflow == 'R':
            return 0

        total = 0
        for rule in workflows[workflow]:
            next_workflow, rule_range = rule.apply_range(part_range)
            if next_workflow:
                total += solve(next_workflow, rule_range, workflows)
        return total

    part_range = {c: (1, 4001) for c in 'xmas'}
    return solve('in', part_range, workflows)


workflows_data, parts_data = stdin.read().split('\n\n')

workflows: dict[str, list[Rule]] = {}
for workflow_data in workflows_data.splitlines():
    new_rules = []
    name, rules = workflow_data.split('{')
    rules = rules[:-1].split(',')

    for i in range(len(rules) - 1):
        rule = rules[i].split(':')
        key, cond, val = rule[0][0], rule[0][1], rule[0][2:]
        dest = rule[1]

        new_rule = Rule(dest, key, cond, int(val))
        new_rules.append(new_rule)
    new_rules.append(Rule(rules[-1]))

    workflows[name] = new_rules

parts: list[dict[str, int]] = []
for part_data in parts_data.splitlines():
    new_part = {}
    for pair in part_data[1:-1].split(','):
        key, val = pair.split('=')
        new_part[key] = int(val)
    parts.append(new_part)

print(part1(workflows, parts))
print(part2(workflows))
