# imports:
import requests
from pprint import pprint
# initial user imputs:
ingredient = input("What do you have in your fridge? ")
allergy_check = input("Do you have any allergies/intolerances? y/n ")
# Lists: 
allergy_list = ['Alcohol-Cocktail', 'Alcohol-Free', 'Celery-Free', 'Crustcean-Free', 'Dairy-Free', 'DASH', 'Egg-Free', 'Fish-Free', 'FODMAP-Free', 'Gluten-Free', 'Immuno-Supportive', 'Keto-Friendly', 'Kidney-Friendly', 'Kosher','Low Potassium', 'Low Sugar', 'Lupine-Free', 'Mediterranean', 'Mollusk-Free', 'Mustard-Free', 'No oil added', 'Paleo', 'Peanut-Free', 'Pescatarian', 'Pork-Free', 'Red-Meat-Free', 'Sesame-Free', 'Shellfish-Free', 'Soy-Free', 'Sugar-Conscious', 'Sulfite-Free', 'Tree-Nut-Free', 'Vegan', 'Vegetarian', 'Wheat-Free']
allergy_res_all = [] # empty list (allergy results from search - all)
# defined function:
def recipe_search(ingredient):
    response = requests.get(url)
    search_results = response.json()  # unpacking the recipe data
    return search_results['hits']

if allergy_check == "y":
    for allergy in allergy_list:
        print(allergy)
    user_allergy = input("From the above list, Please tell me you allergies/intolerances: ")
    url = "https://api.edamam.com/search?q={}&app_id=04806c2d&app_key=460981b3543f17528da3500df67511c8&health{}".format(
        ingredient, user_allergy)
    search_results = recipe_search(ingredient)
    for result in search_results:
        recipe = result['recipe']
        recipe_name = recipe['label']
        rurl = recipe['uri']
        allergy_warning = recipe['healthLabels']
        allergy_res_all = allergy_res_all + allergy_warning #makes a list of all allergy outputs
        if user_allergy in allergy_warning:  # will only print recipes if your allergy is in the list
            print(recipe['label'])
            print(recipe['uri'])
            print(recipe['healthLabels'])
    if user_allergy not in allergy_res_all:
        print('There are no recipes that fit your criteria')

if allergy_check == "n":
    url = "https://api.edamam.com/search?q={}&app_id=04806c2d&app_key=460981b3543f17528da3500df67511c8".format(
        ingredient)
    search_results = recipe_search(ingredient)
    for result in search_results:
        recipe = result['recipe']
        recipe_name = recipe['label']
        rurl = recipe['uri']
        print(recipe['label'])
        print(recipe['uri'])
        print(recipe['healthLabels'])
