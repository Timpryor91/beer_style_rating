# -*- coding: utf-8 -*-
"""

@author: timpr
"""

def populate_style_dict(beer_list, style_dict):
    """
    Assigns the rating of each beer to the relevant list in the style dictionary
    
    Args:
        beer_list (List<Beer>): A list of beer objects
        style_dict (Dict<String:List<float>): A dictonary with beer styles as the key
                                                and empty list as the value
    
    Returns:
        style_dict (Dict<String:List<float>): A dictonary with beer styles as the key
                                              and list of beer ratings for the style as the value

    """    
    for beer in beer_list:
        style_dict[beer.get_style()].append(beer.get_rating())
    
    return(style_dict)