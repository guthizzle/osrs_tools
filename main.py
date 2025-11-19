import specs.dps_spec as dpsSpecs


def main():
    main_dps = 11.215

    vw_dps = 25
    vw_hit = 60.0

    claw_dps = 22.964
    claw_hit = 55.1

    burn_claw_dps = 22.188
    burn_claw_hit = 53.3

    spec = dpsSpecs.DpsSpec(
        spec_dps=vw_dps,
        spec_dmg=vw_hit,
        attack_speed=2.4,
        spec_cost=50,
        target_hitpoints=750,
        main_dps=main_dps,
    )
    print("VW spec")
    print(spec)

    spec.set_spec(
        spec_dps=claw_dps,
        spec_dmg=claw_hit,
        attack_speed=2.4,
        spec_cost=50,
    )
    print("Claw spec")
    print(spec)

    spec.set_spec(
        spec_dps=burn_claw_dps,
        spec_dmg=burn_claw_hit,
        attack_speed=2.4,
        spec_cost=30,
    )
    print("Burn claw spec")
    print(spec)


if __name__ == "__main__":
    main()
