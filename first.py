import requests
import re
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY=os.getenv("API_KEY")


def search_recipes(query):
    url=f"https://api.spoonacular.com/recipes/complexSearch?query={query}&maxFat=25&apiKey={API_KEY}"
    response=requests.get(url)
    data=response.json()

    if (response.status_code != 200):
        
        return None

    if not data["results"]:
        return []
    
    recipes = []
    for recipe in data["results"]:
        recipe_info = {
            "id" : recipe.get("id"),
            "title": recipe.get("title"),
            "image" : recipe.get("image")
        }
        recipes.append(recipe_info)
    
    return recipes


def get_recipe_details(recipe_id):
    details_url=f"https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={API_KEY}"
    details_response=requests.get(details_url)
    if details_response.status_code != 200:
        return None
    details=details_response.json()

    summary = details.get("summary")
    if summary:
        summary = re.sub(r"<.*?>", "", summary)
    else:
        summary="No Description Available!"


    instructions = details.get("instructions")
    if instructions:
        instructions = re.sub(r"<.*?>", "", instructions)
        
    else:
        instructions="No Instructions Available!"

    ingredients = []
    for ingredient in details.get("extendedIngredients", []):
        ingredient_string = (
        f"{ingredient.get('originalName', 'Unknown')} "
        f"({ingredient.get('amount', '')} {ingredient.get('unit', '')})"
    )
        ingredients.append(ingredient_string)
    
    recipe = {}   
    recipe["title"] = details.get("title", "Unknown Recipe")
    recipe["image"] = details.get("image", "NotAvailable")
    recipe["summary"] = summary
    recipe["instructions"] = instructions
    recipe["ingredients"] = ingredients
    recipe["readyInMinutes"] = details.get("readyInMinutes", "NotAvailable")
    recipe["servings"] = details.get("servings", "NotAvailable")
    recipe["healthscore"] = details.get("healthScore", "NotAvailable")
    recipe["dishTypes"] = ", ".join(details.get("dishTypes", []))
    recipe["cuisines"] = ", ".join(details.get("cuisines", []))
    recipe["vegetarian"] = "Yes" if details.get("vegetarian") else "No"
    recipe["vegan"] = "Yes" if details.get("vegan") else "No"
    recipe["glutenFree"] = "Yes" if details.get("glutenFree") else "No"
    recipe["dairyFree"] = "Yes" if details.get("dairyFree") else "No"
    recipe["sourceUrl"] = details.get("sourceUrl", "NotAvailable")
    return recipe


