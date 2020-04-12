def formula(factor):                            #formula used to determine lift
    global lift
    lift = lift * factor + 5
    return lift

def DFactor(weight):                            #check to determine factor
    global factor
    if weight > 0 and weight < 51:
        factor = 1.0
    if weight > 50 and weight < 81:
        factor = 1.1
    if weight > 80 and weight < 101:
        factor = 1.5
    return factor

while True:
    while True:
        try:                                    #try code within try if error occurs execute code under except
            weight = input("enter weight, between 0 and 101, or enter 'exit' to exit the program: ")
            if weight == 'exit':                #check if input string is equal to string exit if so exit()
                break                           #exit() is also possible but results in an error in command prompt
            
            weight = float(weight)              #make weight a float to be able to compare to int or float types
            
            if weight > 0 and weight < 101:     #check if float weight is between acceptable limits 
                break
            else:
                print ('Entered value is not accepted, please try again:')
        except:                                 #try code within try if error occurs execute code under except
            print('Entered value is not accepted, please try again: ')
    try:
        lift = 10
        DFactor(weight)
        
        for i in range(12):                         #loop 12 times
            i += 1                                  # i+1 because i start counting at 0
            formula(factor)                         #run formule with factor as input
            if lift < 100:                          #if lift not to high execute next line
                print("After", i,"months, you can lift", int(lift),"kilograms.")
    except:
        break
