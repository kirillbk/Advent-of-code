# https://adventofcode.com/2024/day/17
# --- Day 17: Chronospatial Computer ---


def execute(a: int, b: int, c: int, program: list[int]) -> list[int]:
    combo = lambda x: a if x == 4 else b if x == 5 else c if x == 6 else x
    output = []
    ip = 0
    while ip < len(program) - 1:
        code, op = program[ip], program[ip + 1]
        match code:
            case 0:
                a = a >> combo(op)
            case 1:
                b = b ^ op
            case 2:
                b = combo(op) % 8
            case 3:
                if a:
                    ip = op
            case 4:
                b = b ^ c
            case 5:
                output.append(combo(op) % 8)
            case 6:
                b = a >> combo(op)
            case 7:
                c = a >> combo(op)
            case _:
                raise RuntimeError()
        if code != 3 or a == 0:
            ip += 2

    return output


def solution1(a: int, b: int, c: int, program: list[int]) -> str:
    output = execute(a, b, c, program)

    return ",".join(map(str, output))


def solution2(program: list[int]) -> int:
    def _dfs(a: int, i: int, program: list[int]) -> int | None:
        if i == -1:
            return a

        for x in range(8):
            x = (a << 3) + x
            if execute(x, 0, 0, program) == program[i:]:
                ans = _dfs(x, i - 1, program)
                if ans:
                    return ans

        return None

    return _dfs(0, len(program) - 1, program)


reg = (input().split(":")[1] for _ in range(3))
a, b, c = map(int, reg)
input()
program = input().split()[1].split(",")
program = list(map(int, program))

print(solution1(a, b, c, program))
print(solution2(program))
