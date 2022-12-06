from utility import parseInputDay5
from typing import List

class Solution:

    def stack_crate_operator(self, use_real_input: bool = False, second_problem: bool = False) -> str:
        """
        Returns a str of the top letters of each stack of boxes
        :param use_real_input: bool. Use real data if True, else test data
        :param second_problem: bool. If True then return answer for second part
        :return: str. Str containing the letters of the top of each stack
        """
        res = ""
        # O(N) time, O(N) space where N is the number of lines
        stacks, instructions = parseInputDay5("test.txt") if not use_real_input else parseInputDay5("real.txt")

        # O(N) time where N is the number of lines for instructions
        for instruction in instructions:
            # Move M number of boxes from one stack to another
            tmp_stack: List[str] = []
            for _ in range(instruction[2]):
                tmp_stack.append(stacks[instruction[0] - 1].pop())
            if second_problem:
                # In second problem, just reverse the stack we are popping from
                tmp_stack = tmp_stack[::-1]
            stacks[instruction[1] - 1].extend(tmp_stack)
        # Finally, pop the top of each stack to our res:
        for stack in stacks:
            res += stack.pop()
        return res

run = Solution()
print(run.stack_crate_operator(True, False))
print(run.stack_crate_operator(True, True))
