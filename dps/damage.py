import random


def _hit_chance(attRoll: float, defRoll: float) -> float:
    """
    Calculate the hit chance based on attack roll and defense roll.
    Private function used internally.
    From https://oldschool.runescape.wiki/w/Accuracy#Formulas

    Args:
        attRoll (float): Attack Roll
        defRoll (float): Monster Defense Roll

    Returns:
        float: The probability of a successful hit (between 0 and 1).

    Raises:
        ValueError: If attRoll or defRoll is negative.
    """
    if attRoll < 0 or defRoll < 0:
        raise ValueError("Attack roll and defense roll must be non-negative.")

    if attRoll > defRoll:
        return 1 - (defRoll + 2) / (2 * (attRoll + 1))
    else:
        return attRoll / (2 * (defRoll + 1))


def roll_hit(attRoll: float, defRoll: float, max_hit: int) -> int:
    """
    Roll whether an attack hits and how much damage it deals.
    Used mostly for simulations.

    Args:
        attRoll (float): Attack Roll
        defRoll (float): Monster Defense Roll
        max_hit (int): Maximum hit potential

    Returns:
        int: Damage dealt (1, 1, ..., max_hit) or 0 if the attack misses.
    """
    chance = _hit_chance(attRoll, defRoll)
    rng = random.random()
    if rng <= chance:
        dmg = random.randint(0, max_hit)
        return 1 if dmg == 0 else dmg
    return 0
