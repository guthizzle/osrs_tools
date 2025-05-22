# TODO: later down the line we should refactor this to take in variables such as accuracy, expected hit etc
# this will be useful when we make a dps calculator accuracy module etc.


class DpsSpec:
    """
    DpsSpec is a utility class for calculating the effectiveness of special attacks (specs)
    in a combat system based on various metrics like damage, speed, cost, and time saved.

    Usage:
    ------
    1. Initialize the class with the spec's DPS, expected damage, attack speed, and cost:
        `spec = DpsSpec(spec_dps=100.0, spec_dmg=200.0, attack_speed=2.0, spec_cost=50)`

    2. Set the target context to define the opponent's hitpoints and the player's base DPS:
        `spec.set_target(target_hitpoints=1000.0, main_dps=50.0)`

    3. Access calculated properties:
        - spec.ttk                        # Time to kill without spec
        - spec.spec_efficiency           # DPS per cost
        - spec.spec_time_save            # Time saved using the spec
        - spec.spec_time_save_efficiency # Time saved per cost

    4. Update spec parameters at any time using:
        `spec.set_spec(spec_dps=150.0, spec_dmg=300.0, attack_speed=1.5, spec_cost=75)`

    Notes:
    ------
    - Internally calculates values like efficiency and time saved whenever values are set.
    - Intended for use in combat calculators, future integration with accuracy/hit chance modules.
    - All metrics are based on expected damage and average DPS; randomness or hit chance is not yet included.

    Example:
    --------
    `spec = DpsSpec(spec_dps=120, spec_dmg=240, attack_speed=2.4, spec_cost=60)`

    `spec.set_target(target_hitpoints=960, main_dps=40)`

    `print(spec.spec_time_save)  # Time saved using spec`
    """

    def __init__(
        self,
        spec_dps: float = 0.0,
        spec_dmg: float = 0.0,
        attack_speed: float = 0.0,
        spec_cost: int = 0,
        target_hitpoints: float = 0.0,
        main_dps: float = 0.0,
    ) -> None:
        """
        Initialise the DpsSpec object with spec damage per second (DPS), expected damage, attack speed, and cost.

        Args:
            spec_dps (float): The damage per second of the spec.
            spec_dmg (float): The expected damage of the spec.
            attack_speed (float): The attack speed of the spec (in seconds).
            spec_cost (int): The cost of the spec.
        """
        self.spec_dps = spec_dps
        self.spec_dmg = spec_dmg
        self.attack_speed = attack_speed
        self.spec_cost = spec_cost

        self.target_hitpoints = target_hitpoints
        self.main_dps = main_dps

        self._update_ttk()
        self._update_efficiency()
        self._update_time_save()
        self._update_time_efficiency()

    def _update_efficiency(self) -> None:
        """
        Update the efficiency of the spec based on its damage per second (DPS) and cost.

        This method is called internally to recalculate the efficiency whenever the spec's attributes change.
        """
        self.spec_efficiency = self.spec_dps / self.spec_cost if self.spec_cost else 0

    def _update_time_save(self) -> None:
        """
        Update the time saved by using the spec based on its damage, attack speed, and hitpoints.

        This method is called internally to recalculate the time saved whenever the spec's attributes change.
        """
        if self.target_hitpoints != 0 and self.main_dps != 0:
            # Calculate ttk if target hitpoints and main dps are set, else set to 0
            new_hitpoints = self.target_hitpoints - self.spec_dmg
            new_ttk = new_hitpoints / self.main_dps + self.attack_speed
            self.spec_time_save = self.ttk - new_ttk
        else:
            self.spec_time_save = 0.0

    def _update_time_efficiency(self) -> None:
        """
        Update the time efficiency of the spec based on its time saved and cost.

        This method is called internally to recalculate the time efficiency whenever the spec's attributes change.
        """
        self.spec_time_save_efficiency = (
            self.spec_time_save / self.spec_cost if self.spec_cost else 0
        )

    def _update_ttk(self) -> None:
        """
        Update the time to kill (TTK) based on the target's hitpoints and main DPS.

        This method is called internally to recalculate the TTK whenever the target's hitpoints or main DPS changes.
        """
        self.ttk = self.target_hitpoints / self.main_dps if self.main_dps else 0

    def set_spec(
        self, spec_dps: float, spec_dmg: float, attack_speed: float, spec_cost: int
    ) -> None:
        """
        Set the spec's damage per second (DPS), attack speed, and cost.

        Args:
            spec_dps (float): The damage per second of the spec.
            spec_dmg (float): The expected damage of the spec.
            attack_speed (float): The attack speed of the spec (in seconds).
            spec_cost (int): The cost of the spec.

        Returns:
            None: The spec's attributes are updated in the instance.
        """
        self.spec_dps = spec_dps
        self.spec_dmg = spec_dmg
        self.attack_speed = attack_speed
        self.spec_cost = spec_cost

        self._update_ttk()
        self._update_efficiency()
        self._update_time_save()
        self._update_time_efficiency()

    def set_target(self, target_hitpoints: float, main_dps: float) -> None:
        """
        Define the target's hitpoints for the spec calculation.

        Args:
            target_hitpoints (float): The hitpoints of the target.
            main_dps (float): The main damage per second (DPS) of the player.

        Returns:
            None: The target's hitpoints is stored in the instance variable.
        """
        self.target_hitpoints = target_hitpoints
        self.main_dps = main_dps

        self._update_ttk()
        self._update_efficiency()
        self._update_time_save()
        self._update_time_efficiency()

    @staticmethod
    def get_marginal_dps(main_dps: float, spec_dps: float) -> float:
        """
        Calculate the marginal DPS of a spec based on the main DPS and spec DPS.

        Helper function to calculate the marginal DPS of a spec.
        This is a static method and can be called without creating an instance of the class.

        Args:
            main_dps (float): The main damage per second (DPS).
            spec_dps (float): The damage per second (DPS) of the spec.

        Returns:
            float: The marginal DPS, calculated as the difference between spec DPS and main DPS.
        """
        return spec_dps - main_dps

    @staticmethod
    def calc_spec_efficiency(spec_dps: float, spec_cost: int) -> float:
        """
        Calculate the efficiency of a spec based on its damage per second (DPS) and cost.

        Helper function to calculate the efficiency of a spec.
        This is a static method and can be called without creating an instance of the class.

        Args:
            spec_dps (float): The damage per second of the spec.
            spec_cost (int): The cost of the spec.

        Returns:
            float: The efficiency of the spec, calculated as DPS divided by cost.
        """
        return spec_dps / spec_cost

    def __str__(self) -> str:
        return (
            f"\n------------------------\n"
            f"DPS Spec:\n"
            f"  DPS: {self.spec_dps:.5f}\n"
            f"  Expected Damage: {self.spec_dmg:.5f}\n"
            f"  Attack Speed: {self.attack_speed:.2f}s\n"
            f"  Cost: {self.spec_cost}\n"
            f"  Damage Efficiency: {self.spec_efficiency:.5f}\n"
            f"  Time Save: {self.spec_time_save:.2f}s\n"
            f"  Time Efficiency: {self.spec_time_save_efficiency:.5f}"
            f"\n------------------------\n"
        )


if __name__ == "__main__":
    # Example usage
    # Spec 1
    spec = DpsSpec(spec_dps=100.0, spec_dmg=200.0, attack_speed=2.0, spec_cost=50)
    spec.set_target(target_hitpoints=1000.0, main_dps=50.0)
    print(spec)

    # spec 2
    spec.set_spec(spec_dps=150.0, spec_dmg=300.0, attack_speed=1.5, spec_cost=75)
    spec.set_target(target_hitpoints=1200.0, main_dps=60.0)
    print(spec)
