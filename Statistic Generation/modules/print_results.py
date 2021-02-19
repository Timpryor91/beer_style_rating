# -*- coding: utf-8 -*-
"""

@author: timpr
"""


def print_results(style_avgs, style_stdevs, style_num_revs):
    """
    Prints calculated statistics to a .csv file
    
    Args:
        sorted_avgs (Dict<String:float>): A dictonary with style groups as key, average rating as value
        style_stdevs (Dict<String:float>): A dictonary with style groups as key, standard deviation as value
        style_num_revs (Dict<String:int>): A dictonary with style groups as key, number of reviews as value
    
    Returns:
        None

    """     
    # Create a file to write result
    beer_results_file = open("beerResults.csv", 'w')
    
    # Heading rows
    beer_results_file.write("Beer Style, Average Rating, Standard Deviation, Number of Reviews \n")
    
    # Write in results row for each beer
    for key in style_avgs:
        beer_results_file.write(
                                str(key) + "," +
                                str(style_avgs[key]) + "," +
                                str(style_stdevs[key]) + "," +
                                str(style_num_revs[key]) + "\n")
    
    beer_results_file.close()
    
    return