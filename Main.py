#!/usr/bin/python
#
import string
import random
import time
# @author Anand Patil
# @version November 11/26
# @course Programming 1
# @assign.ment Login and password generator 2018
# @descrip.tion Generating a password

while True:
    firstName = raw_input("Enter your first name: ")
    lastName = raw_input("Enter your last name: ")  
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
    finalStr = ""
    i = 0
    for i in range(6):
        list.append(randSent[random.randrange(0, rSLeg)])
    
    for i in range(3):
        finalStr = finalStr + list[i]
    
    for i in range(2):
        finalStr = finalStr + str(random.randrange(0, 9))
    
    t = 3
    for i in range(3):
        finalStr = finalStr + list[t]
        t += 1
    
    print "Username:", username + "."
    print "Password:", finalStr + "."
    time.sleep(1)
    con = raw_input("Would you like to do it again? \n 'y' for yes and 'n' for no: ")
    if con.lower() == "n":
        print "Exiting..."
        exit()