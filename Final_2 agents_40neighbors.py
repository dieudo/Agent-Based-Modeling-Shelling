# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 14:00:31 2016

@author: dieudonneouedraogo
"""
from random import uniform  
from math import sqrt
import matplotlib.pyplot as plt
import numpy as numpy
# I can import seed and set seed if you guys want to have the same results as me 

a=1.7
b=1.1
Moore=40
#c=1.1
class Citizen:
    " I defined a class which is all the attributes related to all citizens"

    def __init__(self, language):
        "I defined a function that return the language and print the position"
        self.language = language
        self.print_position()
        self.tolerance=0.5

    def print_position(self):
        "You can change this if you want .I supposed that the country is a 2 by 10 rectangle"
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
        return same_language >= self.tolerance*Moore

    def update(self, citizens):
        "If not happy, then randomly choose new locations until pleased"
        while not self.Pleased(citizens):
            self.print_position()
            
def graphs(agents, cycle_num):
    "Plot the  physical positions  of Citizens after cycle_num rounds of the loop."
    xval0, yval0 = [], []
    xval1, yval1 = [], []
    average_X1, average_Y1 = [], [] #lists aggregating averages for English
    average_X2, average_Y2 = [], [] #lists aggregating averages for Spanish
    # get the posittion  of each speaking citizen
    for citizen in citizens:
        x, y = citizen.position
        if citizen.language == 0:
            xval0.append(x)
            yval0.append(y)
            average_X1.append(sum(xval0)/len(xval0)) #accumulate average X coordinate
            average_Y1.append(sum(yval0)/len(yval0)) #accumulate average Y coordinate
        else:
            xval1.append(x)
            yval1.append(y)
            average_X2.append(sum(xval1)/len(xval1)) #accumulate average X coordinate
            average_Y2.append(sum(yval1)/len(yval1)) #accumulate average Y coordinate
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.plot(xval0, yval0, 's', markerfacecolor='b')
    ax.plot(xval1, yval1, 's', markerfacecolor='r')
    print('the average distance for speaking ennglish is:',sqrt(numpy.average(average_X1)**2 + numpy.average(average_Y1)**2)) #mean position computation for English
    print ('the average distance for speaking spanish is:',sqrt(numpy.average(average_X2)**2 + numpy.average(average_Y2)**2))
    #To number the plots I use this below ,but you can remove it (not necessary)
    ax.set_title('Cycle {}'.format(cycle_num-1 ))
    plt.show()

#below I start from 200 speaking english and 100 spanich ,but you guys can pick any initial values you want.
#Also we may suggest a complicated function that connect the number of people speaking spanich to the number of people speaking english 

# Number of  neighbors,I picked 8 here ,but we can defined to a dynamics of stochastic value to spicy up  the project 
english = rd.randint(400,500)
print ('English Speaking Population= ', english)
spanish = rd.randint(300, 350)
print ('Spanish Speaking Population = ', spanish)
 # The threshold level ,I picked 5

#We can modify this below and find it to be related to some type of function ,to make it exciting for the project



for i in range(1, 2):
    print('for the year',i,'your metrics and plots are')
    english=int(a*english) 
    spanish=int(spanish*b)
    print ('the total population in year',i,'is',english+spanish)

# == Create a list of agents == #
    citizens = [Citizen(0) for i in range(english)]
    citizens.extend(Citizen(1) for i in range(spanish))

#---------------------------------------------------------------#
    n= 1
# ==  run around until no one  want to moave again :no more motion
    while 1:
        print('cycle', n)
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
        
    print('Cycles done!')
# ONCE THIS PROGRAM IS DONE AND NO ONE IS MOVING WE CAN USE networkx  to plot the position of citizen in the country 


            
