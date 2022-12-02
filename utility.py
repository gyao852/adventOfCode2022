from typing import Any


def parseInput(pathToFile: str) -> Any:
    """
    Helper function to parse files
    :param pathToFile: Patth to input file
    :return: Any. Parsed data
    """
    res = ""
    with open(pathToFile, 'r') as f:
        for line in f:
            res += line
    return res
