from utility import parseInput
import heapq


class Solution:
    def max_total_in_string(self, use_real_input: bool = False) -> int:
        """
        Returns the most total Calories
        carried by an elf
        :param use_real_input: bool. Use real data if true, else test data
        :return: int. Maximum calories
        """
        data = parseInput("test.txt") if not use_real_input else parseInput("real.txt")
        elf_cals = [[int(food) for food in elf.split("\n")] for elf in data.split("\n\n")]
        return max(sum(elf_cal) for elf_cal in elf_cals)

    def top_k_in_string(self, use_real_input: bool = False, k: int = 3) -> int:
        """
        Returns the top k calories
        :param k:
        :param use_real_input: bool. Use real data if true, else test data
        :return: int. Sum of top k calories
        """
        data = parseInput("test.txt") if not use_real_input else parseInput("real.txt")
        elf_cals = [[int(food) for food in elf.split("\n")] for elf in data.split("\n\n")]

        # 1) Multiply by -1, use heap to create min heap, then pop k num
        # of calories. O(N) for heapify, O(logN) for popping
        # heap = [-1 * sum(cals) for cals in elf_cals]
        # heapq.heapify(heap)
        # res = 0
        # while k:
        #     k-=1
        #     res += (-1*heapq.heappop(heap))
        # return res
        # 2) Just use timsort from python's builtin sorted functionlaity, and
        # then pop last 3 elements and sum them together
        res = 0
        sums = [sum(cals) for cals in elf_cals]
        sums.sort()
        while k:
            k-=1
            res += sums.pop()
        return res


run = Solution()
print(run.max_total_in_string(True))
print(run.top_k_in_string(True, 3))
