import os
from Date_nd_Time import *

def print_costume():
    costume_txt_file = get_costume_txt_file()
    main_data = get_dictionary(costume_txt_file)
    print("")
    print("")
    print("=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=")
    print("S.No","\t","Costume Name","\t","Brand","\t\t","Price","\t","Qunatity")
    print("=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=")
    for key, value in main_data.items():
        print(key,"\t","|",value[0],"\t","|",value[1],"\t","|",value[2],"\t","|",value[3])
#used to display the costumes in the program.

def get_valid_syno(main_data):
    val_data = False
    while val_data == False:

        try:
            print("")
            syno = (input("Enter the Costume Serial Number: \n Type 'esc' to exit the menu ")).lower()

            if syno == "esc":
                
                return "esc"
            else:
                syno = int(syno)
                #using Else if to check the userinput.
                if syno > 0 and syno <= len(main_data):
                    val_data = True
                    return syno
                else:
                    print("")
                    print("Please provide a valid costume ID!")
        except:
            print("")
            print("=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=")
            print(" Please do not enter the input in Strings. ")
            print("=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=")
#Sets the serial number for the costumes.

def get_valid_quantity(main_data, syno,box):
    val_data = False
    while val_data == False:

        try:
            print("")
            qnty = input("Enter the quantity you would like to rent: \n Enter 'cancel' to cancel: ")
            if qnty.lower() != "cancel":
                qnty = int(qnty)
                
            else:
                return "no"
                
            for key,value in main_data.items():
                if key == syno:
                    if qnty >=1 and qnty <= int(value[3]):
                        val_data = True
                        print("")
                        print("Successfully rented ", qnty, " costumes.")
                        print("=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=")
                        box.append([syno,qnty])
                        return qnty
                    elif(qnty > int(value[3])):
                        print("")
                        print("We do not have enough!")
                        print("=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=")
                    else:
                        print("")
                        print("You cannot rent ", qnty, " costumes!!")
                        print("=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=")

        except:
        
            print("")
            print("=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=")
            print("Invalid Input.Please enter correctly")
            print("=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=")

def write_fnc_rent(main_data, syno, qnty):
    try:
        main_data[syno][3] = str(int(main_data[syno][3]) - qnty)
        file = open("Costume.txt","w")
        
        for value in main_data.values():
            write_data = value[0]+","+value[1]+","+value[2]+","+value[3]+"\n"
            file.write(write_data)
        file.close()
        
    except:
        return

def extra_rent(main_data, costume_txt_file, box, date, time, date_time):
    bTotal = 0

    print("")
    print("Select which costume you want to rent.\n")
    print("=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=")
        
    print_costume()  
    syno = get_valid_syno(main_data) 

    if syno == "esc":
            
        return
    
    elif syno != "esc":
        
        qnty = get_valid_quantity(main_data, syno,box)
        write_fnc_rent(main_data, syno, qnty)
        
        loop = True
        while loop == True:
            if qnty == "no":
                return rent()
            print("")
            extra_rent = (input("Do you want to rent more costumes?(yes/no): ")).lower()
            if extra_rent == "no":
    
                loop = False
                print("")
                Name = input("Enter your name? : ")
                print("")
                Contact = input("Enter your Contact Number? : ")

                file_path = os.path.abspath("Bill/"+ Name + date_time +"Rent"+".txt")

                newtxtfile = open(file_path, "w")
                newtxtfile.write("\n________________________________________________________________________________")
                newtxtfile.write("\nName: "+ Name)
                newtxtfile.write("\nContact: "+ Contact)
                newtxtfile.write("\nDate: "+ date)
                newtxtfile.write("\nTime: "+ time)
                newtxtfile.write("\n________________________________________________________________________________\n")


                newtxtfile.write("\n|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=\n")
                newtxtfile.write("                            BILL OF COSTUMES RENTED!")
                newtxtfile.write("\n|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=")
                
                newtxtfile.write("\n________________________________________________________________________________\n")
                newtxtfile.write("S.N"+"\t"+"Costume Name"+"\t"+"Brand"+"\t\t"+"Price"+"\t\t"+"Quantity")
                newtxtfile.write("\n________________________________________________________________________________\n")
        
                for index in range(len(box)):
                    
                    bID = int(box[index][0])
                    bName = main_data[bID][0]
                    bQuantity = int(box[index][1])
                    bBrand = main_data[bID][1]
                    bPrice = float(main_data[bID][2])* bQuantity 
                    bTotal = bTotal + bPrice
                    
                    newtxtfile.write("\n"+str(index+1)+"\t"+bName+"\t\t"+bBrand+"\t"+str(bPrice)+"\t\t"+str(bQuantity))
                    newtxtfile.write("\n________________________________________________________________________________")

                newtxtfile.write("\n"+                                              "  Total sum:  " + str(bTotal))
                newtxtfile.write("\n________________________________________________________________________________")
                newtxtfile.close()

                newtxtfile = open(file_path, "r")
                file_bill = newtxtfile.read()
                print(file_bill)
                newtxtfile.close()
                
                
            elif extra_rent == "yes":
                print("\n=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|==|=|=|=|=|=|=\n")
                print("          Select the costume you want to rent.")
                print("\n=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|==|=|=|=|=|=|=\n")
                    
                print_costume()

                syno = get_valid_syno(main_data)

                if syno == "esc":
                    if box != []:
                        loop = False
                        print("")
                        Name = input("Enter your name? : ")
                        print("")
                        Contact = input("Enter your Contact Number? : ")

                        file_path = os.path.abspath("Bill/"+ Name + date_time +"Rent"+".txt")

                        newtxtfile = open(file_path, "w")
                        newtxtfile.write("\n________________________________________________________________________________")
                        newtxtfile.write("\nName: "+ Name)
                        newtxtfile.write("\nContact: "+ Contact)
                        newtxtfile.write("\nDate: "+ date)
                        newtxtfile.write("\nTime: "+ time)
                        newtxtfile.write("\n________________________________________________________________________________\n")


                        newtxtfile.write("\n|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=\n")
                        newtxtfile.write("                            BILL OF COSTUMES RENTED!")
                        newtxtfile.write("\n|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=")
                        
                        newtxtfile.write("\n________________________________________________________________________________\n")
                        newtxtfile.write("S.N"+"\t"+"Costume Name"+"\t"+"Brand"+"\t\t"+"Price"+"\t\t"+"Quantity")
                        newtxtfile.write("\n________________________________________________________________________________\n")
                
                        for index in range(len(box)):
                            
                            bID = int(box[index][0])
                            bName = main_data[bID][0]
                            bQuantity = int(box[index][1])
                            bBrand = main_data[bID][1]
                            bPrice = float(main_data[bID][2])* bQuantity 
                            bTotal = bTotal + bPrice
                            
                            newtxtfile.write("\n"+str(index+1)+"\t"+bName+"\t\t"+bBrand+"\t"+str(bPrice)+"\t\t"+str(bQuantity))
                            newtxtfile.write("\n________________________________________________________________________________")

                        newtxtfile.write("\n"+                                              "  Total sum:  " + str(bTotal))
                        newtxtfile.write("\n________________________________________________________________________________")
                        newtxtfile.close()

                        newtxtfile = open(file_path, "r")
                        file_bill = newtxtfile.read()
                        print(file_bill)
                        newtxtfile.close()
                        
                    else:
                        return 
    
                elif syno != "esc":
        
                    qnty = get_valid_quantity(main_data, syno, box)
        
                    write_fnc_rent(main_data, syno, qnty)
                    
        
            else:
                print("")
                print("=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=")
                print("Invalid Input. Please Enter yes or no.")
                print("=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=")

def rent_costumes():
    box = []
    date,time = get_datetime()
    date_time = get_dt()
    costume_txt_file = get_costume_txt_file()
    main_data = get_dictionary(costume_txt_file)
    extra_rent(main_data, costume_txt_file, box, date, time, date_time)
    
    
#carries out the rent function in the program
