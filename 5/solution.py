# seeds: 79 14 55 13

# seed-to-soil map:
# 50 98 2
# 52 50 48

# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15

# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4

# water-to-light map:
# 88 18 7
# 18 25 70

# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13

# temperature-to-humidity map:
# 0 69 1
# 1 0 69

# humidity-to-location map:
# 60 56 37
# 56 93 4

from sys import stdin


class Solution:
    def __init__(self) -> None:
        _, seeds = stdin.readline().split(':')
        seeds = map(int, seeds.split())
        self._seeds = list(seeds)

        self._maps = []
        for mapping in stdin.read().strip().split('\n\n'):
            current_map = []
            for line in mapping.split('\n')[1:]:
                dest, source, length = map(int, line.split())
                current_map.append((dest, source, length))
            self._maps.append(current_map)

    def solve1(self) -> int:
        locations = self._seeds.copy()

        for i in range(len(locations)):
            for map in self._maps:
                for dest, source, length in map:
                    if source <= locations[i] < source + length:
                        locations[i] += dest - source
                        break

        return min(locations)

    def _get_map_range(self, map: list[(int, int, int)], ranges: list) -> list[int, int]:
        new_ranges = []
        for dst, src, length in map:
            delta = dst - src
            not_intersected_ranges = []

            while ranges:
                start, end = ranges.pop()
                # ----|intersection|
                if start < src and src < end <= src + length:
                    not_intersected_ranges.append((start, src))
                    new_ranges.append((dst, end + delta))
                # ----|intersection|----
                elif start < src and end > src + length:
                    not_intersected_ranges.append((start, src))
                    not_intersected_ranges.append((src + length, end))
                    new_ranges.append((dst, dst + length))
                # |intersection|
                elif src <= start < src + length and end <= src + length:
                    new_ranges.append((start + delta, end + delta))
                # |intersection|----
                elif src <= start < src + length and end > src + length:
                    new_ranges.append((start + delta, dst + length))
                    not_intersected_ranges.append((src + length, end))
                # no intersection
                # -------------
                else:
                    not_intersected_ranges.append((start, end))

            ranges = not_intersected_ranges

        return new_ranges + not_intersected_ranges


    def solve2(self) -> int:
        min_locations = []
        for start, length in zip(self._seeds[::2], self._seeds[1::2]):
            current_ranges = [(start, start + length)]
            for map in self._maps:
                current_ranges = self._get_map_range(map, current_ranges)
            min_locations.append(min(current_ranges)[0])

        return min(min_locations)


solution = Solution()
print(solution.solve1())
print(solution.solve2())
