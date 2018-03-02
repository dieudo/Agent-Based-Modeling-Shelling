# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 14:00:31 2016

@author: dieudonneouedraogo
"""
from random import uniform  
from math import sqrt
import matplotlib.pyplot as plt
import random as rd
import numpy as numpy

# I can import seed and set seed if you guys want to have the same results as me 

#annual rate of growth for popoulation sepaking languages 
a=1.7# English adaptation rate
b=1.1# Spanish adaptation rate 
c=1.1# Chinese adaptation rate 
d=1.05# arabic adapatation rate 
Moore=8# We chose moore neighborhood 
Tolerance=0.1
class Citizen:
    " I defined a class which is all the attributes related to all citizens"

    def __init__(self, language):
        "I defined a function that return the language and print the position"
        self.language = language
        self.get_position()

    def get_position(self):
        "You can change this if you want .I supposed that the country is a 10 by 10 rectangle"
        self.position= uniform(0,1), uniform(0,1)# You can do different assumptions if you want 

    def distance(self, next):
        "Computes euclidean distance between self and next citizen ."
        " You guys may suggest differents distances measures"
        x = (self.position[0] - next.position[0])**2
        y = (self.position[1] - next.position[1])**2
        return sqrt(x + y)

    def Pleased(self, citizens):
        "I defined a function that will measure the level of happiness of the citizens"
        "True if sufficient number of nearest neighbors speak the same language ."
        distances = []
        # distances is a list of pairs (d, citizen), where d is distance from
        # citizen to self
        for citizen in citizens:
            if self != citizen:
                dist = self.distance(citizen)
                distances.append((dist, citizen))
        # == Sort from smallest to largest, according to distance == #
        distances.sort()
        #  assigned the neighbors that fall in that distance 
        neighbors = [citizen for d, citizen in distances[:Moore]]
        # == Count how many speak the same language  as self == #
        same_language = sum(self.language == citizen.language for citizen in neighbors)
        return same_language >= Tolerance*Moore

    def update(self, citizens):
        "If not happy, then randomly choose new locations until pleased"
        while not self.Pleased(citizens):
            self.get_position()
            
def graphs(agents, cycle_num):
    "Plot the  physical positions  of Citizens after cycle_num rounds of the loop."
    xval0, yval0 = [], []
    xval1, yval1 = [], []
    xval2, yval2 = [], [] #lists aggregating x,y coordinates for Chinese
    xval3, yval3 = [], [] #lists aggregating x,y coordinates for Arabics
    average_X1, average_Y1 = [], [] #lists aggregating averages for English
    average_X2, average_Y2 = [], [] #lists aggregating averages for Spanish
    average_X3, average_Y3 = [], [] #lists aggregating averages for Chinese
    average_X4, average_Y4 = [], [] #lists aggregating averages for Arab
    
    
    # get the posittion  of each speaking citizen
    for citizen in citizens:
        x, y = citizen.position
        if citizen.language == 0:
            xval0.append(x)
            yval0.append(y)
            average_X1.append(sum(xval0)/len(xval0)) #accumulate average X coordinate
            average_Y1.append(sum(yval0)/len(yval0)) #accumulate average Y coordinate
        elif citizen.language==1:
            xval1.append(x)
            yval1.append(y)
            average_X2.append(sum(xval1)/len(xval1)) #accumulate average X coordinate
            average_Y2.append(sum(yval1)/len(yval1)) #accumulate average Y coordinate
        elif citizen.language==2: #if the citizen speaks Chinese
            xval2.append(x) #Gather x value and append
            yval2.append(y) #Gather Y value and append
            average_X3.append(sum(xval2)/len(xval2)) #accumulate average X coordinate
            average_Y3.append(sum(yval2)/len(yval2)) #accumulate average Y coordinate
                
        else: #if the citizen speaks Arabic
            xval3.append(x) #Gather x value and append
            yval3.append(y) #Gather Y value and append
            average_X4.append(sum(xval3)/len(xval3)) #accumulate average X coordinate
            average_Y4.append(sum(yval3)/len(yval3)) #accumulate average Y coordinate
    
    fig, ax = plt.subplots(figsize=(10, 10))
    
    ax.plot(xval0, yval0, 's', markerfacecolor='b')
    ax.plot(xval1, yval1, 's', markerfacecolor='r')
    ax.plot(xval2, yval2,'s',markerfacecolor='green')
    ax.plot(xval3, yval3,'s',markerfacecolor='yellow')
        #average distance in moore's neighbourhood as a metric for amount of clustering
    print'the average distance for speaking ennglish is:', sqrt(numpy.average(average_X1)**2 + numpy.average(average_Y1)**2) #mean position computation for English
    print 'the average distance for speaking spanish is:',sqrt(numpy.average(average_X2)**2 + numpy.average(average_Y2)**2) #mean position computation for Spanish
    print 'the average distance for  speaking chineese is:',sqrt(numpy.average(average_X3)**2 + numpy.average(average_Y3)**2) #mean position computation for Chinese            
    print 'the average distance for speaking arabic is:',sqrt(numpy.average(average_X4)**2 + numpy.average(average_Y4)**2) #mean position computation for Arabic
    
    #To number the plots I use this below ,but you can remove it (not necessary)
    ax.set_title('Cycle {}'.format(cycle_num-1 ))
    plt.show()

#The values we collect from the year before our study 

english = rd.randint(300, 400)
print 'English Speaking Population= ', english 
spanish = rd.randint(200, 280)
print 'Spanish Speaking Population = ', spanish
chinese = rd.randint(70, 100)
print 'Chinese Speaking Population = ', chinese
arabic = rd.randint(50, 70)
print 'Arabic Speaking Popululation = ', arabic

#Taking into considerations the rate of adaptations associated with each language 
#Our projections for the following years after we collected the data !

#I run this loop below to find the values for year 1 to year 5
for i in xrange(1, 5):
    
    print'for the year',i,'your metrics and plots are'
    english=int(a*english) 
    spanish=int(b*spanish)
    chinese=int(c*chinese)
    arabic=int(d*arabic)
    print 'the total population in year',i,'is',english+spanish+chinese+arabic

# == Create a list of agents == #
    citizens = [Citizen(0) for i in range(english)]
    citizens.extend(Citizen(1) for i in range(spanish))
    citizens.extend(Citizen(2) for i in range(chinese))
    citizens.extend(Citizen(3) for i in range(arabic))
#---------------------------------------------------------------#
    n= 1
# ==  run around until no one  want to moave again :no more motion
    while 1:
        print'cycle', n
        graphs(citizens, n)
        n += 1
        no_motion = True
        for citizen in citizens:
            last_position = citizen.position
            citizen.update(citizens)
            if citizen.position != last_position:
                no_motion = False
        if no_motion:
            break
        
    print'Cycles done!'
# ONCE THIS PROGRAM IS DONE AND NO ONE IS MOVING WE CAN USE networkx  to plot the position of citizen in the country 


            
