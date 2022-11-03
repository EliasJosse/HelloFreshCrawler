#!/usr/bin/env python
# coding: utf-8


import requests
from bs4 import BeautifulSoup



def getRecipeLinks(soup) :
    #Gather all links on page
    links = [tag_a.get('href') for tag_a in soup.find_all('a')]

    #recipe links end with  '-' + <24 hex-digits>
    #filter links which are long enough to contain '-' at place 24 from the end
    recipe_links = [link for link in links if type(link) is str and len(link) > 30 and link[len(link)-25] == '-']

    return recipe_links



URL = "https://www.hellofresh.se/recipes/amerikanska-recept?page=20"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")


recipe_links = getRecipeLinks(soup)

recipe_page = requests.get(recipe_links[1])
print(recipe_links[1])
recipe_page_soup = BeautifulSoup(recipe_page.content, "html.parser")
print(recipe_page_soup.find('h1').text)
print(recipe_page_soup.find('h4').text)



for tag_a in recipe_page_soup.find_all('p') :
    print(tag_a)




#for recepi_link in recipe_links :






    
