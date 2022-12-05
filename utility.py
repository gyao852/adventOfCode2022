from typing import Dict, Any, List, Tuple
from collections import defaultdict, deque
import math

def parseInput(pathToFile: str) -> Any:
    """
    Helper function to parse files
    :param pathToFile: Path to input file
    :return: Any. Parsed data
    """
    res = ""
    with open(pathToFile, 'r') as f:
        for line in f:
            res += line
    return res


def parseInputDay5(pathToFile: str) -> (List[List[str]], List[Tuple[int]]):
    """
    Helper function to parse stacks for
    day5 problem
    :param pathToFile: Path to input file
    :return: Any. Parsed data
    """
    initial_stack: Dict[int, deque] = defaultdict(deque)
    instructions: List[Tuple[int]] = []
    res = ""
    with open(pathToFile, 'r') as f:

        # Handle initial stack
        for line in f:
            if line == "\n":
                break
            line_len = len(line)
            for i in range(1, line_len, 4):
                # We reached the line that shows stack number idx
                if line[i].isdigit():
                    break
                if line[i] == ' ':
                    continue
                initial_stack[math.ceil(i/4)].appendleft(line[i])
        stack_in_list = [[]] * len(initial_stack)
        for idx, stack in initial_stack.items():
            stack_in_list[idx-1] = stack


        # Handle instructions:
        for line in f:
            if line == "\n" or "move" not in line:
                continue
            instruction = line.split(" ")
            instructions.append((int(instruction[3]), int(instruction[5]), int(instruction[1])))
        return stack_in_list, instructions
