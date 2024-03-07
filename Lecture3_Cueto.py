# Lecture 3 Notes

#LISTS
listahan = ["mafe", "justin", "mika", "uste"]

#Print [mika]
print(listahan[2])

# subset of the list, Print [mafe] and [justin]
print(listahan[0:2])
print(listahan[1:3])

# Print starting the start
print(listahan[:3])

# Print start from index
print(listahan[2:])

# Print from negative number starts from the last one in the list (reversed order)
print(listahan[-1])
print(listahan[-3])

# Print from nasa gitna ng -3 and 3; gets first item, last item, then in between
print(listahan[-3:3])

#Addition of Lists
print(listahan[0:2] + listahan[2:4])
print(listahan[0:4])

# Change elements
listahan[0] = "chelzy"
print(listahan)

#TUPLES
tuple_1 = ("maja", "jannah", "jewel")
print(tuple_1)

# Tuples are immutable
print(tuple_1[0])
# tuple_1[0] = "quinmar"
# print(tuple_1)

# NESTED LISTS
# Access list first then element to print element in a list
list_1 = [ ["apple", "bola", "carton"], ["apricot", "banana", "cow"] ]
print(list_1)
print(list_1[0][2])

# NESTED TUPLES
tuple_2 = ((12.12444, -12.12414), (35.4837487, -727.287287), (211.2282, 29.12783))
print(tuple_2[2][0])

# DICTIONARIES
dog = {
        "name": "Bogart",
        "age": 2,
        "color": "white",
        "favorite_num": 3.14,
        1.113: 45 # pwede si number as key (float or int)
       }
print(dog[1.113])
print(dog.values()) # returns a list of values
print(dog.keys()) # returns a list of keys

# Can change an element's value
dog["favorite_num"] = 39
print(dog["favorite_num"])

# BOOLEAN DATA TYPES
grade = 85
if grade >= 92:
    print("YAHOO")
if grade >= 60:
    print("NICE")
else:
    print("SAD")

# Printed both YAHOO and NICE since hindi naka-elif
# grade = 93
# if grade >= 92:
#     print("YAHOO")
# if grade >= 60:
#     print("NICE")
# else:
#     print("SAD")

# Kung gusto mo na NICE lang
grade = 93
if grade >= 92:
    print("YAHOO")
elif grade >= 60:
    print("NICE")
else:
    print("SAD")

# Lagay pa more details after elif
grade = 59
favorite = True
if grade >= 92:
    print("YAHOO")
elif grade >= 60:
    print("NICE")
elif grade < 60 and favorite:
    print("PASANG-AWA")
else:
    print("SAD")

# LOOPS: AND BREAK CONTINUE AND PASS
# If inuna yung print(number), ipi-print niya pa rin lahat so dapat after the break/continue command

# Stops at 4 since ayaw na niya by 5
for number in range(10):
    if number == 5:
        break
    print(number)

# Skips 5 then continues the loop
for number in range(10):
    if number == 5:
        continue
    print(number)

# 5 lang ang ipi-print
for number in range(10):
    if number == 5:
        print(number)
        continue
for number in range(10):
    if number == 5:
        pass 
        print(number)

rec = 0
while rec <= 5000:
    rec = int(input("Enter REC: "))
    kulang = 5000 - rec
    if rec >= 4500:
        print("This is enough already.")
        break
    print("You need", kulang)

print("REC is satisfied!")
print("*** END ***")

# Hindi na gagawin yung A little bit more!
rec = 0
while rec <= 5000:
    rec = int(input("Enter REC: "))
    kulang = 5000 - rec
    if rec >= 4500:
        continue
        print("A little bit more!")
    print("You need", kulang)

print("REC is satisfied!")
print("*** END ***")

# Para masabi niya pa rin, use pass
rec = 0
while rec <= 5000:
    rec = int(input("Enter REC: "))
    kulang = 5000 - rec
    if rec >= 4500:
        pass
        print("A little bit more!")
    print("You need", kulang)

print("REC is satisfied!")
print("*** END ***")