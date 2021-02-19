# -*- coding: utf-8 -*-
"""
@author: timpr
"""

class Beer():
    """
    A particular beer on Untappd
    """  
    def __init__(self, beer_name, brewery_name, rating, num_reviews, style):
        """
        Initialize a beer object

        Args:
            beer_name (string): the name of the beer
            brewery_name (string): the name of the brewery that produced the beer
            rating (float): the average rating of the beer
            num_reviews (integer): the number of ratings the beer has
            style (string): the style of the beer (e.g. Stout - Milk)
        """
        self.beer_name = str(beer_name) 
        self.brewery_name = str(brewery_name)
        self.rating = float(rating)
        self.num_reviews = int(num_reviews)
        self.style = str(style)
        
    def get_beer_name(self):      
        return (self.beer_name)
    
    def get_brewery_name(self):     
        return (self.brewery_name)
    
    def get_rating(self):     
        return (self.rating)
    
    def get_num_reviews(self):     
        return (self.num_reviews)
    
    def get_style(self):     
        return (self.style)
