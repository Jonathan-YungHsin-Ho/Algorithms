#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    if not set(recipe.keys()).issubset(set(ingredients.keys())):
        return 0
    else:
        batches = 0
        max_batches = math.inf
        for key in recipe:
            batches = ingredients[key] // recipe[key]
            max_batches = batches if batches < max_batches else max_batches
        return max_batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
