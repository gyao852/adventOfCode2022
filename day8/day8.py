from utility import parseInput
from typing import Any, List, Optional
from functools import reduce
import math

class Tree:
    def __init__(self,row: int, col: int, height: int):
        self.row = row
        self.col = col
        self.height = height
        self.sides_visible = []
        self.sides_values = []

    def __repr__(self):
        return f"({self.height},{math.prod(self.sides_values)})"

class Solution:

    def find_visible_trees(self, use_real_input: bool = False, second_problem: bool = False) -> int:
        """
        Populate the topology of a matrix of trees, and returns the number of trees that are
        visible outside of the grid, or the tree with the highest 'scenic' score based on the
        product of all the trees it can see past it. This was primarily just a 2d traversal,
        with a tranpose so that we can easily check all four directions of a 2d coordinate.

        First, we check the conditions for a cell left and right; then we tranpose it and
        call the same helper function that does the check for left and right. Because we transposed
        the matrix, checking left or right the second time is essentially checking it 'top' and 'bottom'
        :param use_real_input: bool. Use real data if True, else test data
        :param second_problem: bool. If True then return answer for second part
        :return: str. Str containing the letters of the top of each stack
        """

        # Parse our input
        lines = parseInput("test.txt") if not use_real_input else parseInput("real.txt")
        lines = lines.split("\n")
        tree_map: List[List[int]] = []
        visible_map: List[List[Optional[Tree]]] = []
        for line in lines:
            tree_map.append([int(x) for x in line])
            visible_map.append([None for _ in line])

        def print_map(some_map: List[List[Any]]) -> None:
            for i in range(len(some_map)):
                line = "".join([str(x) for x in some_map[i]])
                print(line)
            print()

        for i in range(len(tree_map)):
            for j in range(len(tree_map[i])):
                visible_map[i][j] = Tree(i,j,tree_map[i][j])
                if i == 0:
                    visible_map[i][j].sides_visible.append("left")
                elif j == 0:
                    visible_map[i][j].sides_visible.append("right")
                elif i == len(tree_map) - 1:
                    visible_map[i][j].sides_visible.append("top")
                elif j == len(tree_map) - 1:
                    visible_map[i][j].sides_visible.append("bottom")

        def set_tree_visibility(reference_map: List[List[int]], topography_map: List[List[Tree]],
                                left_side: str = "left", right_side: str = "right") -> None:
            nonlocal second_problem
            for i in range(1, len(reference_map) - 1):
                for j in range(1, len(reference_map[i]) - 1):
                    # Check if visible left
                    tallest_left_tree = max(reference_map[i][:j + 1])
                    tallest_left_tree_idx = reference_map[i][:j + 1].index(tallest_left_tree)
                    if reference_map[i][j] == tallest_left_tree:
                        if j == tallest_left_tree_idx:
                            topography_map[i][j].sides_visible.append(left_side)
                    # Check if visible right
                    tallest_right_tree = max(reference_map[i][j:])
                    tallest_right_tree_idx = len(reference_map[i][j:]) - list(reversed(reference_map[i][j:])).index(
                        tallest_right_tree) - 1 + j
                    if reference_map[i][j] == tallest_right_tree:
                        if j == tallest_right_tree_idx:
                            topography_map[i][j].sides_visible.append(right_side)

                    # If the current tree is tall enough to even see a single side
                    # we should populate the tree's side values for later calculations
                    # Calculate 'left' sides tree counts
                    if j == tallest_left_tree_idx:
                        topography_map[i][j].sides_values.append(len(reference_map[i][:j + 1])-1)
                    else:
                        left_value = 0
                        for v in range(len(reference_map[i][:j + 1])-2, -1, -1):
                            if reference_map[i][v] < reference_map[i][j]:
                                left_value += 1
                            else:
                                left_value += 1
                                break
                        topography_map[i][j].sides_values.append(left_value)
                    if j == tallest_right_tree_idx:
                        topography_map[i][j].sides_values.append(len(reference_map[i][j:])-1)
                    else:
                        right_value = 0
                        for v in range(j+1,len(reference_map[i])):
                            if reference_map[i][v] < reference_map[i][j]:
                                right_value += 1
                            else:
                                right_value += 1
                                break
                        topography_map[i][j].sides_values.append(right_value)
                    if i == 3 and j == 2:
                        print(topography_map[i][j].sides_visible, topography_map[i][j].sides_values)

        def transpose_maps():
            nonlocal tree_map
            nonlocal visible_map
            for i in range(len(tree_map)):
                for j in range(i, len(tree_map[i])):
                    tmp_ref = tree_map[j][i]
                    tree_map[j][i] = tree_map[i][j]
                    tree_map[i][j] = tmp_ref
                    tmp_top = visible_map[j][i]
                    visible_map[j][i] = visible_map[i][j]
                    visible_map[i][j] = tmp_top

        set_tree_visibility(tree_map, visible_map)
        transpose_maps()
        set_tree_visibility(tree_map, visible_map, "top", "bottom")
        transpose_maps()
        res = 0
        for i in range(len(visible_map)):
            for j in range(len(visible_map[i])):
                if visible_map[i][j].sides_visible:
                    curr_tree = visible_map[i][j]
                    print(f"Tree at {i},{j} ({curr_tree.height}) can see side(s): {','.join(curr_tree.sides_visible)}!")
                    if not second_problem:
                        res += 1
                    else:
                        res = max(res,math.prod(curr_tree.sides_values))
        print_map(tree_map)
        print_map(visible_map)
        return res


run = Solution()
print(run.find_visible_trees(False, False))
print(run.find_visible_trees(True, False))
print(run.find_visible_trees(False, True))
print(run.find_visible_trees(True, True))
