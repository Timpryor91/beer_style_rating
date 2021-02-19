# -*- coding: utf-8 -*-
"""

@author: timpr
"""
import statistics
import operator

def calculate_stats(style_group_dict):
    """
    Calculates statistics for different beer style groups
    
    Args:
        style_dict (Dict<String:List<float>): A dictonary with beer styles as the key
                                              and list of beer ratings for the style as the value 
    
    Returns:
        sorted_avgs (Dict<String:float>): A dictonary with style groups as key, average rating as value
        style_stdevs (Dict<String:float>): A dictonary with style groups as key, standard deviation as value
        style_num_revs (Dict<String:int>): A dictonary with style groups as key, number of reviews as value

    """   
    style_avgs = {}
    style_stdevs = {}
    style_num_revs = {}
    
    # Populate the avg, stdev and num review dictionaries for each style
    # Need at least one value to calculate average, 2 to calculate standard deviation
    for style in style_group_dict:
        rating_num = len(style_group_dict[style])
        if rating_num < 1:
            rating_avg = 0
        else:
            rating_avg = round(statistics.mean(style_group_dict[style]),3)
            
        if rating_num < 2:
            rating_stdev = 0            
        else:
            rating_stdev = round(statistics.pstdev(style_group_dict[style]),3)
        style_avgs[style] = rating_avg, 
        style_stdevs[style] = rating_stdev 
        style_num_revs[style] = rating_num
        
    # Sort the style averages dictionary keys into order from lowest to highest average rating
    sorted_avg_tuples = sorted(style_avgs.items(), key=operator.itemgetter(1))
    sorted_avgs = {k: v for k, v in sorted_avg_tuples}
    for key in sorted_avgs:
        sorted_avgs[key] = sorted_avgs[key][0]
    
    
    return (sorted_avgs, style_stdevs, style_num_revs)