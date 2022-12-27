import heapq
from collections import deque
from functools import reduce
from typing import Callable, Deque

from utility import parseInput


class Monkey:
    def __init__(self, starting_items: Deque[int], operation: Callable,
                 divider: int, true_throw: int, false_throw: int, ):
        self.starting_items: Deque[int] = starting_items
        self.operation: Callable = operation
        self.divider = divider
        self.true = true_throw
        self.false = false_throw
        self.inspections = 0

    def throw(self, current_item: int) -> int:
        if current_item % self.divider == 0:
            return self.true
        return self.false

    def __repr__(self):
        return f"""
        Starting items: {self.starting_items}
        Operation: {self.operation}
        Throws: {self.true} if divisible by {self.divider} else {self.false}
        Inspections: {self.inspections}
        """


class Solution:

    def keep_away_tracker(self, use_real_input: bool = False,
                          second_problem: bool = True) -> int:
        """
        :param use_real_input: bool. Use real data if True, else test data
        :param second_problem: bool. If True then return answer for second part
        :return: str. Str containing the letters of the top of each stack
        """
        lines = parseInput("test.txt") if not use_real_input else parseInput(
            "real.txt")
        lines = lines.split("\n")
        monkeys = []
        line_reader = 0

        def op_conversion(operation_str: str) -> Callable:
            func = operation_str.split(" = ")[1]
            # https://peps.python.org/pep-0622/#sequence-patterns
            match (func.split()):
                case [_, "+", _]:
                    parts = func.split(" + ")
                    if parts[1] == 'old':
                        return lambda a: a + a
                    return lambda a: a + int(parts[1])
                case [_, "-", _]:
                    parts = func.split(" - ")
                    if parts[1] == 'old':
                        return lambda a: a - a
                    return lambda a: a - int(parts[1])
                case [_, "*", _]:
                    parts = func.split(" * ")
                    if parts[1] == 'old':
                        return lambda a: a * a
                    return lambda a: a * int(parts[1])
                case [_, "/", _]:
                    parts = func.split(" / ")
                    if parts[1] == 'old':
                        return lambda a: a / a
                    return lambda a: a / int(parts[1])
            raise Exception(f"Found unexpected operator: {func.split()}")

        def start_items(starting_str: str) -> Deque[int]:
            return deque([int(item) for item in
                          starting_str.split("Starting items: ")[
                              1].split(", ")])

        def divider_conversion(dividing_str: str) -> int:
            return int(dividing_str.split(" by ")[1])

        def monkey_throw_conversion(statement_str: str) -> int:
            return int(statement_str.split("monkey ")[1])

        while line_reader < len(lines):
            if lines[line_reader].startswith("Monkey"):
                line_reader += 1
                starting_items = start_items(lines[line_reader])
                line_reader += 1
                operation = op_conversion(lines[line_reader])
                line_reader += 1
                divider = divider_conversion(lines[line_reader])
                line_reader += 1
                true = monkey_throw_conversion(lines[line_reader])
                line_reader += 1
                false = monkey_throw_conversion(lines[line_reader])
                new_monkey = Monkey(starting_items, operation, divider, true,
                                    false)
                monkeys.append(new_monkey)
            line_reader += 1
        lcd = 1
        for monkey in monkeys:
            lcd *= monkey.divider
        max_rounds = 20 if not second_problem else 10000
        for i in range(max_rounds):
            for idx, monkey in enumerate(monkeys):
                while monkey.starting_items:
                    starting_item = monkey.starting_items.popleft()
                    current_worry = monkey.operation(starting_item)
                    if not second_problem:
                        current_worry = current_worry // 3
                    else:
                        current_worry = current_worry % lcd
                    monkeys[monkey.throw(current_worry)].starting_items.append(
                        current_worry)
                    monkey.inspections += 1
        for idx, monkey in enumerate(monkeys):
            print(
                f"Monkey {idx}: "
                f"{', '.join([str(x) for x in monkey.starting_items])}")
        print("\n")
        inspections = []
        for idx, monkey in enumerate(monkeys):
            print(f"Monkey {idx} inspected items {monkey.inspections} times.")
            inspections.append((monkey.inspections, idx))
        heapq.heapify(inspections)
        return reduce(lambda a, b: a[0] * b[0], heapq.nlargest(2, inspections))


run = Solution()
print(run.keep_away_tracker(False, False))
print(run.keep_away_tracker(True, False))
print(run.keep_away_tracker(False, True))
print(run.keep_away_tracker(True, True))
