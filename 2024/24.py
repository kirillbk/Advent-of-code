# https://adventofcode.com/2024/day/24
# --- Day 24: Crossed Wires ---

from abc import ABC, abstractmethod
from dataclasses import dataclass
from operator import attrgetter
from sys import stdin
from typing import Self


@dataclass
class Wire:
    out: int
    name: str


@dataclass
class Gate(ABC):
    in1: Self | Wire
    in2: Self | Wire
    name: str

    @property
    @abstractmethod
    def out(self) -> int: ...


class And(Gate):
    @property
    def out(self) -> int:
        return self.in1.out & self.in2.out


class Or(Gate):
    @property
    def out(self) -> int:
        return self.in1.out | self.in2.out


class Xor(Gate):
    @property
    def out(self) -> int:
        return self.in1.out ^ self.in2.out


def simulate(schema: dict[str, Gate]) -> int:
    out = filter(lambda x: x.name.startswith("z"), schema.values())
    out = (gate.out for gate in sorted(out, key=attrgetter("name"), reverse=True))
    ans = 0
    for z in out:
        ans = (ans << 1) | z

    return ans


def solution1(schema: dict[str, Gate]) -> int:
    return simulate(schema)


# use Graphviz: dot -Tsvg -O .\graph.gv
def solution2(schema: dict[str, Gate]) -> int:
    f = open("graph.gv", "w")
    f.write("digraph G {\n\tnode [shape=box]\n")

    for gate in schema.values():
        match gate:
            case Wire():
                color = "blue"
                xlabel = "IN"
            case Or():
                color = "green"
                xlabel = "OR"
            case And():
                color = "red"
                xlabel = "AND"
            case Xor():
                color = "purple"
                xlabel = "XOR"
        f.write(f"\t{gate.name} [color={color} xlabel={xlabel}]\n")
        if not isinstance(gate, Wire):
            f.write(f"\t{gate.in1.name} -> {gate.name}\n")
            f.write(f"\t{gate.in2.name} -> {gate.name}\n")

    f.write("\t{rank=same " + ", ".join(f"x{i:02}, y{i:02}" for i in range(45)) + "}\n")
    f.write("\t{rank=same " + ", ".join(f"z{i:02}" for i in range(46)) + "}\n}")

    ans = ["z12", "kwb", "z16", "qkf", "z24", "tgr", "cph", "jqn"]
    ans.sort()
    return ",".join(ans)


wires, gates = stdin.read().split("\n\n")
wires = [wire.split(":") for wire in wires.split("\n")]
gates = [gate.split() for gate in gates.split("\n")]
gates.pop()

schema = {name: Wire(out=int(val), name=name) for name, val in wires}
cntr = 0
while cntr != len(gates):
    for in1, op, in2, _, name in gates:
        if name not in schema and in1 in schema and in2 in schema:
            cntr += 1
            match op:
                case "AND":
                    schema[name] = And(schema[in1], schema[in2], name=name)
                case "OR":
                    schema[name] = Or(schema[in1], schema[in2], name=name)
                case "XOR":
                    schema[name] = Xor(schema[in1], schema[in2], name=name)
                case _:
                    raise RuntimeError()


print(solution1(schema))
print(solution2(schema))
