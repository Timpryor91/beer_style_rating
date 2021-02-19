# -*- coding: utf-8 -*-
"""

@author: timpr
"""

def group_styles(style_dict):

    """
    Groups the ratings for beer styles into style groups
    
    Args:
        beer_list (List<Beer>): A list of beer objects
        style_dict (Dict<String:List<float>): A dictonary with beer styles as the key
                                              and list of beer ratings for the style as the value
    
    Returns:
        style_group_dict (Dict<String:List<float>): A dictonary with style groups as the key
                                              and list of beer ratings for the style as the value

    """   
    style_groups = {"Miscellaneous": [
                                    "Hard Seltzer",
                                    "Grape Ale - Italian",
                                    "Grape Ale - Other",
                                    "Gluten-Free",
                                    "Happoshu",
                                    "Non-Alcoholic Beer",
                                    "Black & Tan",
                                    "Chilli / Chile Beer",
                                    "Freeze-Distilled Beer",
                                    "Table Beer",
                                    "Ginger Beer",
                                    "Gruit / Ancient Herbed Ale",
                                    "Historical Beer - Other",
                                    "Honey Beer",
                                    "Kombucha",
                                    "Malt Beer",
                                    "Malt Liquor",
                                    "Pumpkin / Yam Beer",
                                    "Root Beer",
                                    "Shandy / Radler",
                                    "Smoked Beer",
                                    "Specialty Grain",
                                    "Spiced / Herbed Beer",
                                    "Traditional Ale",
                                    "Winter Warmer"
                                    ],
                    "Sour": [
                                    "Sour - Berliner Weisse",
                                    "Sour - Flanders Oud Bruin",
                                    "Sour - Flanders Red Ale",
                                    "Sour - Fruited",
                                    "Sour - Fruited Berliner Weisse",
                                    "Sour - Fruited Gose",
                                    "Sour - Gose",
                                    "Sour - Other",
                                    "American Wild Ale"
                                    ],
                    "Single Stout": [
                                    "Stout - American",
                                    "Stout - Coffee",
                                    "Stout - English",
                                    "Stout - Foreign Export",
                                    "Stout - Irish Dry",
                                    "Stout - Milk / Sweet",
                                    "Stout - Oatmeal",
                                    "Stout - Other",
                                    "Stout - Oyster",
                                    "Stout - Pastry",
                                    "Stout - White"
                                    ],
                    "UK": [
                                    "English Bitter",
                                    "English Mild Ale",
                                    "Extra Special / Strong Bitter",
                                    "Scottish Ale",
                                    "Scottish Export Ale"
                                    ],
                    "Barleywine": [
                                    "Barleywine - American",
                                    "Barleywine - English",
                                    "Barleywine - Other"
                                    ],
                    "Brown Ale": [
                                    "Brown Ale - American",
                                    "Brown Ale - Belgian",
                                    "Brown Ale - English",
                                    "Brown Ale - Imperial / Double",
                                    "Brown Ale - Other"
                                    ],
                    "Pale Ale": [
                                    "Pale Ale - American",
                                    "Pale Ale - Australian",
                                    "Pale Ale - Belgian",
                                    "Pale Ale - English",
                                    "Pale Ale - International",
                                    "Pale Ale - Milkshake",
                                    "Pale Ale - New England",
                                    "Pale Ale - New Zealand",
                                    "Australian Sparkling Ale",
                                    "Cream Ale",
                                    "Golden Ale",
                                    "Kentucky Common"
                                    ],
                    "Double Porter": [
                                    "Porter - Imperial / Double",
                                    "Porter - Imperial / Double Baltic",
                                    "Porter - Imperial / Double Coffee"
                                    ],
                    "Double IPA": [
                                    "IPA - Imperial / Double",
                                    "IPA - Imperial / Double Milkshake",
                                    "IPA - Imperial / Double New England",
                                    "IPA - Triple",
                                    "IPA - Triple New England",
                                    "IPA - Quadruple"
                                    ],
                    "Belgian": [
                                    "Belgian Blonde",
                                    "Belgian Dubbel",
                                    "Belgian Quadrupel",
                                    "Belgian Strong Dark Ale",
                                    "Belgian Strong Golden Ale",
                                    "Belgian Tripel"
                                    ],
                    "Bock": [
                                    "Bock - Doppelbock",
                                    "Bock - Eisbock (Traditional)",
                                    "Bock - Hell / Maibock / Lentebock",
                                    "Bock - Single / Traditional",
                                    "Bock - Weizenbock",
                                    "Bock - Weizendoppelbock"
                                    ],
                    "Pilsner": [
                                    "Pilsner - Czech",
                                    "Pilsner - German",
                                    "Pilsner - Imperial / Double",
                                    "Pilsner - Other"
                                    ],
                    "Lambic": [
                                    "Lambic - Faro",
                                    "Lambic - Framboise",
                                    "Lambic - Fruit",
                                    "Lambic - Gueuze",
                                    "Lambic - Kriek",
                                    "Lambic - Traditional",
                                    "Fruit Beer"
                                    ],
                    "German": [
                                    "Dunkelweizen",
                                    "Hefeweizen",
                                    "Hefeweizen Light / Leicht",
                                    "Altbier",
                                    "Dampfbier",
                                    "Festbier",
                                    "Kellerbier / Zwickelbier",
                                    "Kristallweizen",
                                    "Kölsch",
                                    "Märzen",
                                    "Rauchbier",
                                    "Schwarzbier",
                                    "Steinbier",
                                    "Zoigl"
                                    ],
                    "Alernative IPA": [
                                    "IPA - Imperial / Double Black",
                                    "IPA - Brett",
                                    "IPA - Brut",
                                    "IPA - Black / Cascadian Dark Ale",
                                    "IPA - Red",
                                    "IPA - Rye",
                                    "IPA - Sour",
                                    "IPA - Farmhouse"
                                    ],
                    "Single IPA": [
                                    "IPA - American",
                                    "IPA - Belgian",
                                    "IPA - English",
                                    "IPA - International",
                                    "IPA - Milkshake",
                                    "IPA - New England",
                                    "IPA - Session / India Session Ale",
                                    "IPA - White",
                                    "Dark Ale",
                                    "Winter Ale"
                                    ],
                    "Farmhouse Ale": [
                                    "Farmhouse Ale - Bière de Garde",
                                    "Farmhouse Ale - Bière de Mars",
                                    "Farmhouse Ale - Other",
                                    "Farmhouse Ale - Sahti",
                                    "Farmhouse Ale - Saison",
                                    "Bière de Champagne",
                                    "Wild Ale - Other",
                                    "Brett Beer",
                                    "Grisette"
                                    ],
                    "Single Porter": [
                                    "Porter - American",
                                    "Porter - Baltic",
                                    "Porter - Coffee",
                                    "Porter - English",
                                    "Porter - Other"
                                    ],
                    "Strong": [
                                    "Adambier",
                                    "Strong Ale - American",
                                    "Strong Ale - English",
                                    "Strong Ale - Other",
                                    "Scotch Ale / Wee Heavy",
                                    "Burton Ale",
                                    "Mumme",
                                    "Old Ale"
                                    ],
                    "Wheat Beer": [
                                    "Wheat Beer - American Pale Wheat",
                                    "Wheat Beer - Other",
                                    "Wheat Beer - Wheat Wine",
                                    "Wheat Beer - Witbier",
                                    "Lichtenhainer"
                                    ],
                    "Mead": [
                                    "Mead - Acerglyn / Maple Wine",
                                    "Mead - Braggot",
                                    "Mead - Cyser",
                                    "Mead - Melomel",
                                    "Mead - Metheglin",
                                    "Mead - Other",
                                    "Mead - Pyment",
                                    "Mead - Traditional"
                                    ],
                    "Red Ale": [
                                    "Red Ale - American Amber / Red",
                                    "Red Ale - Imperial / Double",
                                    "Red Ale - Irish",
                                    "Red Ale - Other",
                                    "Rye Beer",
                                    "Kvass",
                                    "Roggenbier",
                                    "Rye Wine"
                                    ],
                    "Double Stout": [
                                    "Stout - Imperial / Double",
                                    "Stout - Imperial / Double Coffee",
                                    "Stout - Imperial / Double Milk",
                                    "Stout - Imperial / Double Oatmeal",
                                    "Stout - Imperial / Double Pastry",
                                    "Stout - Imperial / Double White",
                                    "Stout - Russian Imperial"
                                    ],
                    "Lager": [
                                    "Lager - Amber",
                                    "Lager - American",
                                    "Lager - American Amber / Red",
                                    "Lager - American Light",
                                    "Lager - Dark",
                                    "Lager - Dortmunder / Export",
                                    "Lager - Euro Dark",
                                    "Lager - Euro Pale",
                                    "Lager - Helles",
                                    "Lager - IPL (India Pale Lager)",
                                    "Lager - Japanese Rice",
                                    "Lager - Munich Dunkel",
                                    "Lager - Pale",
                                    "Lager - Red",
                                    "Lager - Strong",
                                    "Lager - Vienna",
                                    "Lager - Winter",
                                    "Blonde Ale",
                                    "California Common",
                                    "Grätzer / Grodziskie",
                                    "Patersbier"
                                    ]
                    }
    
    # Dictionary to collate ratings for each style group
    style_group_dict = {}
    
    # Sort ratings in their relevant style group based on the style group dictionary
    for group in style_groups:
        for style in style_dict:
            if style in style_groups[group]:
                if group in style_group_dict:
                    style_group_dict[group].extend(style_dict[style]) 
                else:
                    style_group_dict[group] = style_dict[style]
        
    # Create an additional entry that contains all the beers
    styles = list(style_group_dict.keys())
    style_group_dict["All Beers"] = []
    for key in styles:
            style_group_dict["All Beers"].extend(style_group_dict[key])                
     
    return(style_group_dict)