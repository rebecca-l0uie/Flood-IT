#########################################
# Author : Rebecca Louie
# Date   : June 23rd 2017
# Func   : Desktop game with FLTK graphics 
#		   Written in Python 2.7
# Usage  : python finalFlood.py
#########################################

#!/usr/bin/python
from fltk import *
import random

#Creating button class
class button(Fl_Button):
	def __init__(self, x, y, w, h, label=None):
		Fl_Button.__init__(self,x, y, w, h, label)

#Function to change the colour and add button to the flooded list
# Checks the surrounding buttons around the clicked button		
def flood(w):
	clr = w.color()
	#print clr
	#print flooded
	for item in flooded:
		around = [item+1, item-1, item+17, item-17]
		for i in around:
			if i<0:
				pass
			if blist[i].color() == clr:
				if i not in flooded:
					flooded.append(i)
	for item in  flooded:
		blist[item].color(clr)
		blist[item].redraw()
		#print item
	global amount
	amount=amount-1
	if amount>=0:
		turns.value(str(amount))
	else:
		turns.value('You lost!')
		
global amount
flooded = [18]
ROSE=fl_rgb_color(241,154,154)
BLUE=fl_rgb_color(154,223,241)
MINT=fl_rgb_color(154,241,214)
YELLOW=fl_rgb_color(249,241,123)
PURPLE=fl_rgb_color(172,154,241)
CREAM=fl_rgb_color(255,247,227)
colours=[ROSE, BLUE, MINT, YELLOW, PURPLE, CREAM]
gs = 17
win = Fl_Window(0,0,gs*30-60,gs*30+40,'Flood')
win.begin()
win.color(fl_rgb_color(229,229,229))
blist = []
for y in range(0,gs):
	for x in range(0,gs):
		X =30*x
		Y =30*y
		blist.append(button(X-30,Y-30,30,30))
		blist[-1].box(FL_FLAT_BOX)
		c=random.choice(colours)
		blist[-1].color(c)
		blist[-1].colour=c

grid = []

#Adding buttons to the screen
for x in range(gs,gs*gs-gs):
	if x%gs!=0 and x%gs!=gs-1:
		grid.append(x)
innergrid = set(grid)
agrid = set(range(0,gs*gs))
outring = agrid-innergrid
for x in outring:
	blist[x].color(fl_rgb_color(229,229,229))
	blist[x].deactivate()
	
bclist = []
C=iter([ROSE, BLUE, MINT, YELLOW, PURPLE, CREAM])

#Assigning colours
for x in range(0,6):
	cbut=[]
	cbut.append(button((40*x+20),gs*30-30,40,40,None))
	n=next(C)
	cbut[-1].color(n)
	cbut[-1].colour=n
	cbut[-1].callback(flood)
amount = 30 #Setting the number of turns
turns = Fl_Input(40*6+65,487,100,30, 'Turns') #Display for turns
turns.value(str(amount)) #Displaying numbers of turns 
turns.align(FL_ALIGN_TOP)
win.end()
win.show()
Fl.run()
