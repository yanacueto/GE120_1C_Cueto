"""
GE 120: Introductory Object-Oriented Programming for Geomatics
Machine Exercise 2: Control Structures
Gianna May S. Cueto
2023-02505
"""

# CREATE A SENTINEL-CONTROLLED LOOP (WHILE LOOP)
first = 1
last = 2
lines = []

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

# If the azimuth is in DMS format
    if "-" in azimuth:
        degrees, minutes, seconds = azimuth.split("-")
        azimuth = (int(degrees) + (int(minutes)/60) + (float(seconds)/3600))%360
    else:
        azimuth = float(azimuth)%360

# Format for Variation of Azimuths
# Take note that the angles are in Azimuth from the South.
    # If the angle is in Quadrant 3
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
        break

    # Create a tuple of the line
    line = (str(first) + "-" + str(last), distance, bearing)
    lines.append(line)

    # Ask for a new line through the input function
    goback = input("Do you want to end the traverse? ")
    if goback.lower() == "yes" or goback.lower() == "y":
        break
    else:
        new_line = input("Add new line? ")
    if new_line.lower() == "yes" or new_line.lower() == "y":
        first = first + 1
        last = last + 1
        continue

# Printing the program
print("\n") 
print('{: ^10} {: ^20} {: ^20}'.format("LINE NO.", "DISTANCE", "BEARING"))
for line in lines:
    print('{: ^10} {: ^20} {: ^20}'.format(line[0], line[1], line[2]))
print("************** END **************")
