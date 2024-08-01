import random, tempatureConverter

#Convert fahrenheit to celsius 

#List of color based temaptures
#<90 Degrees and up: red> <75 - 89 Degrees: yellow <64 - 74 Degrees: green>  <63 and Below blue>

#print tempature in both fahrenheit and celsius, print in the color assigned to the tempature
#user input to take in tempature


#-------REFINEMENT--------------------REFINEMENT------------------REFINEMENT----------------REFINEMENT--------------REFINEMENT
#Format Celsius to show only one place after the decimal
# i.e, 22.8888888888 --> 22.8


#---------------------------------Code Setup-------------------------------
#1 import random
#2, from colorama import Force 
#3, 5 variables to hold the color
    #i.e., red = Force.RED

    #4 def tempatureConverter(user_input):
       #5 FAHRENHEIT_TO_CELSIUS = This variable is to do conversion from Fahrenheit to Celsius 
       #6 Conditional if/elif/else: total of 4 statements
       #6a, pint statements that print Fahrenheit and tempature to color associated
       #i.e., print("Fahrenheit: ", red, tempature, black)
       #i.e., print("Celsius: ", red, tempature, black)

       #Call function and pass parameters to function

#-------------------------------ACTUAL CODE---------------------------------
import random
from colorama import Fore

red = Fore.RED 
black = Fore.BLACK  
green = Fore.GREEN
blue = Fore.BLUE
yellow = Fore.YELLOW

def temperatureConverter(user_input):
    FAHRENHEIT_TO_CELSIUS = (user_input - 32) * (5/9)

    if(user_input >= 90):
       print("Fahrenheit: ", red, user_input, black)
       print("Celsius: ", red, "{0:4.1f}".format(FAHRENHEIT_TO_CELSIUS), black)
    elif(user_input <= 75) & (user_input >= 89):
       print("Fahrenheit: ", yellow, user_input, black)
       print("Celsius", yellow, "{0:4.1f}".format(FAHRENHEIT_TO_CELSIUS), black)
    elif(user_input >= 64) & (user_input <= 74):
       print("Fahrenheit: ", green, user_input, black)
       print("Celsius ", green, "{0:4.1f}".format(FAHRENHEIT_TO_CELSIUS), black)
    elif(user_input <=63):
       print("Fahrenheit ", blue, user_input, black)
       print("Celsius ", blue, "{0:4.1f}".format(FAHRENHEIT_TO_CELSIUS), black)

user=float(input("Enter a tempature in Fahrenheit to convert to Celsius:    "))

for x in range(5):
       temperatureConverter(user)
       user=float(input("Enter a tempature in Fahrenheit to convert to Celsius:  "))

       
     
