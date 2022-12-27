from typing import List

from utility import parseInput


class Operation:
    def __init__(self, variable: str, strength: str):
        self.variable: str = variable
        self.strength: int = int(strength)


class Solution:
    MIN_PIXEL_LENGTH = 0
    MAX_PIXEL_LENGTH = 40
    SPRITE_SIZE = 3

    def signal_strength_calculator(self, use_real_input: bool = False,
                                   second_problem: bool = True) -> int:
        """
        Calculate the signal strength by just reading line by line and
        using some simple boolean calculation. Hardest part was making sure the
        'state' of each before, during and after a cycle. This was achieved by
        just making a subfunction to work out each 'step'.
        :param use_real_input: bool. Use real data if True, else test data
        :param second_problem: bool. If True then return answer for second part
        :return: str. Str containing the letters of the top of each stack
        """
        lines = parseInput("test.txt") if not use_real_input else parseInput(
            "real.txt")
        lines = lines.split("\n")
        x: int = 1
        op_count: int = 0
        signal_strength: List[int] = []
        signal_screen: List[List[str]] = []
        current_row = -1

        def print_sprite_position(sprite_pos: int) -> None:
            sprite_position = ['.'] * self.MAX_PIXEL_LENGTH
            for i in range(self.SPRITE_SIZE):
                if sprite_pos - 1 + i < self.MAX_PIXEL_LENGTH:
                    sprite_position[sprite_pos - 1 + i] = '#'
            print(f"Sprite position: {''.join(sprite_position)}")

        def print_screen() -> None:
            """
            Print screen of the signal calculator
            :return: None
            """
            for screen_line in signal_screen:
                print(''.join(screen_line))

        def step_and_check_signal() -> None:
            """
            Perform one step in the calculator operation
            and then check to see if we meet part 1 condition.
            Also check part 2's spirit movements
            :param crt_pos: current pixel being drawn
            :return: None
            """
            nonlocal x
            nonlocal op_count
            nonlocal signal_strength
            nonlocal signal_screen
            nonlocal current_row
            if op_count % 40 == 0:
                current_row += 1
                signal_screen.append([])
            op_count += 1
            crt_position = (op_count - 1) % 40
            if second_problem and crt_position in {x - 1, x, x + 1}:
                signal_screen[current_row].append("#")
                print(
                    f"During cycle  {op_count}: CRT draws pixel in position {crt_position}")
                print(f"Current CRT row: "
                      f"{''.join(signal_screen[current_row])}\n")
            else:
                signal_screen[current_row].append(".")
            if op_count == 20 or op_count % 40 == 20:
                signal_strength.append(x * op_count)

        for idx, line in enumerate(lines):
            cmd = line.split(" ")
            if second_problem:
                print_sprite_position(x)
            print(f"Start cycle   {op_count + 1}: begin executing "
                  f"{' '.join(cmd)}")
            if cmd[0][:3] == "add":
                step_and_check_signal()
                step_and_check_signal()
                x += int(cmd[1])
            else:
                step_and_check_signal()
        if second_problem:
            print_screen()
        return sum(signal_strength)


run = Solution()
print(run.signal_strength_calculator(False, False))
print(run.signal_strength_calculator(True, False))
print(run.signal_strength_calculator(False, True))
print(run.signal_strength_calculator(True, True))
