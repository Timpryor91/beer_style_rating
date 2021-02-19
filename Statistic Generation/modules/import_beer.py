# -*- coding: utf-8 -*-
"""

@author: timpr
"""
from classes.beer_class import Beer

def import_beer_data():
    """
    Imports beer data from .csv file and creates a list of beer objects
    
    Args:
        None
    
    Returns:
        beer_list (List<Beer>): A list of beer objects
    """    

    # Pandas didn't like some of the non-english characters for some reason
    # so using a more crude file read method    
    
    beer_list=[]
    
    beer_data = open("beerData.csv", 'r')
    beer_data.readline()

    for line in beer_data:
        line = line.rstrip()
        line_list = line.split(",")
        beer_name = line_list[4]
        brewery_name = line_list[5]
        rating = line_list[11]
        num_reviews = line_list[12]
        style = line_list[2]
        
        # Don't include beers that don't have a rating
        if (rating == "NA"):
            continue
        
        beer_list.append(Beer(beer_name,
                              brewery_name,
                              rating,
                              num_reviews,
                              style)
                              )
    beer_data.close()
    
    return(beer_list)