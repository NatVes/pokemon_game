def battle(player, cpu):  # Function that takes two Pokémon data objects (player and cpu)

    player_stats = {}  # empy dict

    for stat in player["stats"]:  # loop start of player stats
        stat_name = stat["stat"]["name"]  # extract stat name
        stat_value = stat["base_stat"]  # extract value of that stat
        player_stats[stat_name] = stat_value  # stores stat in dictionary (e.g. {"attack": 55})

    cpu_stats = {}

    for stat in cpu["stats"]:
        stat_name = stat["stat"]["name"]
        stat_value = stat["base_stat"]
        cpu_stats[stat_name] = stat_value

    player_attack = player_stats["attack"] - cpu_stats["defense"]  # calc player physical attack vs cpu defense
    cpu_attack = cpu_stats["attack"] - player_stats["defense"]  # inverted

    player_special = player_stats["special-attack"] - cpu_stats["special-defense"]  # players special attack vs cpu spd
    cpu_special = cpu_stats["special-attack"] - player_stats["special-defense"]  # inverted

    player_speed = player_stats["speed"] - cpu_stats["speed"] #speed difference
    cpu_speed = cpu_stats["speed"] - player_stats["speed"]

    player_hp = player_stats["hp"] - cpu_stats["hp"] #hp difference
    cpu_hp = cpu_stats["hp"] - player_stats["hp"]

    player_power = max(player_attack, 0) + max(player_special, 0) + max(player_speed, 0) + max(player_hp, 0)
    cpu_power = max(cpu_attack, 0) + max(cpu_special, 0) + max(cpu_speed, 0) + max(cpu_hp, 0)
    #power is a calculation of the attack vs defense and spa vs spd as well as speed and hp difference
    #the pokemon with the highest power wins
    print(f"Player power: {player_power}")
    print(f"CPU power: {cpu_power}")

    if player_power > cpu_power:
        print("Player wins!")
    elif cpu_power > player_power:
        print("CPU wins!")
    else:
        print("It's a draw!")