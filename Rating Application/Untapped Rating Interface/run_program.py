# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 19:52:01 2021

@author: timpr
"""
from tool_interface import initiate_interface
from modules.beer_data import import_beer_data

# Run the application
if __name__ == "__main__":
    
    # Import beer style names and statistics
    style_avgs, style_stdevs, all_beers = import_beer_data()
    
    # Launch interface        
    initiate_interface(style_avgs, style_stdevs, all_beers)