# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 13:54:21 2023

@author: DELL
"""

import pandas as pd
import matplotlib.pyplot as plt

'''
A user defined function is created to depicts the line plot.And also inserted the required data set to plot the line plot. 
which is used for the furthur analysis of  provided data. 
'''
def linechart(linedata):
    data_1 = linedata # New variable is created to store the dataset.
    print(data_1) # prints teh specified  dataset for plotting line chart
#Line plots
   
# Plot the four countries with labels 
    plt.plot(data_1["Year"], data_1["India"], label="India" ,color = 'blue')
    plt.plot(data_1["Year"], data_1["Israel"], label="Israel" ,color= 'orange')
    plt.plot(data_1["Year"], data_1["Jamaica"], label="Jamaica",color= 'green')
    plt.plot(data_1["Year"], data_1["Italy"], label="Italy",color= 'red')

# Set lables and show the legend
    plt.xlim(2007,2020)
    plt.title("FERTILITY RATE TOTAL (BIRTHS PER WOMEN)")
    plt.xlabel("YEAR")
    plt.ylabel("FERTILITY RATE")
    plt.legend()
    plt.savefig("Lineplot.png")
    plt.show()
    return # A return statement is used to end the execution of the function call 


if __name__ == "__main__":
    #To read the data in excel format for linechart
    data_1 = pd.read_excel("data_1.xlsx")   
    #Here is the function for calling lineplot
    linechart(data_1)
   