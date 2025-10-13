"""
Utility functions for handling experience points (XP) and levels in a game.

Functions:
- generate_xp_table: Generates the XP table for levels 1 to 99.
- get_xp: Returns the cumulative XP required for a given level.
- get_level: Returns the level corresponding to a given XP amount.

"""


def generate_xp_table() -> list[int]:
    """
    Define and return the XP table for levels 1 to 99.

    Returns:
        list[int]: A list where the index represents the level and the value at that index represents the cumulative XP required for that level.
    """
    xp_table = [0]  # xp required for level 1 = 0
    cumulative = 0
    for lvl in range(1, 100):
        increment = int((lvl + 300 * (2 ** (lvl / 7.0))) // 1)
        cumulative += increment
        xp_table.append(cumulative // 4)  # OSRS uses cumulative/4
    return xp_table


def get_xp(level: int, xp_table: list[int]) -> float:
    """
    Given a level, return the cumulative XP required for that level.

    Args:
        level (int): The level to check (1-99).
        xp_table (list[int]): The XP table to reference.

    Returns:
        float: The cumulative XP required for the given level, or 0.0 if the level is out of bounds.

    Raises:
        ValueError: If the level is out of bounds (less than 1 or greater than 99).
    """
    if 1 <= level < len(xp_table):
        return float(xp_table[level])
    elif level >= len(xp_table):
        raise ValueError(f"Level {level} is out of bounds for the XP table.")
    elif level < 1:
        raise ValueError(f"Level {level} is out of bounds for the XP table.")
    return 0.0


def get_level(xp: float, xp_table: list[int]) -> int:
    """
    Given an XP amount, return the corresponding level.

    Args:
        xp (float): The XP amount to check.
        xp_table (list[int]): The XP table to reference.

    Returns:
        int: The level corresponding to the given XP amount.
    """

    level = 1

    for lvl in range(1, len(xp_table) + 1):
        required = xp_table[lvl - 1]
        if xp >= required:
            level = lvl
        else:
            break

    return level
