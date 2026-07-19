import requests
import re
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY=os.getenv("API_KEY")
def search_recipes(query):
    name=input("Enter name of food or main ingredients: ")
    url=f"https://api.spoonacular.com/recipes/complexSearch?query={name}&maxFat=25&apiKey={API_KEY}"
    response=requests.get(url)
    data=response.json()

    if (response.status_code != 200):
        print("API ERROR")
        print(response.text)
        exit()

    if not data["results"]:
        print("No Recipes Found")
        exit()
    
    return data.get("results", [])

    # name=input("Enter name of food or main ingredients: ")
##url=f"https://api.spoonacular.com/recipes/complexSearch?query={name}&maxFat=25&apiKey={API_KEY}"
# response=requests.get(url)
# data=response.json()

# if (response.status_code != 200):
#     print("API ERROR")
#     print(response.text)
#     exit()

# if not data["results"]:
#     print("No Recipes Found")
#     exit()

for index , recipe in enumerate(data["results"]):
    print(f"{index+1}. {recipe['title']}")

print("--------------------------------------")
dish = int(input("Enter a Dish Number: "))
if dish < 1 or dish > len(data["results"]):
    print("Invalid recipe number.")
    exit()
selected_recipe = data["results"][dish - 1]
recipe_id = selected_recipe["id"]

# id=data["results"][0]["id"]
details_url=f"https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={API_KEY}"
details_response=requests.get(details_url)
if details_response.status_code != 200:
    print("Failed to fetch recipe details.")
    print(details_response.text)
    exit()
details=details_response.json()

print("-----------------------------------------")
print("                DETAILS                  ")
print("-----------------------------------------")
print("READY IN MINUTES:", details.get("readyInMinutes"),"Not Available")
print("SERVINGS: ", details.get("servings","Not Available"))
print("-----------------------------------------")
print("               INGREDIENTS               ")
print("-----------------------------------------")

for index ,i in enumerate(details["extendedIngredients"]):
    print(index+1,". ",i.get("originalName","Unknown")," ( ",i.get("amount",""), i.get("unit","")," ) ")

print("-----------------------------------------")
print("             DESCRIPTION                 ")
print("-----------------------------------------")
summary = details.get("summary")
if summary:
    summary = re.sub(r"<.*?>", "", summary)
else:
    summary="No Description Available!"

print("Description : ",summary)

print("-----------------------------------------")
print("              INSTRUCTIONS               ")
print("-----------------------------------------")

instructions = details.get("instructions")

if instructions:
    instructions = re.sub(r"<.*?>", "", instructions)
    print(instructions)
else:
    print("Instructions not available.")

print("-----------------------------------------")
dish_types = details.get("dishTypes", [])
print("Dish Type.......")
if dish_types:
    print("\n".join(dish_types))
else:
    print("Dish Type: Not Available")


print("Health Score : ", details.get("healthScore","Not Available"))

print("Source Website:", details.get("sourceUrl", "Not Available"))
print("Image:", details.get("image", "Not Available"))

cuisines = details.get("cuisines", [])
print("Cuisine ..........")
if cuisines:
    print("\n".join(cuisines))
else:
    print("Cuisine: Not Available")


print("-----------------------------------------")
print("            DIET INFORMATION             ")
print("-----------------------------------------")
print("Vegetarian :", "Yes" if details.get("vegetarian") else "No")
print("Vegan      :", "Yes" if details.get("vegan") else "No")
print("Gluten Free:", "Yes" if details.get("glutenFree") else "No")
print("Dairy Free :", "Yes" if details.get("dairyFree") else "No")

