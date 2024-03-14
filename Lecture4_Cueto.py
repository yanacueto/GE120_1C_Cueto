# # CREATING A FUNCTION

# print("Hello world")

# # Convert a number into a string
# a = 1
# b=str(a)
# print(type(b))

# # Defining our own functions
# def shout(word):
#     print(number)
#     print(word + "!")
#     print("I created this function")

# number = 1

# shout("BONGGA")

# number = 3

# shout("JUSTIN")
# # print(word) is not defined because in the global perspective, we did not define "word", only in a local code

# # Variables inside fucnfctions are not available globally

# # To show that function first finds a word in the local context
# # def shout(word):
# #     print(word + "!")

# # shout()

# # Use global variable if not in local
# def shout(word1, word2):
#     print(word1+"!")
#     print(word2+".....")
          
# shout("Mafe", "Omar")

# def shout(word1, num_ulit_last_letter):
#     '''
#     Given a word, kunin yung last letter, ulitin ng ilang beses
#     tapos kapag prinint, print the word, plus inulit na last letter 
#     + exclamation point.
#     '''
#     print(word1.upper()+word1[-1].upper()*(num_ulit_last_letter-1)+"!!!!!")
          
# shout("Mafe", 5)

# print(shout.__doc__)

# print(len.__doc__)
# help(len)

# Types of Arguments

# def convertDMStoDEG(dms="118-25-14.48", name="JANNAH"):
#     '''
#     Convert DMS to degrees

#     Arguments
#         dms-string
#     '''
#     degrees, minutes, seconds = dms.split("")
#     dd = int(degrees) + (int(minutes)/60) + (float(seconds)/3600)
#     print(name + " , ETO YUNG VALUE: ", round(dd,6))

# convertDMStoDEG()

# def print_as_table(*lines):
#     print("\n") 
#     print('{: ^10} {: ^20} {: ^20}'.format("LINE NO.", "DISTANCE", "BEARING"))
#     for line in lines:
#         print('{: ^10} {: ^20} {: ^20}'.format(line[0], line[1], line[2]))

# line1 = (1, '112.13', 'N 30.0 E')
# line2 = (2, '89.3', 'S 32.1 W')

# print_as_table(line1, line2)

# RETURNING FROM A FUNCTION
# result = convertDMStoDEG("12-12-12")
# result += 10
# print(result)

# printing after returning something
def getDirection(degrees):
    '''
    Gives the direction of an angle

    Input:
    degrees - float

    Output:
    quadrant - string
    '''
    print("HELLO EVERYONE")
    if degrees > 0 and degrees < 90:
        return "S-W"
    elif degrees > 90 and degrees < 180:
        return "N-W"
    elif degrees > 180 and degrees < 270:
        return "N-E"
    elif degrees > 270 and degrees < 360:
        return "S-E"
    else:
        return "ewan q kung nasaan yan"
    
    # print("HELLO EVERYONE") # won't work kasi may return na agad if after mo pa ilalagay

direction = getDirection(100) # save sa variable when you call a return function kasi it won't work otherwise
print(direction)
    
# dms = "100-12-14"
# dd = convertDMStoDEG(dms)
# direction = getDirection(dd)
# print(direction) 