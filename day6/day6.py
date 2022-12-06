from utility import parseInput, parseInputDay5
import itertools
from typing import List


class Solution:

    def coms_fixer(self, use_real_input: bool = False, window_size: int = 4) -> int:
        """
        Returns a str of the top letters of each stack of boxes
        :param use_real_input: bool. Use real data if True, else test data
        :param second_problem: bool. If True then return answer for second part
        :return: str. Str containing the letters of the top of each stack
        """
        res = ""
        # O(N) time, O(N) space where N is the number of lines
        coms = parseInput("test.txt") if not use_real_input else parseInput("real.txt")

        for i in range(0,len(coms)-(window_size-1), 1):
            window = coms[i:i+window_size]
            if len(set(window)) == window_size:
                return i+window_size
        return -1

run = Solution()
print(run.coms_fixer(True))
print(run.coms_fixer(True,14))
