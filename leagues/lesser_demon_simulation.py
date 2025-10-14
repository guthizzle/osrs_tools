import random
import utils.xp_table as exp
import dps.damage as dmg
import accuracy.magic_accuracy as ma
from typing import Tuple


# Potentially separate into its own simulation module? - unsure if overkill since its pretty specific
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

    xp_table = exp.generate_xp_table()

    casts = 0
    xp = exp.get_xp(
        start_magic_level, xp_table
    )  # total cumulative XP in the magic skill
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
        magic_level = exp.get_level(xp, xp_table)

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
        dam = dmg.roll_hit(mar, mdr, max_hit)
        hp -= dam

        # gain xp
        dam_xp = dam * 2 * xp_multiplier
        xp += xp_per_cast * xp_multiplier + dam_xp

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
    # simulate(rounds=100000, xp_multiplier=16)
