import requests
def fetch(name):
    s_url = "https://pokeapi.co/api/v2/pokemon" 
    response = requests.get(f"{s_url}/{name}")
    if response.status_code == 200:
        api_data = response.json()
        return  api_data
    else:
        print("There was an issue getting the data of API")

# name="pikachu"
# name = "ditto"
name = "typhlosion"
data =  fetch(name)
if data:
    print ( f"Name:  {data['name']} " )
    print ( f"Height:  {data['height']} " )
    print ( f"Weight: {data['weight']} " )
    print ( f"GameIndex:  {data['game_indices'][7]['game_index']} " )  #pokemon usually do not have more than 8 indices