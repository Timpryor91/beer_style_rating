# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 10:41:36 2021

@author: timpr
"""

from classes.beer_class import Beer
import random

def random_beer_list(style_dict):
    """
    Creates a random list of beers for the purposes of testing prior to implementing the web
    scraping
    """  
    beer_list = []

    for i in range(1000):
        beer_name = "Beer" + str(i)
        brewery_name = "Brewery" + str(i)
        rating = 5*random.random()
        num_reviews = 20000*random.random()
        style = random.choice(list(style_dict))
        beer_list.append(Beer(beer_name, brewery_name, rating, num_reviews, style))
    
    return(beer_list)