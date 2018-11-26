#!/usr/bin/python
#
import string
import random
# @author Anand Patil
# @version November 11/26
# @course Programming 1
# @assign.ment Login and password generator 2018
# @descrip.tion Generating a password


firstName = raw_input("Enter your first name (no dashes nor spaces): ")
lastName = raw_input("Enter your last name (no dashes nor spaces): ")  
try:
    bornYear = input("Enter the year you were born (no letters): ")
    bornYear = abs(bornYear)
except:
    print "You must enter an integer. Exiting code..."
    exit()
randSent = raw_input("Now enter a random sentence: ")

firstName = firstName.lower()
lastName = lastName.lower()
bornYear = bornYear % 100
if bornYear < 10:
    bornYear = "0" + str(bornYear)
else:
    bornYear = str(bornYear)
username = lastName[:5] + firstName[:3] + bornYear


randSent = randSent.replace(" ", "")

rSLeg = len(randSent)
list = []
for i in range(0, 7):
    list.append(randSent[random.randrange(0, rSLeg)])
print list