from Date_nd_Time import *
from Rent_Extra import *
from Return_Extra import *

def start_message():
    print ("")
    print ("                      Welcome to Our Costume rental Store ")
    print ("")
    print("|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|")
#The above function is used to display the starting message of the program.


def choose_options():
    print("")
    print ("Choose one of the following options:")
    print ("")
    print ("Would you like to rent the costume?    (1)")
    print ("Would you like to return the costume?  (2)")
    print ("Would you like to exit the program?    (3)")
    print()
#The above function display the first interactive options that the user can choose.    


def user_end_message():
    print ("-----------------------------Thank You for you time-----------------------------")
#The above function is used to display the following message after the user ends the program.


def startOptions():
    loop = True
    while loop == True:
        start_message()
        choose_options()

        try:
            print("")
            usr_input = int(input("Pick Your Option: "))
            if  usr_input == 1:
                rent_costumes()
            elif  usr_input == 2:
                ret()
            elif  usr_input == 3:
                user_end_message()
                loop = False
            else:
                print("")
                print("Invalid Input!!!")
                print("Chose a valid option!")
                   
        except:
            print("\n")
            print("=|=|=|=|=|=|=|=|=|=|=|=|=|=|=")
            print("The following Input is Invalid")
            print("=|=|=|=|=|=|=|=|=|=|=|=|=|=|=")


    
startOptions()
