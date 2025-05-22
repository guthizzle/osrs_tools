import specs.dps_spec as dpsSpecs


def main():
    main_dps = 10.17482

    vw_dps = 22.5
    vw_hit = 52.5

    claw_dps = 25.96198
    claw_hit = 60.80876

    burn_claw_dps = 20.70089
    burn_claw_hit = 48.18214

    spec = dpsSpecs.DpsSpec(
        spec_dps=vw_dps,
        spec_dmg=vw_hit,
        attack_speed=2.4,
        spec_cost=50,
        target_hitpoints=700,
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
