from sys import stdin
from re import findall


value = 0
mydict = dict(one='1', two='2', three='3', four='4', five='5', six='6', seven='7', eight='8', nine='9')
for line in stdin:
    m = findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)
    value += int(mydict.get(m[0], m[0]) + mydict.get(m[-1], m[-1]))

print(value)
