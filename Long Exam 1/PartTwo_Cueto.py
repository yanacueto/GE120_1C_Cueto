"""
GE 120: Introductory Object-Oriented Programming for Geomatics
First Long Exam, Part 2: Coding
Gianna May S. Cueto
2023-02505
"""

# PRINTING A TITLE FOR THE PROGRAM
print("DIRECT LEVELLING CALCULATOR")
print("initialized by Gianna May S. Cueto")
print("*** a program that performs direct levelling computations with the assumption of a closed-loop survey***")

# IMPORTING MATH FUNCTIONS
from math import sqrt

# DEFINING SELF-MADE FUNCTIONS
def floatInput(prompt):
    '''
    asks for inputs and returns outputs as float
    '''
    input == float(prompt)
    return input

def getHeight(relev, backsight):
    '''
    Input:
    relev - float
    backsight - float

    Output:
    height - float
    '''
    height = relev + backsight
    return height

def getNewElev(hi, foresight):
    '''
    Input:
    hi - float
    foresight - float

    Output:
    elevation - float
    '''
    elevation = hi - foresight
    return elevation

# CREATING A SENTINEL-CONTROLLED LOOP
levelling_table = []
total_distance = 0
tp_counter = 1

ielev = float(input("Initial Elevation of BM0: "))

while True:
    print()

# ASKING FOR INPUTS
    relev = float(input("Running Elevation: "))

    backsight = float(input("Backsight (m): "))
    foresight = float(input("Foresight (m): "))
    distance = float(input("Distance to Next TP (m): "))

    hi = getHeight(relev, backsight)
    newrelev = getNewElev(hi, foresight)

    total_distance = total_distance + distance

    if relev == 100:
        newrelev = hi - backsight
    else:
        newrelev = hi - foresight

    # CREATING A TUPLE OF THE LIST
    lt = (str(tp_counter), backsight, hi, foresight, newrelev)
    levelling_table.append(lt)

    # ASKING FOR A NEW MEASUREMENT
    new_meas= input("Do you want to create a new measurement? ")
    if new_meas.lower() == "yes" or new_meas.lower() == "y":
        tp_counter = tp_counter + 1
        continue
    else: 
        new_meas.lower() == "no" or new_meas.lower() == "n"
        break

    """
    [hindi na po me abot sir so cinomment q na lang t-t]
    
    COMPUTING FOR THE ERROR
    surverror = bmfinal - bminitial
    
    COMPUTING FOR THE ALLOWABLE ERROR
    allowerror = sqrt(distance*1000)

    CLASSIFYING THE SURVEY
    if allowerror >= 1/1000:
        print("FIRST ORDER ACCURACY")
    elif allowerror >= 1/50000:
        print("SECOND ORDER ACCURACY")
    elif alloweror >= 1/20000:
        print("THIRD ORDER ACCURACY")
    else:
        print("ERROR TOO LARGE")
    """
    
# PRINTING THE PROGRAM
print("\n") 
print('{: ^20} {: ^20} {: ^20} {: ^20} {: ^20}'.format("STATION","BACKSIGHT", "HEIGHT OF INST.", "FORESIGHT", "ELEVATION"))

for lt in levelling_table:
    print('{: ^20} {: ^20} {: ^20} {: ^20} {: ^20}'.format(lt[0], lt[1], lt[2], lt[3], lt[4]))

print("TOTAL DISTANCE: ", total_distance)
print("*** END ***")