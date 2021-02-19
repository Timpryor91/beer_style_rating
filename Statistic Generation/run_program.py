# -*- coding: utf-8 -*-
"""
@author: timpr
"""
from modules.create_style_dicts import create_style_dict
from modules.populate_dict import populate_style_dict
from modules.calculate_stats import calculate_stats
from modules.import_beer import import_beer_data
from modules.style_groups import group_styles
from modules.print_results import print_results

# Run the application
if __name__ == "__main__":
    
    # Define dictionary for beer style
    style_dict = create_style_dict()
    
    # Import beer data from .csv file
    beer_list = import_beer_data()
    
    # Populate style dictionary with beer ratings
    style_dict = populate_style_dict(beer_list, style_dict)    
    
    # Group styles into style groups
    style_group_dict = group_styles(style_dict)    
   
    # Calculate statistics for each beer type
    style_avgs, style_stdevs, style_num_revs = calculate_stats(style_group_dict)
    
    # Print results to a .csv
    print_results(style_avgs, style_stdevs, style_num_revs)
    

    
    