from utility import parseInput
from typing import List, Set
import heapq
from functools import reduce


class Solution:

    def unique_in_each_sack(self, use_real_input: bool = False) -> int:
        """
        Returns the sum of the priority badges
        carried by an elf
        :param use_real_input: bool. Use real data if true, else test data
        :return: int. Sum of badge types
        """
        res = 0
        data = parseInput("test.txt") if not use_real_input else parseInput("real.txt")
        rucksack = [set(sack[:len(sack) // 2]).intersection(set(sack[len(sack) // 2:])) for sack in
                                     data.split('\n')]
        # Simply sum up all badge values
        # for sack in rucksack:
        #     badge = sack.pop()
        #     if badge.islower():
        #         res += ord(badge) - 96
        #     else:
        #         res += ord(badge) - 38
        # return res

        # NOTE: Even though the question prioritizes based on the
        # badge value, we can make a max heap like so to make a sorted list
        # of the rucksack badges, based on priority. In the end we just sum
        # everything, so it doesn't matter but the heap struct could help in the future
        rucksack = [sack.pop() for sack in rucksack]
        rucksack = list(map(lambda a: ord(a) - 96 if a.islower() else ord(a) - 38, rucksack))
        heapq.heapify(rucksack)
        while rucksack:
            res += heapq.heappop(rucksack)
        return res

    def unique_in_k_sacks(self, use_real_input: bool = False, k: int = 3) -> int:
        """
        Returns the sum of unique badges in k groups of rucksack
        carried by an elf
        :param use_real_input: bool. Use real data if true, else test data
        :param k: int. Number of groups
        :return: int. Sum of badge types per k group
        """

        data = parseInput("test.txt") if not use_real_input else parseInput("real.txt")
        rucksack: List[Set[str]] = [set(sack) for sack in data.split('\n')]
        res = 0
        # Sum up badge values at k intervals
        # for i in range(0, len(rucksack),k):
        #     unique = reduce(lambda a,b: a.intersection(b),rucksack[i:i+k])
        #     badge = unique.pop()
        #     if badge.islower():
        #         res += ord(badge) - 96
        #     else:
        #         res += ord(badge) - 38
        # return res
        badges = []
        for i in range(0, len(rucksack),k):
            unique = reduce(lambda a,b: a.intersection(b),rucksack[i:i+k])
            badge = unique.pop()
            if badge.islower():
                badges.append(ord(badge) - 96)
            else:
                badges.append(ord(badge) - 38)
        heapq.heapify(badges)

        while badges:
            res += heapq.heappop(badges)
        return res


run = Solution()
print(run.unique_in_each_sack(True))
print(run.unique_in_k_sacks(True, k=3))
