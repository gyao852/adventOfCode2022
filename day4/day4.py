from utility import parseInput


class Solution:

    def full_assignment_overlap(self, use_real_input: bool = False) -> int:
        """
        Returns count of when a row has one range be a complete subset of the
        other
        :param use_real_input: bool. Use real data if true, else test data
        :return: int. Sum of overlap assignments
        """
        res = 0
        data = parseInput("test.txt") if not use_real_input else parseInput("real.txt")
        assignments = data.split("\n")

        # O(N) overall when N is the number of
        # rows/assignments. O(N) space as well since we
        # parsed and converted the data to list pairs
        for assignment in assignments:
            groups = assignment.split(",")
            first_group = [int(x) for x in groups[0].split("-")]  # O(1) since groups is always size 2
            second_group = [int(x) for x in groups[1].split("-")]
            if (first_group[0] <= second_group[0] and second_group[1] <= first_group[1]) or (
                    first_group[0] >= second_group[0] and first_group[1] <= second_group[1]):
                res += 1
        return res

    def partial_assignment_overlap(self, use_real_input: bool = False) -> int:
        """
        Returns count of when a row has any instance of overlap between
        the two assignment ranges
        other
        :param use_real_input: bool. Use real data if true, else test data
        :return: int. Sum of overlap assignments
        """
        res = 0
        data = parseInput("test.txt") if not use_real_input else parseInput("real.txt")
        assignments = data.split("\n")

        # O(N) overall when N is the number of
        # rows/assignments. O(N) space as well since we
        # parsed and converted the data to list pairs
        for assignment in assignments:
            groups = assignment.split(",")
            first_group = [int(x) for x in groups[0].split("-")]
            second_group = [int(x) for x in groups[1].split("-")]
            # Instead o checking for all combinations of both groups
            # being in a subset/overlap with each other, just check the cases
            # when they are strictly NOT overlapping and ! that.
            if not (first_group[0] < second_group[0] and first_group[1] < second_group[0]) and not (
                    second_group[0] < first_group[0] and second_group[1] < first_group[0]):
                res += 1
        return res


run = Solution()
print(run.full_assignment_overlap(True))
print(run.partial_assignment_overlap(True))
