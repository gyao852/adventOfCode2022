from utility import parseInput


class Solution:
    BASE_POINTS = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }
    ROUND_POINTS = {
        'AX': 3,
        'AY': 6,
        'AZ': 0,
        'BX': 0,
        'BY': 3,
        'BZ': 6,
        'CX': 6,
        'CY': 0,
        'CZ': 3,
    }

    BASE_POINTS_2 = {
        'X': 0,
        'Y': 3,
        'Z': 6,
    }
    ROUND_POINTS_2 = {
        'AX': BASE_POINTS['Z'],
        'AY': BASE_POINTS['X'],
        'AZ': BASE_POINTS['Y'],
        'BX': BASE_POINTS['X'],
        'BY': BASE_POINTS['Y'],
        'BZ': BASE_POINTS['Z'],
        'CX': BASE_POINTS['Y'],
        'CY': BASE_POINTS['Z'],
        'CZ': BASE_POINTS['X'],
    }

    def points_from_strategy(self, use_real_input: bool = False) -> int:
        """
        Returns the most total Calories
        carried by an elf
        :param use_real_input: bool. Use real data if true, else test data
        :return: int. Maximum calories
        """
        data = parseInput("test.txt") if not use_real_input else parseInput("real.txt")
        game_rounds = [game_round.split(" ") for game_round in data.split("\n")]
        res = 0
        # Just use hashmap and return results
        for game in game_rounds:
            res += self.BASE_POINTS[game[1]]
            res += self.ROUND_POINTS[game[0] + game[1]]
        return res

    def points_from_strategy_2(self, use_real_input: bool = False) -> int:
        """
        Returns the most total Calories
        carried by an elf
        :param use_real_input: bool. Use real data if true, else test data
        :return: int. Maximum calories
        """
        data = parseInput("test.txt") if not use_real_input else parseInput("real.txt")
        game_rounds = [game_round.split(" ") for game_round in data.split("\n")]
        res = 0
        # Just use hashmap and return results
        for game in game_rounds:
            res += self.BASE_POINTS_2[game[1]]
            res += self.ROUND_POINTS_2[game[0] + game[1]]
        return res


run = Solution()
print(run.points_from_strategy(True))
print(run.points_from_strategy_2(True))
