# -*- coding: utf-8 -*-
"""

@author: timpr
"""

import tkinter as tk
import numpy as np
import scipy.stats as stats
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 

from modules.style_list import get_style_list

class Interface(object):
    """ 
    Initiates an instance of the login interface object
    
    Params:
    style_avgs (Dict<String,float>):   Dictionary with style group names as keys, 
                                       average rating as values
    style_stdevs (Dict<String,float>): Dictionary with style group names as keys, 
                                       average rating as values
    all_beers Tuple<float>:            Tuple with all beer average rating and standard deviation (length 2) 
    
    """
    
    def __init__(self, window, style_avgs, style_stdevs, all_beers):
        
        self.window = window
        self.style_avgs = style_avgs 
        self.style_stdevs = style_stdevs
        self.all_beers = all_beers
        
        # Set heading
        self.window.title("Untappd Style Rating Adjustment")
    
        # Create frames to position widgets
        self.frame_top = tk.Frame(bg= "gold")
        self.frame_middle = tk.Frame(bg = "white")
        self.frame_bottom = tk.Frame(bg = "gold")
        self.frame_top_left = tk.Frame(master = self.frame_top, bg= "gold")
        self.frame_top_middle = tk.Frame(master = self.frame_top, bg= "gold")
        self.frame_top_right = tk.Frame(master = self.frame_top, bg= "gold")
        self.frame_middle_upper = tk.Frame(master = self.frame_middle, bg= "gold")
        self.frame_middle_lower = tk.Frame(master = self.frame_middle, bg= "white")
        
        # Beer name entry
        self.beer_name_label = tk.Label(master = self.frame_top_left, text = "Beer Name", bg="gold", width = 30)
        self.beer_name_entry = tk.Entry(master = self.frame_top_left, width = 30)
        
        # Beer style dropdown list
        self.style_label = tk.Label(master = self.frame_top_middle, text = "Beer Style", bg="gold", width = 40)
        self.style_list = get_style_list()
        self.current_style = tk.StringVar(master = self.frame_top_middle)
        self.current_style.set(self.style_list[0])
        self.style_dropdown = tk.OptionMenu(self.frame_top_middle, self.current_style, *self.style_list)
        
        # Beer rating entry
        self.beer_rating_label = tk.Label(master = self.frame_top_right, text = "Beer Rating (0.0 - 5.0)", bg="gold", width = 20)
        self.beer_rating_entry = tk.Entry(master = self.frame_top_right, width = 20)
        
        # Button to trigger style score creation for user entered beer
        self.classify_button = tk.Button(master = self.frame_top,
                                         command = self.classify,
                                         height = 1,
                                         width = 8,
                                         text = "Classify",
                                        )
        
        # Create initial plot of distribution for all beers
        self.x_all_beer = np.linspace(self.all_beers[0]- 3*self.all_beers[1], self.all_beers[0] + 3*self.all_beers[1], 1000)
        self.all_beer_graph_figure = Figure(figsize=(6.5,3), dpi =100)
        self.beer_plot = self.all_beer_graph_figure.add_subplot(111)
        self.beer_plot.plot(self.x_all_beer, stats.norm.pdf(self.x_all_beer, self.all_beers[0], self.all_beers[1]))
        self.beer_plot.set_yticklabels([" ", " ", " ", " "])
        self.graph_canvas = FigureCanvasTkAgg(self.all_beer_graph_figure, master = self.frame_middle_upper)
        self.graph_canvas.draw()
        self.graph_canvas.get_tk_widget().pack()
        
        # Create custom legend below chart (in_built legend flexibility with FigureCanvasTkAgg is poor)
        self.all_beers_line_canvas = tk.Canvas(master = self.frame_middle_lower, height = 1.5, width = 10, bg = 'blue')
        self.all_beers_line_canvas.create_line(0,10,0,0)
        self.all_beers_legend_label = tk.Label(master = self.frame_middle_lower, text = "All Beers Distribution", bg="white", width = 19, height = 2)
        self.style_line_canvas = tk.Canvas(master = self.frame_middle_lower, height = 1.5, width = 10, bg = 'orange')
        self.style_line_canvas.create_line(0,10,0,0)
        self.style_legend_label = tk.Label(master = self.frame_middle_lower, text = " Style Distribution", bg="white", width = 15, height = 2)
        self.beer_line_canvas = tk.Canvas(master = self.frame_middle_lower, height = 1.5, width = 10, bg = 'green')
        self.beer_line_canvas.create_line(0,10,0,0)
        self.beer_legend_label = tk.Label(master = self.frame_middle_lower, text = "Beer Rating", bg="white", width = 11, height = 2)
        
        # Style rating score that automatically updates upon classification
        self.style_rating_score_label = tk.Label(master = self.frame_bottom, text = "Beer Style Rating", bg="gold", width = 20)
        self.style_rating_string = tk.StringVar(master = self.frame_bottom)
        self.style_rating_string.set("")
        self.style_rating_label = tk.Label(master = self.frame_bottom, textvariable = self.style_rating_string, bg="white", width = 20, height = 2)
        self.left_fill = tk.Label(master = self.frame_bottom, text = "", bg="gold", width = 25, height = 2)
        self.right_fill = tk.Label(master = self.frame_bottom, text = "", bg="gold", width = 25, height = 2)
        
        # Pack widgets and frames
        self.beer_name_label.pack()
        self.beer_name_entry.pack()
        self.style_label.pack()
        self.style_dropdown.pack()
        self.beer_rating_label.pack()
        self.beer_rating_entry.pack()
        self.classify_button.pack(side = tk.BOTTOM, anchor = "se")
        self.left_fill.pack(side = tk.LEFT)
        self.style_rating_score_label.pack(side = tk.LEFT)
        self.style_rating_label.pack(side = tk.LEFT)    
        self.right_fill.pack(side = tk.LEFT)
        self.all_beers_line_canvas.pack(side = tk.LEFT)  
        self.all_beers_legend_label.pack(side = tk.LEFT)  
        self.style_line_canvas.pack(side = tk.LEFT)  
        self.style_legend_label.pack(side = tk.LEFT)  
        self.beer_line_canvas.pack(side = tk.LEFT)  
        self.beer_legend_label.pack(side = tk.LEFT)    
        self.frame_top_left.pack(side = tk.LEFT)
        self.frame_top_middle.pack(side = tk.LEFT)
        self.frame_top_right.pack(side = tk.LEFT)
        self.frame_middle_upper.pack()
        self.frame_middle_lower.pack()   
        self.frame_top.pack()
        self.frame_middle.pack()
        self.frame_bottom.pack()
        
        # self.mainloop()

    def classify(self):
        """
        Creates a plot showing where a beer rating falls on its normal distribution
        """    
        # Calculate beer style rating and populate results cell
        self.beer_rating = float(self.beer_rating_entry.get())
        if (self.beer_rating < self.style_avgs[self.current_style.get()] - 1.5*self.style_stdevs[self.current_style.get()]):
            self.style_rating_string.set("Poor")
            self.style_rating_label.config(bg = "#da9694")
        elif (self.beer_rating < self.style_avgs[self.current_style.get()] - 0.5*self.style_stdevs[self.current_style.get()]):
            self.style_rating_string.set("Subpar")
            self.style_rating_label.config(bg = "#fabf8f")
        elif (self.beer_rating < self.style_avgs[self.current_style.get()] + 0.5*self.style_stdevs[self.current_style.get()]):
            self.style_rating_string.set("Good")
            self.style_rating_label.config(bg = "#95b3d7")
        elif (self.beer_rating < self.style_avgs[self.current_style.get()] + 1.5*self.style_stdevs[self.current_style.get()]):
            self.style_rating_string.set("Very Good")
            self.style_rating_label.config(bg = "#c4d79b")
        else:
            self.style_rating_string.set("Excellent")
            self.style_rating_label.config(bg = "#92d050")
        
        # Clear the plot if it already exists
        # (need to do this to prevent generation of multiple graph instances)    
        self.beer_plot.clear()
        
        # Replot the average beer distribution after clearing full plot
        self.beer_plot.plot(self.x_all_beer, stats.norm.pdf(self.x_all_beer, self.all_beers[0], self.all_beers[1]))
        self.beer_plot.set_yticklabels([" ", " ", " ", " "])
        
        # Create distribution plot for current selected style
        self.avg_current = self.style_avgs[self.current_style.get()]
        self.stdev_current = self.style_stdevs[self.current_style.get()]
        self.x_current_style = np.linspace(self.avg_current - 3*self.stdev_current, self.avg_current + 3*self.stdev_current, 100)
        self.beer_plot.plot(self.x_current_style, stats.norm.pdf(self.x_current_style, self.avg_current, self.stdev_current))
        
        # Plot vertical line corresponding to the selected beer's rating
        self.beer_plot.plot([self.beer_rating, self.beer_rating], [0,stats.norm.pdf(self.beer_rating, self.avg_current, self.stdev_current)])
        
        # Update plots    
        self.graph_canvas.draw()
                       
        return
