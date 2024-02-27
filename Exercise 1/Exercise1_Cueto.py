"""
GE 120: Introductory Object-Oriented Programming for Geomatics
Machine Exercise 1: Procedural Programming
Gianna May S. Cueto
2023-02505
"""

# DECIMAL DEGREES TO DEGREE-MINUTE-SECONDS
dd = 118.42069
print("This is the given:", dd)
# Obtain the degrees part of the given.
degree = int(dd)
print("This is the obtained degrees part of the given in integer format:", degree)
# Obtain the minutes part of the given but take note that it is still in degree format.
minutes = dd - degree
print("This is the obtained minutes part of the given in degree format:", minutes)
# Obtain the minutes part of the given in minute format.
minutes = (dd - degree) * 60
print("This is the obtained minutes part of the given:", minutes)
# This is done to obtain the integer part of the obtained minutes.
minutes_whole = int(minutes)
print("This is the obtained minutes part of the given in integer format:", minutes_whole)
# Obtain the seconds part of the given.
seconds = (minutes - minutes_whole) * 60
print("This is the obtained seconds part of the given:", seconds)
# Obtain the rounded up version of the seconds part of the given.
seconds_dec = (round(seconds, 2))
print("This is the obtained seconds part of the given in rounded decimal format:", seconds_dec)
"""
In printing the result, we use the string function to display it as a string.
We also used the round function to only display two (2) decimal places as it is the required output of the script.
"""
print("DMS: " + str(degree) + "-" + str(minutes_whole) + "-" + str(seconds_dec))


# DEGREE-MINUTE-SECONDS TO DECIMAL DEGREES
# The dms value must be a string input.
dms = "118-25-14.48"
# Obtain the values of the string input separately by using the split function.
values = dms.split("-")
degrees = int(values[0])
minutes = int(values[1])
seconds = float(values[2]) # Use the float function so that decimals remain in the given.
"""
Solve for the decimal degrees by using the conversion factors:
1 degree = 60 minutes
1 minute = 60 seconds
1 degree = 3600 seconds 
"""
dd = degrees + (minutes / 60) + (seconds / 3600)
# In printing the result, use the round function to only display six (6) decimal places to check if it matches with the given in the first script.
print("DD:", round(dd, 6))