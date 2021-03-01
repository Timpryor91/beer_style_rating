# -*- coding: utf-8 -*-
"""

@author: timpr
"""
from classes.beer_class import Beer
import requests as req
from bs4 import BeautifulSoup as bs

def scrape_beer_data():
    """
    Scrapes beer rating data from Untappd

    Returns
    -------
    beer_list (List<Beer>): A list of beer objects

    """

    beer_object_list = []
    beer_name_list = []
    
    # Loop over number range, chosen based on typical numbers seen for beer IDs on Untapped
    # HTML format is https://untappd.com/b/beer-name/beer-id-number
    for number in range(5000000):
        r = req.get('https://untappd.com/b/---/%s' % number)
        if r.status_code == 400:
            # If request has worked correctly, use Beatiful soup to extract page content
            content = bs(r.content, 'lxml')
            page_contents = content.find('div', {'class':'content'})  
            
            # Ignore empty pages
            if page_contents is not None:
                # Obtain sub HTML blocks
                beer_name_content = page_contents.find('div', {'class': 'name'})
                beer_details_content = page_contents.find('div', {'class': 'details'})
                
                # Extract text entries to populate Beer object parameters
                beer_name = beer_name_content.h1.string
                brewery_name = beer_name_content.find('p', {'class' : 'brewery'}).a.string
                style = beer_name_content.find('p', {'class': 'style'}).string
                rating = beer_details_content.find('p', {'class' : 'rating'}).find('span', {'class' : 'num'}).string
                num_reviews = beer_details_content.find('p', {'class':'raters'}).string
            
                # Add new beers to beer list (as some numbers will route to the same page)
                if beer_name not in beer_name_list:
                    beer_name_list.append(beer_name)
                    beer_object_list.append(Beer(beer_name,
                                          brewery_name,
                                          rating,
                                          num_reviews,
                                          style)
                                          )
    return(beer_object_list)