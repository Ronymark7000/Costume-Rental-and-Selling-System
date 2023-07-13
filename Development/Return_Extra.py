
from Date_nd_Time import *

import os



def print_return_costume():
    costume_txt_file = get_costume_txt_file()
    main_data = get_dictionary(costume_txt_file)

    print("\n")
    print("=|=|=|=|=|=|=|=|=|=|=|=|=|=")
    print("S.No","\t","Costume Name")
    print("=|=|=|=|=|=|=|=|=|=|=|=|=|=")
    
    for key,value in main_data.items():
        
        print(key,"\t",value[0])
        
def get_return_syno(main_data):
    val_data = False
    while val_data == False:
        
        try:
            print("")
            return_syno = input("Enter the costume you want to return? \n Enter 'esc' to exit to menu): ")

            if return_syno == "esc":                
                return "esc"
            
            elif return_syno != "esc":
                
                return_syno = int(return_syno)
                
                if return_syno > 0 and return_syno <= len(main_data):
                    val_data = True

                    return return_syno
                else:
                    print("")
                    print("=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=")
                    print("Please provide a valid costume ID!")
                    print("=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=")
                
        except:
            print("")
            print("=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=")
            print(" Please do not enter the input in Strings. ")
            print("=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=")

def get_return_qnty(main_data, return_syno):
    loop = False
    while loop == False:

        try:
            print("")
            return_qnty = input("Enter the quantity you would like to return: /n Enter 'no' to cancel: ")
            
            for key,value in main_data.items():
                if key == return_syno:
                            
                    if return_qnty == "no":
                        return "no"
                    else:
                        return_qnty = int(return_qnty) 

                        print("=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=")
                        print(return_qnty,value[0],"returned successfully.")
                        print("=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=")
                        
                        return return_qnty

        except:
            print("")
            print("=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=")
            print(" Please do not enter the input in Strings. ")
            print("=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=")



def write_fnc_return(main_data, return_syno, return_qnty):
    try:  
        main_data[return_syno][3] = str(int(main_data[return_syno][3]) + return_qnty)
        file = open("Costume.txt","w")
        
        for value in main_data.values():
            write_data = value[0]+","+value[1]+","+value[2]+","+value[3]+"\n"
            file.write(write_data)
        file.close()
        
    except:
        return

def extra_return(main_data,costume_txt_file,box,date,time,date_time):
    bTotal = 0
    
    print("")
    print("Select which costume you want to return.\n")
    print("=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=")
        
    print_return_costume()

    return_syno = get_return_syno(main_data)

    if return_syno == "esc":

        return
    
    elif return_syno != "esc":
        
        return_qnty = get_return_qnty(main_data, return_syno)
            
        box.append([return_syno, return_qnty])

        write_fnc_return(main_data, return_syno, return_qnty)
        loop = True
        while loop == True:
            

            if return_qnty == "none":
                
                return ret()
            
            extra_return = (input("Do you want to return more costumes?(yes/no): ")).lower()
            
            if extra_return == "no":
                
                print("")
                Name = input("Enter your name? : ")
                print("")
                Contact = input("Enter your Contact Number? : ")
                print("")
                beforeTime = (input("Is the costume returned before its due?(yes/no): ")).lower()

                if beforeTime == "yes":
                    file_path = os.path.abspath("Bill/"+ Name + date_time +"Return"+".txt")

                    newtxtfile = open(file_path, "w")
                    newtxtfile.write("\n________________________________________________________________________________")
                    newtxtfile.write("\nName: "+ Name)
                    newtxtfile.write("\nContact: "+ Contact)
                    newtxtfile.write("\nDate: "+ date)
                    newtxtfile.write("\nTime: "+ time)
                    newtxtfile.write("\n________________________________________________________________________________\n")


                    newtxtfile.write("\n|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=\n")
                    newtxtfile.write("                            BILL OF COSTUMES RETURNED!")
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
                        newtxtfile.write("\n____________________________________________________________________________")

                    newtxtfile.write("\n"+"\t\t" + "  Total sum:  " + str(bTotal))
                    newtxtfile.write("\n____________________________________________________________________________")
                    newtxtfile.close()

                    newtxtfile = open(file_path, "r")
                    file_bill = newtxtfile.read()
                    print(file_bill)
                    newtxtfile.close()

                    loop = False
                  
                    
                elif beforeTime == "no":
                    Days = int(input("Number of days late?(Fine Per Day = +50):"))

                    file_path = os.path.abspath("Bill/" + Name + date_time + "RETURN"+".txt")

                    newtxtfile = open(file_path, "w")
                    newtxtfile.write("\n________________________________________________________________________________")
                    newtxtfile.write("\nName: "+ Name)
                    newtxtfile.write("\nContact: "+ Contact)
                    newtxtfile.write("\nDate: "+ date)
                    newtxtfile.write("\nTime: "+ time)
                    newtxtfile.write("\n________________________________________________________________________________\n")


                    newtxtfile.write("\n|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=\n")
                    newtxtfile.write("                            BILL OF COSTUMES RETURNED!")
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
                        bFine = float(50*Days)
                        bFinalTotal = bTotal + bFine
                        
                        newtxtfile.write("\n"+str(index+1)+"\t"+bName+"\t\t"+bBrand+"\t"+str(bPrice)+"\t\t"+str(bQuantity))
                        newtxtfile.write("\n____________________________________________________________________________")

                    newtxtfile.write("\n"+"\t" +  "Final Proce without fine : " + str(bTotal))
                    newtxtfile.write("\n"+"\t" +  "Total Fine               : " + str(bFine))
                    newtxtfile.write("\n"+"\t" +  "Grand Total:             : " + str(bFinalTotal))
                    newtxtfile.write("\n____________________________________________________________________________")
                    newtxtfile.close

                    newtxtfile = open(file_path, "r")
                    file_bill = newtxtfile.read()
                    print(file_bill)
                    newtxtfile.close()
    
                    loop = False            
                    
            elif extra_return == "yes":
                print("\n=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|==|=|=|=|=|=|=\n")
                print("          Select the costume you want to return.")
                print("\n=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|==|=|=|=|=|=|=\n")
                        
                print_return_costume()
                return_syno = get_return_syno(main_data)

                if return_syno == "esc":

                    if box != []:
                        loop = False
                        
                        print("")
                        Name = input("Enter your name? : ")
                        print("")
                        Contact = input("Enter your Contact Number? : ")
                        print("")
                        beforeTime = (input("Is the costume returned before its due?(yes/no): ")).lower()

                        if beforeTime == "yes":
                            file_path = os.path.abspath("Bill/" + Name + date_time + "RETURN"+".txt")

                            newtxtfile = open(file_path, "w")
                            newtxtfile.write("\n________________________________________________________________________________")
                            newtxtfile.write("\nName: "+ Name)
                            newtxtfile.write("\nContact: "+ Contact)
                            newtxtfile.write("\nDate: "+ date)
                            newtxtfile.write("\nTime: "+ time)
                            newtxtfile.write("\n________________________________________________________________________________\n")


                            newtxtfile.write("\n|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=\n")
                            newtxtfile.write("                            BILL OF COSTUMES RETURNED!")
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
                                newtxtfile.write("\n____________________________________________________________________________")

                            newtxtfile.write("\n"+"\t\t" + "  Total sum:  " + str(bTotal))
                            newtxtfile.write("\n____________________________________________________________________________")
                            newtxtfile.close()

                            newtxtfile = open(file_path, "r")
                            file_bill = newtxtfile.read()
                            print(file_bill)
                            newtxtfile.close()
                            
                        elif beforeTime == "no":
                            Days = int(input("Number of days late?(Fine Per Day = +50):"))

                            file_path = os.path.abspath("Bill/" + Name + date_time + "RETURN"+".txt")

                            newtxtfile = open(file_path, "w")
                            newtxtfile.write("\n________________________________________________________________________________")
                            newtxtfile.write("\nName: "+ Name)
                            newtxtfile.write("\nContact: "+ Contact)
                            newtxtfile.write("\nDate: "+ date)
                            newtxtfile.write("\nTime: "+ time)
                            newtxtfile.write("\n________________________________________________________________________________\n")


                            newtxtfile.write("\n|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=\n")
                            newtxtfile.write("                            BILL OF COSTUMES RETURNED!")
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
                                bFine = float(50*Days)
                                bFinalTotal = bTotal + bFine
                                
                                newtxtfile.write("\n"+str(index+1)+"\t"+bName+"\t\t"+bBrand+"\t"+str(bPrice)+"\t\t"+str(bQuantity))
                                newtxtfile.write("\n____________________________________________________________________________")

                            newtxtfile.write("\n"+"\t" +  "Final Proce without fine : " + str(bTotal))
                            newtxtfile.write("\n"+"\t" +  "Total Fine               : " + str(bFine))
                            newtxtfile.write("\n"+"\t" +  "Grand Total:             : " + str(bFinalTotal))
                            newtxtfile.write("\n____________________________________________________________________________")
                            newtxtfile.close

                            newtxtfile = open(file_path, "r")
                            file_bill = newtxtfile.read()
                            print(file_bill)
                            newtxtfile.close()
                    else:
                        
                        return

                elif return_syno != "esc":
                    return_qnty = get_return_qnty(main_data, return_syno)
            
                    box.append([return_syno, return_qnty])

                    write_fnc_return(main_data, return_syno, return_qnty)

            else:
                print("")
                print("=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=")
                print("Invalid Data.Please enter correct input!!!")
                print("=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=")
def ret():
    box = []
    date,time = get_datetime()
    date_time = get_dt()
    costume_txt_file = get_costume_txt_file()
    main_data = get_dictionary(costume_txt_file)
   
    extra_return(main_data, costume_txt_file, box, date, time, date_time)
#carries out the retunr function of the program

