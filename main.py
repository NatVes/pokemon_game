import requests
import json
import random

# Get the list of pokemon from the API
url = "https://pokeapi.co/api/v2/pokemon?limit=10000"

response = requests.get(url)
pokemon_list = json.loads(response.text)["results"]

for pokemon in pokemon_list:
    print(pokemon["name"])
print(len(pokemon_list))
# Ask the user to choose a pokemon
print("Enter your pokemon:")

choice = input().lower()

# Get the pokemon's data from the API
url = f"https://pokeapi.co/api/v2/pokemon/{choice}/"
response = requests.get(url)
pokemon_data = json.loads(response.text)

# Get ability
abilities = pokemon_data["abilities"][0]
ability = abilities["ability"]

# Format height and weight
height = int(pokemon_data["height"])
weight = int(pokemon_data["weight"])

height_formatted = height / 10
weight_formatted = weight / 10

# Print pokemon data
print(f"Name: {pokemon_data['name']}")
print(f"Weight: {weight_formatted} (kgs)")
print(f"Height: {height_formatted} (m)")
print(f"Ability: {ability['name']}")

print("\nStats:")

for stat in pokemon_data["stats"]:
    stat_name = stat["stat"]["name"]
    stat_value = stat["base_stat"]
    print(f"{stat_name}: {stat_value}")

cpu_id = random.randint(1, 151)

url = f"https://pokeapi.co/api/v2/pokemon/{cpu_id}/"
response = requests.get(url)
cpu_pokemon_data = json.loads(response.text)
# Get CPU ability
cpu_abilities = cpu_pokemon_data["abilities"][0]
cpu_ability = cpu_abilities["ability"]

# Format CPU height and weight
cpu_height = int(cpu_pokemon_data["height"])
cpu_weight = int(cpu_pokemon_data["weight"])

cpu_height_formatted = cpu_height / 10
cpu_weight_formatted = cpu_weight / 10

# Print CPU pokemon data
print(f"Opponent's Pokemon: {cpu_pokemon_data['name']}")
print(f"Opponent Weight: {cpu_weight_formatted} (kgs)")
print(f"Opponent Height: {cpu_height_formatted} (m)")
print(f"Opponent Ability: {cpu_ability['name']}")


