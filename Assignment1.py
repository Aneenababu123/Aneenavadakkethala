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

'''
A user defined function is created to depicts the bar plot ,also inserted the required data set to plot the chart.
Which is used for the furthur analysis of  provided data. 
'''

def barchart(bardata):
    data_2 = bardata # New variable is created to store the dataset.
    print(data_2) # prints the specified dataset for plotting bar chart

# Set labels for x and y axis
    plt.figure()
    plt.bar(data_2["COUNTRY"], data_2["FEMALE"], label="FEMALE")
    plt.bar(data_2["COUNTRY"], data_2["MALE"], label="MALE")
    plt.title("CAUSE OF DEATH BY INJURY IN THE YEAR 2019") # Shows the title of chart
    plt.xlabel("Country") # for x axis
    plt.ylabel("Death Rate") # for y axis
    plt.savefig("barplot.png") # Saving the figure with png file extension
    plt.legend()
    plt.show()
    return # A return statement is used to end the execution of the function call 

'''
A  user defined function is created to depict the piechart ,also inserted the required data set to plot the chart.
Which is used for the furthur analysis of  provided data. 
'''


def piechart(piedata):
    data_3 = piedata # New variable is created to store the dataset.

    print(data_3) # prints the specified dataset for plotting pie chart
    plt.pie(data_3["2017"], labels=data_3["COUNTRY"], autopct="%1.1f%%")
    # plot title
    plt.title('MOBILE SUBSCRIPTION RATE PER 100 PERSON IN THE YEAR OF 2017')
    plt.savefig("Pieplot.png")
 
    # function to show the plot
    plt.show()
    return # A return statement is used to end the execution of the function call 


if __name__ == "__main__":
    #To read the data in excel format for linechart
    data_1 = pd.read_excel("data_1.xlsx")  
    #To read the data in excel format for barchart
    data_2 = pd.read_excel("death.xlsx")
    #To read the data in excel format for piechart
    data_3 = pd.read_excel("Mobile_sub.xlsx")
    #Here is the function for calling lineplot
    linechart(data_1)
   #Here is the function for calling barchart
    barchart(data_2)
    #Here is the function for calling piechart
    piechart(data_3)