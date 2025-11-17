import requests
from curl import Urls  

def fetch_ingredients():
    url = f"{Urls.BASE_PAGE}/api/ingredients"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json().get("data", [])

    BUNS, SAUCES, FILLINGS = [], [], []

    for item in data:
        ingredient = {"id": item["_id"], "name": item["name"], "type": item["type"]}
        if item["type"] == "bun":
            BUNS.append(ingredient)
        elif item["type"] == "sauce":
            SAUCES.append(ingredient)
        else:
            FILLINGS.append(ingredient)

    INGREDIENTS = BUNS + SAUCES + FILLINGS
    return BUNS, SAUCES, FILLINGS, INGREDIENTS
