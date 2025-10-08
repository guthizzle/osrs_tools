from enum import Enum


# TODO: VALUES
class RangePrayer(Enum):
    SHARP_EYE = "Sharp Eye"
    HAWK_EYE = "Hawk Eye"
    EAGLE_EYE = "Eagle Eye"
    RIGOUR = "Rigour"


class MagicPrayer(Enum):
    NONE = 1.0
    MYSTIC_WILL = 1.05
    MYSTIC_LORE = 1.10
    MYSTIC_MIGHT = 1.15
    AUGURY = 1.25


# TODO: VALUES
class AttackPrayer(Enum):
    CLARITY_OF_THOUGHT = "Clarity of Thought"
    IMPROVED_REFLEXES = "Improved Reflexes"
    INCREDIBLE_REFLEXES = "Incredible Reflexes"
    CHIVALRY_ATTACK = "Chivalry (Attack)"
    PIETY_ATTACK = "Piety (Attack)"


# TODO: VALUES
class StrengthPrayer(Enum):
    BURST_OF_STRENGTH = "Burst of Strength"
    SUPERHUMAN_STRENGTH = "Superhuman Strength"
    ULTIMATE_STRENGTH = "Ultimate Strength"
    CHIVALRY_STRENGTH = "Chivalry (Strength)"
    PIETY_STRENGTH = "Piety (Strength)"
