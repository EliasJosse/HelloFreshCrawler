#!/usr/bin/env python
# coding: utf-8


import requests
from bs4 import BeautifulSoup


#Gather all recipe links on page
def get_Recipe_Links(soup) :
    links = [tag_a.get('href') for tag_a in soup.find_all('a')]

    #recipe links end with  '-' + <24 hex-digits>
    #filter links which are long enough to contain '-' at place 24 from the end
    recipe_links = [link for link in links if type(link) is str and len(link) > 30 and link[len(link)-25] == '-']

    return recipe_links

#Extract Title, description, ingredients, amount, and steps.
def getTitle_Ingredients_Steps(recipe_link) :

    recipe_page_soup = link_To_Soup(recipe_link)

    title = recipe_page_soup.find('h1').text

    tags_p = recipe_page_soup.find_all('p')

    description = tags_p[1]

    tags_p.remove(tags_p[0])
    tags_p.remove(tags_p[0])

    ingredients = []
    steps = []

    for tag_p in tags_p :

        
        # Ingredients
        try :
            if type(tag_p['class']) :
                ingredients.append(tag_p.text)
            
        # Steps
        except :
            steps.append(tag_p.text)
    
    return title, description, ingredients, steps


# Extract duration and nutritional value.
def get_Nutrients_Duration(recipe_link) :

    recipe_page_soup = link_To_Soup(recipe_link)

    isNutrient = False
    isDuration = False

    nutrients = []
    duration = ""

    for tag_span in recipe_page_soup.find_all('span') :

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


def link_To_Soup(URL) :

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    return soup



#Get all recipe category pages on page
def get_Category_Links(URL) :

    soup = linkToSoup(URL)

    links =  [tag_a.get('href') for tag_a in soup.find_all('a')]

    category_links = [ URL + string.replace("/recipes","") + "?page=20" for string in links if type(string) is str and "recept" in string]

    return category_links



# write recipe to file
path = "D:/programmering/"
recipeName = "NameOfRecipe"
filename = path + recipeName + ".txt"
file = open(filename, 'w')
file.write( recipeName +"\n"
           "Salt   1g    \n"
           "Peppar 2g    \n"
           "Energi 2000 Kcal \n")
file.close()





    
