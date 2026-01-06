import requests
from pydantic import BaseModel


def pegar_pokemon(id: int) -> PokemonSchame:
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
    data = response.json()
    datatypes = data["types"]
    types_list = []
    for type_info in datatypes:
        types_list.append(type_info["type"]["name"])
    types = ", ".join(types_list)
    pokemon = PokemonSchame(name=data["name"], type=types)
    return pokemon


if __name__ == "__main__":
    print(pegar_pokemon(10))
    print(pegar_pokemon(25))
    print(pegar_pokemon(150))
