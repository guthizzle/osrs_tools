from math import floor
from accuracy.prayers_enum import MagicPrayer


class MagicAccuracy:
    def __init__(self):
        pass

    def calculate_mar(
        self,
        effective_level: float,
        magic_attack_bonus: int,
        task_salve: bool = False,
    ) -> float:
        """
        Calculate the Magic Attack roll (MAR).

        """
        mar = effective_level * (magic_attack_bonus + 64)
        if task_salve:
            mar *= 1.15

        return floor(mar)

    # TODO: add support for attack style bonuses
    def calculate_effective_level(
        self,
        magic_level: int,
        level_boost: int,
        prayer: MagicPrayer,
        void: bool = False,
    ) -> float:
        """
        Calculate the effective magic level.

        Args:
            magic_level (int): The player's magic level.
            level_boost (int): The level boost from equipment or potions.
            prayer (MagicPrayer): The active prayer affecting magic.
            void (bool): Whether the player is wearing Void Knight equipment.

        Returns:
            float: The effective magic level.
        """
        if not isinstance(prayer, MagicPrayer):
            raise ValueError(
                "Invalid prayer type. Must be an instance of MagicPrayer Enum."
            )

        effective_level = floor((magic_level + level_boost) * prayer.value)
        if void:
            effective_level = floor(effective_level * 1.45)
        effective_level += 9

        return effective_level

    def __str__(self) -> str:
        # TODO: implement string representation, we want to display the MAR, average hit and display of accuracy relevant stats.
        pass
