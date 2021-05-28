# -*- coding: utf-8 -*-
"""

@author: timpr
"""
# from tool_interface import initiate_interface
from tool_interface import Interface

from modules.beer_data import import_beer_data
import tkinter as tk

# Run the application
if __name__ == "__main__":
    
    # Import beer style names and statistics
    style_avgs, style_stdevs, all_beers = import_beer_data()
    
    # # Launch interface        
    # initiate_interface(style_avgs, style_stdevs, all_beers)
    
    #Initiate tool interface
    window = tk.Tk()
    tool_interface = Interface(window, style_avgs, style_stdevs, all_beers)
    window.mainloop()