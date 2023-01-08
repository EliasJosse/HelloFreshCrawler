#!/usr/bin/env python
# coding: utf-8


import requests
import Recipe
from bs4 import BeautifulSoup



def URL_To_Soup(URL) :

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser", multi_valued_attributes=None)

    return soup

#Gather all recipe links on page
def get_Recipe_Links(soup) :
    links = [tag_a.get('href') for tag_a in soup.find_all('a')]

    #recipe links end with  '-' + <24 hex-digits>
    #filter links which are long enough to contain '-' at place 24 from the end
    recipe_links = [link for link in links if type(link) is str and len(link) > 30 and link[len(link)-25] == '-']

    return recipe_links

#Extract Title, description, ingredients, amount, and steps.
def getTitle_Ingredients_Steps(recipeSoup) :

    title = recipeSoup.find('h1').text

    if("verkar" in title) :
        return 1,1,1,1

    description = recipeSoup.find('h4').text
   
    tags_p = recipeSoup.find_all('p')

    try :
        tags_p.remove(tags_p[0])
        tags_p.remove(tags_p[0])
    except :
        print(recipeLink)

    ingredients = []
    steps = []

    for tag_p in tags_p :

        
        # Ingredients and amounts
    #step    
    #ingredient   dsbz dsct dsft dsbn dsbp dsbq dsfu
    #ignredient   dsbz dsct dsft dsbn dsbp dsbq dsfu
        if "dsbz dsct dsfs dsbn dsbp dsbq dsft" == tag_p.get('class') :
            ingredients.append(tag_p.text)

        # Steps
        else :
            steps.append(tag_p.text)
    
    return title, description, ingredients, steps


# Extract duration and nutritional value.
def get_Nutrients_Duration(recipeSoup) :

    isNutrient = False
    isDuration = False

    nutrients = []
    duration = ""

    for tag_span in recipeSoup.find_all('span') :

        if tag_span.text == "Näringsvärden" :
            isNutrient = True
            continue

        if tag_span.text == "Köksredskap" :
            isNutrient = False
            continue

        if tag_span.text == "Tillagningstid" :
            isDuration = True
            continue

        if isDuration : 
            duration = tag_span.text
            isDuration = False

        if isNutrient :
            nutrients.append(tag_span.text)

    return nutrients, duration


#Get all recipe category pages on page
def get_Category_Links(categorySoup) :

    links =  [tag_a.get('href') for tag_a in soup.find_all('a')]

    category_links = [ URL + string.replace("/recipes","") + "?page=20" for string in links if type(string) is str and "recept" in string]

    return category_links

# write recipe to file
def write_Recipe_To_File(recipe, outputPath) :
 
    if(title == 1) : return

    filename = outputPath + recipe.title + ".txt"

    file = open(filename, 'w', encoding="utf-8")

    file.write(recipe.__str__())

    file.close()


source = "https://www.hellofresh.se/recipes/appelburgare-5f2a7eb6ae5bb563d564abaf"

soup = URL_To_Soup(source)

title, description, ingredients, steps = getTitle_Ingredients_Steps(soup)

nutrients, duration = get_Nutrients_Duration(soup)

recipe = Recipe.Recipe(title, description, ingredients, steps, nutrients, duration, source)


print(recipe)




