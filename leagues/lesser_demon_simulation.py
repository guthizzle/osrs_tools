import accuracy.magic_accuracy as ma
import random
from typing import Tuple


def hit_chance(mar: float, mdr: float) -> float:
    if mar > mdr:
        return 1 - (mdr + 2) / (2 * (mar + 1))
    else:
        return mar / (2 * (mdr + 1))


def roll_hit(mar: float, mdr: float, max_hit: int) -> int:
    """Roll whether an attack hits and how much damage it deals.

    Args:
        mar: Magic Attack Roll
        mdr: Monster Defense Roll
        max_hit: Maximum hit potential

    Returns damage (1,1,..max_hit)
    """
    chance = hit_chance(mar, mdr)
    rng = random.random()
    if rng <= chance:
        dmg = random.randint(0, max_hit)
        return 1 if dmg == 0 else dmg
    return 0


def define_xp_table() -> list[int]:
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


def check_level(xp: float, xp_table: list[int]) -> int:
    level = 1

    for lvl in range(1, len(xp_table) + 1):
        required = xp_table[lvl - 1]
        if xp >= required:
            level = lvl
        else:
            break

    return level


def check_xp(level: int, xp_table: list[int]) -> int:
    """
    Given a level, return the cumulative XP required for that level.

    Args:
        level (int): The level to check (1-99).

    Returns:
        int: The cumulative XP required for the given level.

    Raises:
        ValueError: If the level is out of bounds (less than 1 or greater than 99).

    """
    for lvl in range(1, len(xp_table) + 1):
        if lvl == level:
            return xp_table[lvl - 1]
        elif lvl > level:  # if level's too small
            raise ValueError(f"Level {level} is out of bounds for the XP table.")
        elif level > len(xp_table):  # if level's too high
            raise ValueError(f"Level {level} is out of bounds for the XP table.")


def simulate_kill(
    monster_hp: int,
    start_magic_level: int = 1,
    start_max_hit: int = 1,
    xp_per_cast: float = 5.5,
    xp_multiplier: float = 1.0,
    magic_attack_bonus: int = 0,
    mdr: float = 540,
    seed: int | None = None,
) -> Tuple[int, int]:
    """
    Simulate casting until the monster is dead.

    Args:
        monster_hp (int): The hitpoints of the monster to be
        start_magic_level (int): The starting magic level of the player.
        start_max_hit (int): The starting maximum hit of the player.
        xp_per_cast (float): The experience gained per cast.
        xp_multiplier (float): Multiplier for experience gained.
        magic_attack_bonus (int): The magic attack bonus of the player.
        mdr (float): The monster's defense roll.
        seed (int | None): Seed for random number generator for reproducibility.

    Returns:
        Tuple[int, int]: Number of casts to kill & final magic level


    """
    if seed is not None:
        random.seed(seed)

    acc = ma.MagicAccuracy()

    xp_table = define_xp_table()

    casts = 0
    xp = check_xp(start_magic_level, xp_table)  # total cumulative XP in the magic skill
    magic_level = start_magic_level
    max_hit = start_max_hit

    # compute initial effective level and MAR
    eLvl = acc.calculate_effective_level(
        magic_level=magic_level,
        level_boost=0,
        prayer=ma.MagicPrayer.NONE,
        void=False,
    )
    mar = acc.calculate_mar(
        effective_level=eLvl,
        magic_attack_bonus=magic_attack_bonus,
        task_salve=False,
    )

    hp = monster_hp

    while hp > 0:
        magic_level = check_level(xp, xp_table)

        if magic_level < 4:
            max_hit = 2
        elif magic_level < 9:
            max_hit = 4
        elif magic_level < 13:
            max_hit = 6
        else:
            max_hit = 8

        eLvl = acc.calculate_effective_level(
            magic_level=magic_level,
            level_boost=0,
            prayer=ma.MagicPrayer.NONE,
            void=False,
        )
        mar = acc.calculate_mar(
            effective_level=eLvl,
            magic_attack_bonus=magic_attack_bonus,
            task_salve=False,
        )

        # roll hit
        dmg = roll_hit(mar, mdr, max_hit)
        hp -= dmg

        # gain xp
        dmg_xp = dmg * 2 * xp_multiplier
        xp += xp_per_cast * xp_multiplier + dmg_xp

        casts += 1

    return casts, magic_level


def simulate(rounds: int = 1000, xp_multiplier: float = 5):
    total_casts = 0
    final_levels = []

    for _ in range(rounds):
        casts, final_lvl = simulate_kill(
            monster_hp=79,
            start_magic_level=1,
            start_max_hit=2,
            xp_per_cast=5.5,
            xp_multiplier=xp_multiplier,
            mdr=540,
            seed=None,  # Different seed for each simulation
        )
        total_casts += casts
        final_levels.append(final_lvl)

    avg_casts = total_casts / rounds
    avg_final_level = sum(final_levels) / rounds

    print("-----------------------------------")
    print("Simulation Results:")
    print(f"XP Multiplier: {xp_multiplier}")
    print(f"Average casts to kill over {rounds} rounds: {avg_casts}")
    print(f"Average final level: {avg_final_level}")
    print("-----------------------------------")


if __name__ == "__main__":
    simulate(rounds=100000, xp_multiplier=5)
    simulate(rounds=100000, xp_multiplier=16)
