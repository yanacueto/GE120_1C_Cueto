"""
GE 120: Introductory Object-Oriented Programming for Geomatics
Machine Exercise 3: Functional Programming
Gianna May S. Cueto
2023-02505
"""

# CREATING FUNCTIONS TO BREAK DOWN THE PREVIOUS CODE
from math import cos, sin, radians, sqrt

def getLatitude(distance, azimuth):
    '''
    Compute for the latitude of a given line.

    Input: 
    distance - float
    azimuth - float

    Output:
    latitude - float
    '''
    latitude = -distance * cos(radians(azimuth))
    return latitude

def getDeparture(distance, azimuth):
    '''
    Compute for the departure of a given line.

    Input: 
    distance - float
    azimuth - float

    Output:
    departure - float
    '''
    departure = -distance * sin(radians(azimuth))
    return departure

def azimuthToBearing(azimuth):
    '''
    Compute for the DMS bearing of a given angle.

    Input: 
    azimuth - float

    Output:
    bearing - string
    '''
    if azimuth > 0 and azimuth < 90:
        azi = azimuth
        degrees = int(azi)
        minutes = (azi - degrees) * 60
        minutes_whole = int(minutes)
        seconds = (minutes - minutes_whole) * 60
        seconds_dec = (round(seconds, 2))
        degminsec = str(degrees) + "-" + str(minutes_whole) + "-" + str(seconds_dec)
        bearing = 'S {: ^10} W'.format(degminsec)
    # If the angle is in Quadrant 2
    elif azimuth > 90 and azimuth < 180:
        azi = 180 - azimuth
        degrees = int(azi)
        minutes = (azi - degrees) * 60
        minutes_whole = int(minutes)
        seconds = (minutes - minutes_whole) * 60
        seconds_dec = (round(seconds, 2))
        degminsec = str(degrees) + "-" + str(minutes_whole) + "-" + str(seconds_dec)
        bearing = 'N {: ^10} W'.format(degminsec)
    # If the angle is in Quadrant 1
    elif azimuth > 180 and azimuth < 270:
        azi = azimuth - 180
        degrees = int(azi)
        minutes = (azi - degrees) * 60
        minutes_whole = int(minutes)
        seconds = (minutes - minutes_whole) * 60
        seconds_dec = (round(seconds, 2))
        degminsec = str(degrees) + "-" + str(minutes_whole) + "-" + str(seconds_dec)
        bearing = 'N {: ^10} E'.format(degminsec)
    # If the angle is in Quadrant 4
    elif azimuth > 270 and azimuth < 360:
        azi = 360 - azimuth
        degrees = int(azi)
        minutes = (azi - degrees) * 60
        minutes_whole = int(minutes)
        seconds = (minutes - minutes_whole) * 60
        seconds_dec = (round(seconds, 2))
        degminsec = str(degrees) + "-" + str(minutes_whole) + "-" + str(seconds_dec)
        bearing = 'S {: ^10} E'.format(degminsec)
    # If the angles are exactly on the axis
    elif azimuth == 0:
        bearing = "DUE SOUTH"
    elif azimuth == 90:
        bearing = "DUE WEST"
    elif azimuth == 180:
        bearing = "DUE NORTH"
    elif azimuth == 270:
        bearing = "DUE EAST"
    else:
        bearing = "Invalid input."
    return bearing

# CREATE A SENTINEL CONTROLLED LOOP
first = 1
last = 2
lines = []
sumLat = 0
sumDep = 0
sumDist = 0

# Setting up the distance and azimuth in the program
while True:
    print()
    print("LINE NO.", first, "-", last)

    wrong_format = False
    try:
        distance = float(input("Distance: "))
    except ValueError:
            print("The accepted format is in numerals only. Please abide this format.")
            break
    azimuth = (input("Azimuth from the South: "))
    
    if "-" in str(azimuth): # if user gives DMS
        degrees, minutes, seconds = azimuth.split("-")
        azimuth = (int(degrees) + (int(minutes)/60) + (float(seconds)/3600))%360
    else:
        azimuth = float(azimuth)%360

    bearing = azimuthToBearing(azimuth)
    lat = getLatitude(azimuth=float(azimuth), distance=float(distance))
    dep = getDeparture(azimuth=float(azimuth), distance=float(distance))

    sumLat = sumLat + lat # sumLat += lat is the same as sumLat + lat
    sumDep = sumDep + dep
    sumDist = sumDist + distance

    # Create a tuple of the line
    line = (str(first) + "-" + str(last), distance, bearing, lat, dep)
    lines.append(line)

    # Ask for input
    new_line = input("Add new line? ")
    if new_line.lower() == "yes" or new_line.lower() == "y":
        first = first + 1
        last = last + 1
        continue
    else:
        break

# Printing the program
print("\n") 
print('{: ^10} {: ^20} {: ^20} {: ^20} {: ^30}'.format("LINE NO.", "DISTANCE", "BEARING", "LATITUDE", "DEPATURE"))
for line in lines:
    print('{: ^10} {: ^20} {: ^20} {: ^20} {: ^30}'.format(line[0], line[1], line[2], line[3], line[4]))

print("SUMMATION OF LATITUDE: ", sumLat)
print("SUMMATION OF DEPARTURE: ", sumDep)
print("TOTAL DISTANCE: ", sumDist)

lec = sqrt(sumLat**2 + sumDep**2)
print("LEC: ", lec)

rec = sumDist/lec
print("1: ", rec)

print("************** END **************")

# compass rule
"""
corrlat = (sum of lat/D)*line[1]

constCorrLat = -sumLat/sumDis
constCorrDep = -sumDep/sumDis

for line in lines:
    corrlat = constCorrLat*line[1]
    corrdep = constCorrDep*line[1]

    adjlat = line[3] + corr_lat
    adjdep = line[4] + corr_dep

    lines.append
    print()

use pythagorean for distance
use degrees(atan(dep/lat)) or atan(dep/lat)*(180/math.pi)
"""

'''
Fix the azimuth part para mag-accept pa rin siya ng azimuth in DMS!!!
'''
