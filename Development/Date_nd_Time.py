
import datetime

def get_datetime():
    import datetime
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)
    hour = str(datetime.datetime.now().hour)
    minute = str(datetime.datetime.now().minute)
    second = str(datetime.datetime.now().second)

    date = str(year + month + day)
    time = str(hour + minute + second)
    return date,time

def get_dt():
    import datetime
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)
    hour = str(datetime.datetime.now().hour)
    minute = str(datetime.datetime.now().minute)
    second = str(datetime.datetime.now().second)

    date_time = str(year + month + day + hour + minute + second)
    
    return date_time


def get_costume_txt_file():
    file = open("Costume.txt", "r")
    data = file.readlines()
    file.close()
    return data
#the above function is used to read the text file in the program.

def get_dictionary(costume_txt_file):
    data = {}
    for index in range(len(costume_txt_file)):
        data[index+1] = costume_txt_file[index].replace("\n","").split(",")
    return data
#the above function is used to save the above text file in a dictionary within the program.





    
