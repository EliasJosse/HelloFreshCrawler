#!/usr/bin/env python
# coding: utf-8


class Recipe:

    def __init__(self, title, description, ingredients, steps, nutrients, duration, source) :

        self.title = title
        self.description = description
        self.ingredients = ingredients
        self.steps = steps
        self.nutrients = nutrients
        self.duration = duration
        self.source = source


    def __str__(self) :

        output = self.title + "\n"
        output += self.description + " \n\n"
        output += "Ingredienser" + " \n\n"

        ingredientStartColumn = 9

        for i in range(len(self.ingredients)) :
            if(i % 2 == 0) :
                ingredientStartColumn -= len(self.ingredients[i])
                output += self.ingredients[i]

            else :
                spaces = ""

                for j in range(ingredientStartColumn) :
                    spaces += " ";    

                output += spaces + self.ingredients[i] + " \n"
                ingredientStartColumn = 9

        output += "\n\n\n"

        for i in range(len(self.steps)) :
            output += str(i+1) + ". \n" + self.steps[i] + "\n\n"
      
        output +=  " \n\n"


        output += "Tillagningstid " + self.duration +  " \n"
        output += "Näringsvärde " + self.nutrients[1]


        output +=  " \n\n"

  

        output += self.source

        return output
    