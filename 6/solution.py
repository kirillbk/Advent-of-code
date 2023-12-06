# Time:      7  15   30
# Distance:  9  40  200

class Solution:
    def __init__(self) -> None:
        _, self._time = input().split(':')
        _, self._distance = input().split(':')

    def solve1(self) -> int:
        t = map(int, self._time.split())
        d = map(int, self._distance.split())

        answer = 1
        for time, distance in zip(t, d):
            cntr = 0
            for i in range(0, time):
                if (time - i) * i > distance:
                    cntr += 1
            answer *= cntr

        return answer

    def solve2(self) -> int:
        time = int(self._time.replace(' ', ''))
        distance = int(self._distance.replace(' ', ''))

        answer = 0
        for i in range(0, time):
            if (time - i) * i > distance:
                answer += 1

        return answer


solution = Solution()
print(solution.solve1())
print(solution.solve2())
