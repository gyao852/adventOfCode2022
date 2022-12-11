from collections import deque

from utility import parseInput


class Cell:
    def __init__(self):
        self.curr_cursor: str = "."
        self.visited_state: str = "."


class Solution:

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

        # for _ in range(6):
        #     travel_map.append(
        #         deque([Cell(), Cell(), Cell(), Cell(), Cell(), Cell()]))
        tail_i = head_i = 0
        tail_j = head_j = 0

        # travel_map[5][0].visited_state = "S"

        def checkAdj() -> bool:
            nonlocal head_i, tail_i
            nonlocal tail_i, tail_j
            return abs(head_i - tail_i) <= 1 and abs(head_j - tail_j) <= 1

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
                # travel_map[head_i][head_j].curr_cursor = "."
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

                #
                #
                # if head_i < 0:
                #     new_top_row = deque([])
                #     for _ in range(len(travel_map[head_i])):
                #         new_top_row.append(Cell())
                #     travel_map.appendleft(new_top_row)
                #     head_i = 0
                #
                # # re-expand our map to the left
                # if head_j < 0:
                #     for row in travel_map:
                #         row.appendleft(Cell())
                #     head_j = 0
                #
                # # re-expand our map down an entire row
                # if head_i >= len(travel_map):
                #     new_top_row = deque([])
                #     for _ in range(len(travel_map[head_i])):
                #         new_top_row.append(Cell())
                #     travel_map.append(new_top_row)
                #     head_i = len(travel_map) - 1
                #
                # # Expand the entire right column
                # if head_j >= len(travel_map[head_i]):
                #     for i in range(len(travel_map)):
                #         travel_map[i].append(Cell())
                #     head_j = len(travel_map[head_i]) - 1
                # travel_map[head_i][head_j].curr_cursor = "H"
                # if cmd == "U 2":
                #     print(abs(head_i - tail_i) <= 1 and abs(
                #         head_j - tail_j) <= 1)

                if checkAdj():
                    continue
                else:
                    # travel_map[tail_i][tail_j].curr_cursor = '.'
                    if head_i == tail_i:
                        if head_j > tail_j:
                            tail_j += 1
                        elif head_j < tail_j:
                            tail_j -= 1
                    elif head_j == tail_j:
                        if head_i > tail_i:
                            tail_i += 1
                        elif head_i < tail_i:
                            tail_i -= 1
                    elif head_i > tail_i:
                        if head_j > tail_j:
                            tail_i += 1
                            tail_j += 1
                        else:
                            tail_i += 1
                            tail_j -= 1
                    elif head_i < tail_i:
                        if head_j > tail_j:
                            tail_i -= 1
                            tail_j += 1
                        else:
                            tail_i -= 1
                            tail_j -= 1
                travel_map.append((tail_i, tail_j))
                # travel_map[tail_i][tail_j].curr_cursor = 'T'
                # travel_map[tail_i][tail_j].visited_state = '#'
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
