def _hash(s: str) -> int:
    h = 0
    for c in s:
        h += ord(c)
        h *= 17
        h %= 256

    return h


def part1(init_seq: list[str]) -> int:

    return sum(_hash(step) for step in init_seq)


def part2(init_seq: list[str]) -> int:
    boxes = [{} for _ in range(256)]
    for step in init_seq:
        if '=' in step:
            label, focal = step.split('=')
            h = _hash(label)
            boxes[h][label] = int(focal)
        else:
            label = step[:-1]
            h = _hash(label)
            boxes[h].pop(label, None)

    answer = 0
    for i, box in enumerate(boxes, 1):
        for slot, focal in enumerate(box.values(), 1):
            answer += i * slot * focal

    return answer


init_seq = input().split(',')
print(part1(init_seq))
print(part2(init_seq))
