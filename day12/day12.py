from heapq import heappush, heappop, heapify
from typing import List, Set

from utility import parseInput


class Coordinate:
    def __init__(self, x: int, y: int, marker: str, val: int, min_dist: int
    = 10000):
        self.x: int = x
        self.y: int = y
        self.marker: str = marker
        self.val: int = val
        self.min_dist: int = min_dist

    def __repr__(self):
        return f"{self.marker} ({self.x},{self.y}) {self.min_dist}"

    def __lt__(self, other):
        return self.x < other.x


class Solution:

    def hill_climbing_pather(self, use_real_input: bool = False,
                             second_problem: bool = True) -> int:
        """
        Use Dijkstra's algorithm, which is primarily a bfs that has dfs
        characteristics. The reason why this didn't work initially is because
        I didn't use a heurstic, which is the whole point. Instead of using a queue,
        use a heapq with a prioritization key using each unexplored node's
        minimum distance. ALso, the reason why this initially was slow was
        because I added the seen check in the adj helper method. This means
        that it got checked at the end, after we already explored it; leading to
        a usless double check.
        :param use_real_input: bool. Use real data if True, else test data
        :param second_problem: bool. If True then return answer for second part
        :return: str. Str containing the letters of the top of each stack
        """
        # Populate the input matrix
        explore_matrix: List[List[Coordinate]] = []
        lines = parseInput("test.txt") if not use_real_input else parseInput(
            "real.txt")
        lines = lines.split("\n")
        start = None
        end = None
        for r, line in enumerate(lines):
            a_line = []
            for c, val in enumerate(list(line)):
                a_line.append(Coordinate(r, c, val, ord(val) - 96))
                if val == 'S':
                    start = a_line[-1]
                    start.val = 0
                elif val == 'E':
                    end = a_line[-1]
                    end.val = 27
                elif second_problem and val == 'a':
                    a_line[-1].min_dist = 0
            explore_matrix.append(a_line)
        if not start and not end:
            raise Exception("No (S)tart  or (E)nd positions found!")
        m = len(explore_matrix)
        n = len(explore_matrix[0])

        def print_map() -> None:
            nonlocal explore_matrix
            print("--------------------------------------------")
            for r in range(m):
                line = ""
                for c in range(n):
                    cell = explore_matrix[r][c]
                    if cell.min_dist == 10000:
                        pair = f"{cell.marker},∞, {cell.val}"
                    else:
                        pair = f"{cell.marker},{cell.min_dist},{cell.val}"
                    line = line + f"{pair} "
                print(line)

        def add_adj_coords(pos: Coordinate) -> None:
            nonlocal explore_matrix
            nonlocal m
            nonlocal n
            nonlocal second_problem
            nonlocal heap
            nonlocal seen
            for x, y in ([[pos.x + 1, pos.y], [pos.x, pos.y + 1],
                          [pos.x - 1, pos.y], [pos.x, pos.y - 1]]):
                if 0 <= x < m and 0 <= y < n:
                    tmp = explore_matrix[x][y]

                    # Handle case where next adjacent cell is 1 above
                    # or less in terms of ascii value
                    if not second_problem:
                        if pos.val >= tmp.val - 1:
                            heappush(heap, (pos.min_dist + 1, tmp))
                    else:
                        if pos.val - 1 <= tmp.val:
                            heappush(heap, (pos.min_dist + 1, tmp))

        start.min_dist = 0
        heap = [(0, start)] if not second_problem else [(0, end)]
        heapify(heap)
        seen: Set[Coordinate] = set()
        while heap:
            dist, cell = heappop(heap)
            # Skip previously visited vertexes
            if cell in seen:
                continue
            if (not second_problem and cell.marker == "E") or (second_problem
                                                               and cell.marker == "a"):
                print_map()
                return dist
            cell.min_dist = min(cell.min_dist, dist)
            seen.add(cell)
            add_adj_coords(cell)
        print_map()


run = Solution()
print(run.hill_climbing_pather(False, False))
print(run.hill_climbing_pather(True, False))
print(run.hill_climbing_pather(False, True))
print(run.hill_climbing_pather(True, True))
