from sys import stdin


class Solution:
    def __init__(self) -> None:
        image = stdin.read().splitlines()

        # galaxies coordinates
        self._galaxies = []
        for y in range(len(image)):
            for x in range(len(image[0])):
                if image[y][x] == '#':
                    self._galaxies.append((x, y))

        # number of empty rows before each row
        self._empty_rows = [0] * len(image)
        for y in range(1, len(image)):
            if '#' not in image[y]:
                self._empty_rows[y] = 1
            self._empty_rows[y] += self._empty_rows[y - 1]

        # number of empty columns befor each column
        self._empty_columns = [0] * len(image[0])
        for x in range(1, len(image[0])):
            col = (image[y][x] for y in range(len(image)))
            if '#' not in col:
                self._empty_columns[x] = 1
            self._empty_columns[x] += self._empty_columns[x - 1]

    def _solve(self, expand: int = 2) -> int:
        answer = 0
        galaxies = self._galaxies
        empty_rows = self._empty_rows
        empty_columns = self._empty_columns

        for i in range(len(galaxies)):
            for j in range(i + 1, len(galaxies)):
                x1, y1 = galaxies[i][0], galaxies[i][1]
                x2, y2 = galaxies[j][0], galaxies[j][1]
                # add manhattan distance
                answer += abs(x2 - x1) + abs(y2 - y1)
                # add number of empty columns between x and y * (expand - 1)
                answer += abs(empty_columns[x2] - empty_columns[x1]) * (expand - 1)
                # add number of empty rows between x and y * (expand - 1)
                answer += abs(empty_rows[y2] - empty_rows[y1]) * (expand - 1)

        return answer


    def solve1(self) -> int:
        return self._solve()

    def solve2(self) -> int:
        return self._solve(1000000)


solution = Solution()
print(solution.solve1())
print(solution.solve2())
