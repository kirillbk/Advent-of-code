# --- Day 9: Disk Fragmenter ---


def solution1(disk_map: list[int]) -> int:
    l = 0
    r = len(disk_map) - 1
    disk_map = disk_map.copy()
    disk = []
    while l <= r:
        if l % 2:
            size = min(disk_map[l], disk_map[r])
            id = r // 2
            for _ in range(size):
                disk.append(id)
            disk_map[l] -= size
            disk_map[r] -= size
            if disk_map[l] == 0:
                l += 1
            if disk_map[r] == 0:
                r -= 2
        else:
            id = l // 2
            for _ in range(disk_map[l]):
                disk.append(id)
            l += 1

    return sum(i * disk[i] for i in range(len(disk)))


def solution2(disk_map: list[int]) -> int:
    offsets = [0] * len(disk_map)
    for j in range(1, len(disk_map)):
        offsets[j] = offsets[j - 1] + disk_map[j - 1]

    disk_map = disk_map.copy()
    disk = [0] * sum(disk_map)

    for i in range(len(disk_map) - 1, 0, -2):
        j = 1
        while j < i and disk_map[i] > disk_map[j]:
            j += 2
        if j > i:
            j = i
        id = i // 2
        for k in range(offsets[j], offsets[j] + disk_map[i]):
            disk[k] = id
        offsets[j] += disk_map[i]
        disk_map[j] -= disk_map[i]
        disk_map[i] = 0

    return sum(i * disk[i] for i in range(len(disk)))


disk_map = list(map(int, input()))

print(solution1(disk_map))
print(solution2(disk_map))
