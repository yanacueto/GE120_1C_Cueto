"""
GE 120: Introductory Object-Oriented Programming for Geomatics
Machine Exercise 3: Functional Programming
Gianna May S. Cueto
2023-02505
"""

# CREATING FUNCTIONS TO BREAK DOWN THE PREVIOUS CODE
from math import cos, sin, radians, sqrt, atan, degrees

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
"""
def getCorrLat(sumLat, sumDist):
    '''
    Compute for the correct latitude of a given line.

    Input: 
    sumLat - float
    sumDist - float

    Output:
    corrlat - float
    '''
    corrlat = (sumLat/sumDist)*line[1]
    return corrlat

def getCorrDep(sumDep, sumDist):
    '''
    Compute for the correct departure of a given line.

    Input: 
    sumDep - float
    sumDist - float

    Output:
    corrdep - float
    '''
    corrdep = (sumDep/sumDist)*line[1]
    return corrdep

def getAdjDis(adjlat, adjdep):
    '''
    Obtain the adjusted distance of a given line.

    Input: 
    adjlat - float
    adjdep - float

    Output:
    adjdis - float
    '''
    adjdis = sqrt(adjlat**2 + adjdep**2)
    return adjdis

def getAdjBear(adjlat, adjdep):
    '''
    Obtain the adjusted bearing of a given line.

    Input: 
    adjlat - float
    adjdep - float

    Output:
    adjbear - float
    '''
    adjbear = degrees(atan(adjdep/adjlat))
    return adjbear
"""
# CREATING A TABLE FOR THE RAW DISTANCES, BEARINGS, LATITUDES, AND DEPARTURES
first = 1
last = 2
lines = []
sumLat = 0
sumDep = 0
sumDist = 0

# Setting up the distance and azimuth in the program
while True:
    print("\n") 
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
print("\033[39mTABLE OF RAW DISTANCES AND BEARINGS")
print('{: ^10} {: ^20} {: ^20} {: ^20} {: ^20}'.format("LINE NO.", "DISTANCE", "BEARING", "LATITUDE", "DEPARTURE"))
for line in lines:
    print('{: ^10} {: ^20} {: ^20} {: ^20} {: ^20}'.format(line[0], line[1], line[2], round(line[3], 8), round(line[4], 8)))

print("SUMMATION OF LATITUDE: ", sumLat)
print("SUMMATION OF DEPARTURE: ", sumDep)
print("TOTAL DISTANCE: ", sumDist)

lec = sqrt(sumLat**2 + sumDep**2)
print("LEC: ", lec)

rec = sumDist/lec
print("REC: 1:", rec)

print("************** END **************")
"""
CREATING A TABLE FOR THE ADJUSTED DISTANCES AND BEARINGS
first = 1
last = 2
adjusted = []
corrlat = 0
corrdep = 0
constCorrLat = 0
constCorrDep = 0
adjlat = 0
adjdep = 0

while True:
    print("\n") 
    print()

    # Using the Compass Rule for corrections
    for line in lines: 
        constcorrlat = getCorrLat(sumLat, sumDist)
        constcorrdep = getCorrDep(sumDep, sumDist)

        adjlat = line[3] + corrlat
        adjdep = line[4] + corrdep

        adjdis = sqrt(adjlat**2 + adjdep**2)
        adjbear = degrees(atan(adjdep/adjlat))

        # adjustedDis = getAdjDis(adjlat, adjdep)
        # adjustedBear = getAdjBear(adjlat, adjdep)

    # Create a tuple of the line
    adjust = (str(first) + "-" + str(last), adjdis, adjbear)
    adjusted.append(adjust)

    print("\n")
    print("ADJUSTED DISTANCES AND BEARINGS")
    print('{: ^20} {: ^20} {: ^30}'.format("LINE NO.", "ADJUSTED DISTANCE", "ADJUSTED BEARING"))
    
    for adjust in adjusted:
        print('{: ^20} {: ^20} {: ^30}'.format(line[0], line[1], line[2]))
"""