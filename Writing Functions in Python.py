def is_leap(year):
    leap = False
    if(year % 400 == 0):
        leap = True
    elif(year % 4 == 0 and year % 100 != 0):
        leap = True
    return leap
    
#Python uses indentations to determine how things work. 
#def name(arguements) is used to create a function be sure to have a return type. 
