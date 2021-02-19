# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 19:54:53 2021

@author: timpr
"""
import pandas as pd

def import_beer_data():
    """
    Imports the beer style statistics determined from the previous analysis

    Returns
    -------
    style_avgs (Dict<String,float>):   Dictionary with style group names as keys, 
                                       average rating as value
    style_stdevs (Dict<String,float>): Dictionary with style group names as keys, 
                                       average rating as value
    all_beers Tuple<float>:            Tuple with all beer average rating and standard deviation (length 2)                            
    """
    
    beer_data = pd.read_csv("beerResults.csv")
    
    # Read in columns from the beer data file
    beer_styles = beer_data["Beer Style"].tolist()
    avg_ratings = beer_data["Average Rating"].tolist()
    stdevs = beer_data["Standard Deviation"].tolist()
    
    style_avgs = {}
    style_stdevs = {}
    
    for i in range(len(beer_styles)):
        if beer_styles[i] == "All Beers":
            all_beers = (avg_ratings[i], stdevs[i])
        else:
            style_avgs[beer_styles[i]] = round(avg_ratings[i],3)
            style_stdevs[beer_styles[i]] = round(stdevs[i],3)
        
    
    return(style_avgs, style_stdevs, all_beers)    