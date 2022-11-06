#!/usr/bin/env python
# coding: utf-8


import requests
from bs4 import BeautifulSoup


#Gather all recipe links on page
def getRecipeLinks(soup) :
    links = [tag_a.get('href') for tag_a in soup.find_all('a')]

    #recipe links end with  '-' + <24 hex-digits>
    #filter links which are long enough to contain '-' at place 24 from the end
    recipe_links = [link for link in links if type(link) is str and len(link) > 30 and link[len(link)-25] == '-']

    return recipe_links

#Extract Title, description, ingredients, amount, and steps.
def getTitle_Ingredients_Steps(recipe_link) :
    recipe_page = requests.get(recipe_link)

    recipe_page_soup = BeautifulSoup(recipe_page.content, "html.parser")

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




URL = "https://www.hellofresh.se/recipes/amerikanska-recept?page=20"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")


recipe_links = getRecipeLinks(soup)

recipe_page = requests.get(recipe_links[1])

recipe_page_soup = BeautifulSoup(recipe_page.content, "html.parser")

isNutrient = False
for tag_span in recipe_page_soup.find_all('span') :

    if tag_span.text == "Näringsvärden" :
        isNutrient = True

    if tag_span.text == "Köksredskap" :
        isNutrient = False

    if isNutrient :
        print(tag_span)




# Extract duration and nutritional value.





#file = open(title, 'w')
#file.write(title)





    
