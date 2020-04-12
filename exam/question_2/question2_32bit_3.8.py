import math

def InfoContent(ListP):
    ListIC = []
    for x in ListP:
        IC = -math.log2(float(x))
        ListIC.append(round(IC,2))
    print('The Information content of each possible outcomes are:',ListIC)
    return()

def entropy(ListP):             #formula for entropy
    ListE = []
    for x in ListP:
        y = 1 / float(x)
        z = math.log2(y)
        Ey = float(z) * float(x)
        ListE.append(Ey)
    Ey = sum(ListE)
    print("The entropy is", round(Ey, 2))
    return()

ListP = []  #ListP is the list in which all the items/values will be added

while True:
    try:
        Pj = input("enter the probability of possible outcomes: ")

            #check if input contains / if so convert into a float
        
        if "/" in Pj:                       #make sure the float number will be shown with 2 digit after . in the list
            a,b = Pj.split("/",)
            Pj_Value = float(a) / float(b)
            ListP.append(round(Pj_Value, 2))

        #check if input contains % if so convert into a float 
            
        elif "%" in Pj:
            Pj_Value = Pj[:Pj.find("%")]
            Pj_Value = float(Pj_Value) / 100
            print(Pj_Value)
            ListP.append(round(Pj_Value, 2))

        #check if empty data has been entered
        
        elif Pj == "":
            break

        #check if integer has been entered if not error will occur and except loop will be executed 
        
        else:
            Pj = float(Pj)
            ListP.append(Pj)
        
    except:
        print("Entered value is not accepted, please try again: ")

print("ListP is",ListP)
InfoContent(ListP)
entropy(ListP)

#   make sure percentages also wil be accepted by removing % sign and divide by 100
#   I(xj) = log2(1/p(xj)) = -log2(p(xj))
#   H(xj) = n som j=1 p(xj)log2(1/p(xj))        n in the formula is in the code the same as len(ListP)
#   answer should be given as float with 2 digits after .
#   after empty data show answer
#   2 ^ Ey / Pj = Pj

