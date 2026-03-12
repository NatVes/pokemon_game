import requests
import json
import random

def get_pokemon_data(choice):
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(choice)
    response = requests.get(url)
    pokemon_data = json.loads(response.text)

    # to get ability
    abilities = pokemon_data['abilities'][0]
    ability = abilities['ability']['name']

    # to format height and weight properly
    height = int(pokemon_data['height'])
    weight = int(pokemon_data['weight'])

    height_formatted = height / 10
    weight_formatted = weight / 10

    stats = {}
    for stat in pokemon_data["stats"]:
        stat_name = stat["stat"]["name"]
        stat_value = stat["base_stat"]
        stats[stat_name] = stat_value

    return {
        "name": pokemon_data["name"],
        "ability": ability,
        "height": height_formatted,
        "weight": weight_formatted,
        "stats": stats
    }

def print_pokemon_data(pokemon):
    print(f"""Name: {pokemon["name"]}
Weight: {pokemon["weight"]}
Height: {pokemon["height"]}
Ability: {pokemon["ability"]}

        STATS:
            """)
    for stat, value in pokemon["stats"].items():
        print(f"{stat}: {value}")

# Get the list of pokemon from the API
url = 'https://pokeapi.co/api/v2/pokemon/'
response = requests.get(url)
pokemon_list = json.loads(response.text)['results']
pokemon_names = []

for pokemon in pokemon_list:
    pokemon_names.append(pokemon["name"])

print(pokemon_names)

# Ask the user to choose a pokemon
print('Enter your pokemon: ')

# Get the user's choice
user_choice = input().lower()

# Get the user's pokemon's data from the API and print it
print("Your choice:")
player_pokemon = get_pokemon_data(user_choice)
print_pokemon_data(player_pokemon)

# CPU chooses a random Pokemon
cpu_choice = random.choice(pokemon_names)

# Get the CPU's pokemon's data from the API and print it
print("\nCPU choice:")
cpu_pokemon = get_pokemon_data(cpu_choice)
print_pokemon_data(cpu_pokemon)

# Battle
def battle(player_pokemon, cpu_pokemon):
    player_hp = player_pokemon['stats']['hp']
    cpu_hp = cpu_pokemon['stats']['hp']

    player_attack = player_pokemon['stats']['attack']
    cpu_attack = cpu_pokemon['stats']['attack']

    player_defense = player_pokemon['stats']['defense']
    cpu_defense = cpu_pokemon['stats']['defense']

    print(f"\n⚔️ Battle: {player_pokemon['name'].title()} vs {cpu_pokemon['name'].title()}!⚔️\n")

    round_number = 1

    while player_hp > 0 and cpu_hp > 0:
        print(f"--- Round {round_number} ---")
        # player attack
        damage_to_cpu = player_attack - cpu_defense
        if damage_to_cpu < 1:
            damage_to_cpu = 1

        cpu_hp -= damage_to_cpu

        print(f"{player_pokemon['name'].title()} deals {damage_to_cpu} damage!")

        if cpu_hp <= 0:
            break

        # cpu attack
        damage_to_player = cpu_attack - player_defense
        if damage_to_player < 1:
            damage_to_player = 1

        player_hp -= damage_to_player

        print(f"{cpu_pokemon['name'].title()} deals {damage_to_player} damage!")

        print(f"HP: {player_pokemon['name'].title()} = {player_hp} | {cpu_pokemon['name'].title()} = {cpu_hp}\n")

        round_number += 1

    if player_hp > 0:
        print(f"🏆 {player_pokemon['name'].title()} wins!")
    else:
        print(f"🏆 {cpu_pokemon['name'].title()} wins!")


battle(player_pokemon, cpu_pokemon)
