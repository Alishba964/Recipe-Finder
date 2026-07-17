# print("hello world")
import requests
import re
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY=os.getenv("API_KEY")

name=input("Enter name of food or main ingredients: ")
url=f"https://api.spoonacular.com/recipes/complexSearch?query={name}&maxFat=25&apiKey={API_KEY}"
response=requests.get(url)
data=response.json()
print(response.status_code)


print(data["results"][0]["title"])


id=data["results"][0]["id"]
details_url=f"https://api.spoonacular.com/recipes/{id}/information?apiKey={API_KEY}"
details_response=requests.get(details_url)
details=details_response.json()

print("READY IN MINUTES:", details["readyInMinutes"])
print("SERVINGS: ", details["servings"])
print("INGREDIENTS: ")
for i in details["extendedIngredients"]:
    print(i["originalName"]," | ",i["amount"], i["unit"])

desc = re.sub(r"<.*?>", "",details["summary"] )
print("DESCRIPTION: ",desc )
print("Dish Type: ", details["dishTypes"])
inst= re.sub(r"<.*?>", "",details["instructions"] )
print("INSTRUCTIONS ", inst)




# print("Recipe Name : ",data["results"][0]["title"])
# print("NUTRIENTS")
# print("NUTRIENT NAME : ",data["results"][0]["nutrition"]["nutrients"][0]["name"])
# print("NUTRIENT AMOUNT : ",data["results"][0]["nutrition"]["nutrients"][0]["amount"],data["results"][0]["nutrition"]["nutrients"][0]["unit"])