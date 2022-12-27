from collections import deque

from utility import parseInput


class Cell:
    def __init__(self):
        self.curr_cursor: str = "."
        self.visited_state: str = "."


class Solution:
    MAP_LENGTH = 40

    def trail_rope(self, use_real_input: bool = False,
                   second_problem: bool = False) -> int:
        """
        :param use_real_input: bool. Use real data if True, else test data
        :param second_problem: bool. If True then return answer for second part
        :return: str. Str containing the letters of the top of each stack
        """

        # Parse our input
        lines = parseInput("test.txt") if not use_real_input else parseInput(
            "real.txt")
        lines = deque(lines.split("\n"))
        travel_map = deque([])

        for _ in range(self.MAP_LENGTH):
            new_row = deque([])
            for _ in range(self.MAP_LENGTH):
                new_row.append(Cell())
            travel_map.append(new_row)
        head_i = head_j = head_2i = head_2j = self.MAP_LENGTH // 2 - 1
        rope = [(head_i, head_j)]
        if not second_problem:
            rope.append((head_2i, head_2j))
        else:
            for _ in range(9):
                rope.append((head_2i, head_2j))

        travel_map[head_i][head_j].visited_state = "S"

        def checkAdj() -> bool:
            nonlocal head_i, head_2i
            nonlocal head_2i, head_2j
            return abs(head_i - head_2i) <= 1 and abs(head_j - head_2j) <= 1

        def print_map() -> None:
            for row in travel_map:
                print("".join([cell.curr_cursor for cell in row]) + (
                        " " * 5) + "".join(
                    [cell.visited_state for cell in row]))
            print()

        while lines:
            cmd = lines.popleft().split(" ")
            print(f"== {cmd[0]} {cmd[1]} ==")
            for _ in range(int(cmd[1])):
                travel_map[head_i][head_j].curr_cursor = "."
                match cmd[0]:
                    case "L":
                        head_j -= 1
                    case "R":
                        head_j += 1
                    case "U":
                        head_i -= 1
                    case "D":
                        head_i += 1
                    case default:
                        raise Exception(f"Invalid command found! {cmd[0]}")

                if checkAdj():
                    continue
                else:
                    travel_map[head_2i][head_2j].curr_cursor = '.'
                    
                    if head_i == head_2i:
                        if head_j > head_2j:
                            head_2j += 1
                        elif head_j < head_2j:
                            head_2j -= 1
                    elif head_j == head_2j:
                        if head_i > head_2i:
                            head_2i += 1
                        elif head_i < head_2i:
                            head_2i -= 1
                    elif head_i > head_2i:
                        if head_j > head_2j:
                            head_2i += 1
                            head_2j += 1
                        else:
                            head_2i += 1
                            head_2j -= 1
                    elif head_i < head_2i:
                        if head_j > head_2j:
                            head_2i -= 1
                            head_2j += 1
                        else:
                            head_2i -= 1
                            head_2j -= 1
                travel_map.append((head_2i, head_2j))
                travel_map[head_2i][head_2j].curr_cursor = 'T'
                travel_map[head_2i][head_2j].visited_state = '#'
            # print_map()
        return len(set(travel_map))
        # res = 0
        # for i in range(len(travel_map)):
        #     for j in range(len(travel_map[i])):
        #         if travel_map[i][j].visited_state == '#' or travel_map[i][
        #             j].visited_state == 'S':
        #             res += 1
        # return res


run = Solution()
print(run.trail_rope(False, False))
print(run.trail_rope(True, False))
# print(run.trail_rope(False, True))
# print(run.trail_rope(True, True))
