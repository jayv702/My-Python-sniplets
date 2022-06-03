####BASIC CONCEPTS
# just print words
print ('Hello world')
print('Hello other world.')
print('Goodbye world')

# calculate how many seconds in a month
print(((60*60)*24)*30)

#hello world text is a STRING
#whole numbers are INTEGERS
#numbers with decimal points are FLOATS

#the following all produce floats
print (3*3.0)
print(45/9)
print(8+3.23)

#the following will not produce float. guess why?
print(1+2+3+4+5)

#two stars ** will make it possible to raise to a power i.e. exponential
print(8**(1/3))
print(9**3)

#Floor division uses two foward slashes // to determine the quotient of a division.
print('FLOOR DIVISION')
print('will produce 3 because 6 goes into 20 three times.')
print(20//6)
print('10//4='); print(10//4 )

#REMAINDER
#% sign will produce the remainder only
print('REMAINDER')
print(1.25%0.5)
print(20%6)
print(7%(5//2))

#flight time from a plane going la to sydney
#distance is 7425 miles and the plane flies an average of 550 miles
print(7425/550)

####STRINGS LESSONS
#if you want to use a quote you need to add a back slash to it.
#if no backslash is added, it will break the snek!
print('James\' likes to skate, but in fact he can\'t. He\'s very average!')

#NEWLINES or how to create newlines without using the same line. Lulz
#\n to create a new line. \t to tab it out.
print('hello world \nToday we will dance. \nTommorow we will take it over')
print('hello \tworld')
# three """ can also make multiline text much easier
print("""what
the
heck
is up""")

#CONCATENATION
#just adds strings and numbers together like "closeTOGETHER"
print("spam" + 'eggs')
print("2" + "2")
print("python" + "rocks")

print("spam" *3)
print(4*'2')

####VARIABLES lessons how bou dat?
#assigned user to the name James. Das me!
#you can use letters numbers and underscores, but no special symbols or starting with number.
user = "James"
print(user + " is an okay guy")
print(user*4)
x=9
print(x)
print(x+3)
print(x)
#variables can be assigned multiple times, but is not good practice.
user="Stefonek"
print(user)

#INPUT function
#Had to make another file for this one because IDK how this works in atom,
#check file inputs sololearn files
#it for user inputting and spitting out the input back at the user
#x = input()
#print(x)

#IN-PlACE OPERATORS
#lets you write code, but shorter
#instead of 'x = x+3' it is now 'x += 3'
#the following code will make x a 2 then print it, it will then
#make x add 3 then print the result
x=2
print(x)
x+=3
print(x)
#Can also be used with strings, as show in the next four lines
x="spam"
print(x)
x+="eggs"
print(x)

#exampe output (remember float is the decimal version)
spam="7"
spam=spam+"0"
eggs=int(spam)+3
print(float(eggs))

#example output (remember that int is for whole numbers(no decimals))
#(string is str which means y is now a str plus the "2" in quotation marks )
x=5
y=x+3
y=int(str(y)+"2")
print(y)

####BOOLEANS & COMPARISONS
#Booleans can have two values, True and False
#They are for comparing values, for instance the equal operator like ==
#remeber case sensitive so True and False
myfirstboolean=True
print(myfirstboolean)
print(34==69)
print("waffle" == "waffle")
print("other examples of above")
#just like mathematics the booleans are used to compare values and whether they
#are greater than, equal to, less than, and mathematics
x=7
# the != means does not equal
print(x!=8) #this will be True
print(8!=8) #this will be False
#greater than >
print(x>5) #True
print("annie">"andy") #this works through lexicographically
                      #due to the alphabetical order of the words it will compare
                      #annie and andy the first is a and a which are both lowercase
                      #and equal to each other in the alphabet, n is the second letter which is also equal
                      #n and d are both different but since n is higher in the alphabet it is greater than d
                      #so annie is greater than andy, which makes this statement True
                      #this can also be used with other types of booleans to compare words
#less than <
print(x<2)
#greater or equal to >=
print(x>=7)
#less or equal to <=
print(x<=7)

#IF STATEMENTS
d=int(input("pick a number:"))
if d>5:
    print("this d is greater than 5")
    if d<=47:
        print("the d is above 5 but below 47")
        if d>47:
            print("way too high bro")
        else:
            if d<5:
                print("way too low bro")
input("another number:")
