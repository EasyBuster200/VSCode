x=50
if x < 2 :
    print ("small")
elif x < 10:
    print ("medium")
else:
    print ("large")
#try/expect structure
#You surround a dangerous section of code with try and except
#if the code in the try works- the except is skipped 
#if the code in the try fails: it jumps to the except section 

astr = "Hello Bob"
try:
    istr = int(astr)
except:
    istr = -1
print ("First", istr)
astr = "123"
try:
    istr = int (astr)
except:
    istr = -1
print ("Second", istr)

#Sample try/ except
rawstr = input ("Enter a number: ")
try: 
    ival = int(rawstr)
except:
    ival = -1
if ival > 0 :
    print ("Nice work")
if ival < 0 :
    print ("Not A number")

#Functions
#Stored (and reused) steps 
def thing() :
     print("Hello")
     print("Fun")
 #Output should = (Hello Fun Zip Hello Fun)
thing()
print ("Zip")
thing()

#Python Functions:
#There are two kinds of functions in Python: 
#   Built-in functions thata are provided as part of Python: print(), input(), type(), float(), int() ...
#   Functions that we define ourselves and then use.
#We treat the built-in function names as "new" reserved words (i.e., we avoid them as variable names)

#Function Defenition:
#In python a function is some reusable code that takes argument(s) as input, does some computation,  and then returns a result or results. 
#We define a function using the def reserved word.
#We call/invoke the function by using the function name, parentheses, and arguments in an expression. 

#Functions of our own 
#Building our own Functions:
#We create a new fuction using the def keyword followed by optional parameters or parentheses.
#We indent the body of the function 
#This defines the function but does not execute the body of the function
def print_lyrics():
    print ("I'm a lumberjack, and I'm okay.")
    print ("i sleep all night and I work all day.")

x = 5
print ("Hello")

def print_lyrics():
    print ("I'm a lumberjack, and I'm okay.")
    print ("i sleep all night and I work all day.")

print ("Yo")
x = x + 2 
print (x) 
#In here the function print_lyrics is not called/invoked.


#Definitions and uses 
#Once we have defined a function, we can call (or invoke) it as many times as we like 
#This is the sotre and reuse pattern

x = 5
print ("Hello")

def print_lyrics():
    print ("I'm a lumberjack, and I'm okay.")
    print ("i sleep all night and I work all day.")

print ("Yo")
print_lyrics()
x = x + 2 
print (x) 
#here the function print_lyrics is called/invoked

#Arguments 
#An argument is a value we pass into the function as its input when we call the function 
#We use arguments so we can direct the function to do different kinds of work when we call it at different times 
#We put arguments in parenthese after the name of the function

big = max("Hello World") #"Hello World" in this line is the argument of the fuction max 

#Parameters
#A parameter is a variable which we use in the function definition. It is a "handle" that allows the code in the function to access the arguments for a particular function invocation 

def greet (lang):
    if lang =="es":
        print ("Hola")
    elif lang == "fr":
        print ("Bonjour")
    else:
        print ("Hello")
#In the above section of code lang is a parameter 

#Return Values 
#Often a function will take its argument, do some computation, and reeturn a value to be used as the value of the function call in the calling expression. The return keyword is used for this.

def greet (lang):
    if lang =="es":
        return "Hola"
    elif lang == "fr":
        return "Bonjour"
    else:
        return "Hello"
print (greet("en"),"Glenn")

#Loops and Iteration 
n = 5
while n > 0:
    print (n)
    n = n - 1
print ("Blastoff")
print (n)

#Result: 5,4,3,2,1,Blastoff,0.

#Infinite Loop 
n = 5
while n > 0 :
    print ("Lather")
    print ("Rinse")
print ("Dry off")

#Breaking out of a loop
#The break statement ends the current loop and jumps to the statement immediately following the loop
# It is like a loop test that can happen anywhere in the body of the loop.

while True:
    line = input("> ")
    if line == "done":
        break
    print (line)
print ("Done!") 

#Finishing an iteration with continue
#The continue statement ends the current iteration and jumps to the top of the loop and starts the next iteration

while True:
    line = input ("> ")
    if line[0] == "£" :
        continue
    if line == 'done' :
        break
    print (line)
print ("Done!!")

#indefinite loops 
#While loops are called "indefinite loops" because they keep going until a logical condition becomes False
#The loops we have seen so far are pretty easy to examine to see if they will terminatae or if they will be "infinite loops"
#Sometimes it is a little harder to be sure if a loop will terminate 

#Definite Loop 
# Quite often we have a list of items of the lines in a file- effectively a finite set of things
# We can write a loop to run the once for each of the items in a set using the Python for construct.
# These loops are called definite loops because they execute an exact number of items.
# We say that definite loops iterate through the members of a set. 

for i in [5, 4, 3, 2, 1] :
    print (i)
print ("Blastoff!")

friends = ["joseph", "Glenn", "Sally"]
for friend in friends :
    print ("Happy New Year:", friend)
print ("Done")

#Definite loops (for loops) have explicit iteration variables that change each time through a loop. These iteration variables move through the sequence or set. 

# the iteration variable "iterates" through the sequence (ordered set).
#The block (body) of code is executed once for each calue in the sequence. 
#The iteration variable moves through all of the values in the sequence. 

#Loop Idioms: What we do in loops 
#Making "smart" loops
#The trick is "knowing" something about the whole loop when you are stuck writing code that only sees one entry at a time. 

print ("Before")
for thing in [9, 41, 12, 3, 74, 15] :
    print (thing)
print ("After")

#What is the largest number?
# 3 41 12 9 74 15 
#Answer: 74

largest_so_far = -1
print ("Before", largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15] :
    if the_num > largest_so_far :
        largest_so_far = the_num
    print (largest_so_far, the_num)
print ("After", largest_so_far)

#We make a variable that contains the largest value we have seen so far. If the current number we are looking at is larger, it is the new largest value we have so far. 

#Counting in a Loop 
zork = 0
print ("Before", zork)
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + 1
    print (zork, thing)
print("After, zork")

#To count how many times we executed a loop, we intruduce a counter variable that starts at 0 and we add one to it each time through the loop.
#Summing in a loop 
zork = 0
print ("Before", zork)
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + thing
    print (zork, thing)
print("After, zork")

#To add up a value we encounter in a loop, we intruduce a sum variable that starts at 0 and we add the value to the sum each time through the loop. 

count = 0
sum = 0 
print ("Before", count, sum)
for value in [9, 41, 12, 3, 74, 15] : 
    count = count + 1
    sum = sum + value
    print (count, sum, value )
print ("After", count, sum, sum / count)

# An average just combines the counting and sum patterns and divides when the loop is done. 
#Filtering in a loop 

print ("Before")
for value in [9, 41, 12, 3, 74, 15] :
    if value < 20:
        print ("Large number",value)
print ("After")

#Search using a boolean variable. (true or false)

found = False 
print ("before", found)
for value in [9, 41, 12, 3, 74, 15] :
    if value == 3: 
        found = True
    print (found, value)
print ("After", found)

#If we just want to search and know if a value was found, we  use a variable that starts at False and is set to True as sson as we find what we are looking for. 

largest_so_far = -1 
print ("Before", largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15] :
    if  the_num > largest_so_far :
        largest_so_far = the_num
    print (largest_so_far, the_num)
print ("After", largest_so_far)

#How would we change this to make it find the smallest value in the list?
smallest_so_far = -1
print ("Before", smallest_so_far)
for the_num in [9, 41, 12, 3, 74, 15] :
    if the_num < smallest_so_far:
        smallest_so_far = the_num
    print (smallest_so_far, the_num)
print ("After", smallest_so_far)

#We switched the variable name to smallest_so_far and switch the > to <.
#However this is not enough
#This will give us -1 as the smallest number, so we must replace -1 by a number that is bigger than all of the other numbers

smallest_so_far = 100
print ("Before", smallest_so_far)
for the_num in [9, 41, 12, 3, 74, 15] :
    if the_num < smallest_so_far:
        smallest_so_far = the_num
    print (smallest_so_far, the_num)
print ("After", smallest_so_far)

#However this only works if we know the biggest possible value.
#What about if we don't? 

smallest = None 
print ("Before")
for value in [9, 41, 12, 3, 74, 15] :
    if smallest is None :
        smallest = value 
    elif value < smallest :
        smallest = value
    print (smallest, value)
print ("After", smallest)

#We still have a variable that is the smallest so far. The first time though the loop smallest is None, so we take the first value to be the smallest. 

#The "is" and "is not" operators 

smallest = None 
print ("Before")
for value in [9, 41, 12, 3, 74, 15] :
    if smallest is None :
        smallest = value 
    elif value < smallest :
        smallest = value
    print (smallest, value)
print ("After", smallest)

 #Python has an is operator that can be used in logical expressions.
 #Implies "is the same as"
#Similar to, but stronger than ==.
#Is not also is a logical operator. 

#Strings:
#A string is a sequence of characters 
#A string literal uses quotes "Hello" or 'Hello'
#For strings, + means "concatenate" (link things tohether)
#When a string contains numbers, it is still a string.
#We can convert numbers in a string into a number using int()

#Reading and Converting
#We prefer to read data in using strings and then parse and convert the data as we nned
#This gives us more control over error situations and/or bad user input.
#Raw input munebers must be converted from strings. 

#Looking inside strings
#We can get any single character in a string using an index specified in square brackets 
#The index value must be integer and starts at zero
#The index value can be an expression that is computed. 
#b a n a n a
#0 1 2 3 4 5

#Strings have length
#The built-in function len gives us the length of a string.

#Looping through strings
#Using a while statement and an iteration variable, and the len function, we can construct a loop to look at each of the letters in a string individually.

fruit = "banana"
index = 0 
while index < len(fruit) :
    letter = fruit [index]
    print (index, letter)
    index = index + 1

#A definite loop using a for statement is much more elegant
#The iteration variable is completely taken care of by the for loop.
fruit = "banana"
for letter in fruit :
    print (letter)

#Looping and counting 
#This is a simple loop that loops through each letter in a string and counts the number of times the loop ecounters the 'a' character

word = "banana"
count = 0 
for letter in word :
    if letter =="a" :
        count = count + 1 
print (count)

#The iteration variable "iterates" through the sequence (ordered set)
#The block (body) of code is executed once for each value in the sequence
#The iteration variable moves through all of the values in the sequence. 

#Slicing Strings 
#We can also look at any continuos section of a string using a colon operator 
#The second number is once beyond the end of the slice - "up to but not including"
# If the second number is beyond the end of the string it stops at the end.

s = "Monty Python"
print (s[0:4])
print (s[6:7])
print (s[6:20])

#If we leave off the first number or the last number of the slice, it is assumed to be the beginning or the end of the string respectively

s = "Monty Python"
print (s[:2]) #Mo
print (s[8:]) #Thon
print (s[:]) #Monty Python 

#String Concatenation
#When the + operator is applied to strings, it means "concatenation" (the action of linking things together in a series, or the condition of being linked in such a way)

a = "Hello"
b = a + "There"
print (b) #HelloThere

c = a + " " + "There"
print (c) #Hello There

#The + operator does not add the a space between the added strings. 

#Using in as a logical operator
# The in keyword can also be used to check to see if one atring is "in" another string 
#The in expression is  a logical expression that returns True or False and can be used in an if statement. 

fruit = "banana"
"n" in fruit #True 
"m" in fruit #False
"nan" in fruit #True 

if "a" in fruit :
    print ("Found it!") #Found it! 

#String Comparison 
if word == "banana" :
    print ("All right, bananas.")

if word < "banana" :
    print ("Your word", + word + ", comes before banana.")
elif word > "banana" :
    print ("Your word", + word + ", comes after banana.")
else :
    print ("All right, bananas.")

#String library 
#Python has a number of string functions which are in the string library 
#These functions are already built into every dtring - we invoke them by appending the function to the string variable. 
#These functions do not modify the original string, instead they return a new string that has been altered. 

greet = "Hello Bob"
zap = greet.lower()
print (zap) #hello bob
print (greet) #Hello Bob
print ("Hi There".lower()) #hi there

#There are many more X.something function built into python 

#Searching a String 
#We use the find() function to serach for a substring within another string 
#find() finds the first occurence of the substring 
#if the substring is not found, find() returns -1 
#Remember that string position starts at zero. 

fruit ="banana"
pos = fruit.find("na")
print (pos) #2 (postion of the first na in banana)

aa = fruit.find("z")
print (aa) #-1 (because there is no z)

#Making everything UPPER CASE 
#You can make a copy of a string in lower case or upper case.
#Often when we are searching for a string using find() we first convert the string to lower case so we can search a string regardless of case. 

greet ="Hello Bob"
nnn = greet.upper()
print (nnn) #HELLO BOB 

www = greet.lower()
print (www) #hello bob 

#Search and replace 
#The search() function is like a "search and replace" operation in a word processor 
#It replaces all occurrences of the search string with the replacement string. 

greet = "Hello Bob"
nstr = greet.replace ("Bob", "Jane")
print (nstr) #Hello Jane 
nstr = greet.replace ("o", "X")
print (nstr) #HellX BXb

#Stripping whitespace 
#Sometimes we want to take a string and remove whitespace at the begining and/or end. 
#Istrip() and rstrip() remove whitespace at he left and right.
# strip() removes both the begining and ending whitespace.

greet = "     Hello Bob    " 
greet.lstrip() #"Hello Bob    "
greet.rstrip() #"     Hello Bob"
greet.strip() #"Hello Bob"

#Prefixes
line = "Please have a nice day"
line.startswith ("Please") #True
line.startswith ("p") #False

data = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
atpos = data.find("@") #21
sppos = data.find (" ", atpos) #31
host = data [atpos + 1 : sppos]
print (host) #uct.ac.za

#Reading Files 

#File processing
#A text file can be thought of as a sequence of lines.
# Opening a file 
# Before we can read the contents of the file, we must tell python which file we are going to work with and what we will be doing with the file. 
# This is done with the open() function
# Open() returns a "file handle" - a variable used to perform operations on the file.
# Similar to "File -> Open" in a word processor 

#Using open()
#handle = open (filename, mode)
#returns a handle use to manipulate the file 
#filename is a string
#mode is optional and should be "r" if we are planning to read the file and "w" if we are going to write to the file. 

#What is a handle 
fhand = open("mbox.txt")
print (fhand) 

#The new line character
#We use a special character called the "newline" to indicate when a line ends 
#We represent it as \n in strings 
#Newline is still one character - not two 

#File Handle as a sequence
#A file handle open for read can be treated as a sequence of strings where each line in the file is a string in the sequence 
#We can use the for statement to iterate through a sequence 
#Remember -  a sequence is an ordered set.

xfile = open ("mbox.txt")
for cheese in xfile :
    print (cheese)

#Counting lines in a file 
#open a file read-only 
#Use a for loop to read each line 
#Count the lines and print out the number of lines 

fhand = open ("mbox.txt")
count = 0
for line in fhand:
    count = count + 1
print ("Line Count:", count)

#Reading the *whole* File 
#We can read the whole file (newlines and all) into a single string

fhand = open ("mbox-short.txt")
inp = fhand.read()
print (len(inp)) # 94626
print (inp[:20]) #From stephen.marquar

#Searching through a file 
#We can put an if statement in our for loop to only print lines that meet some criteria. 

fhand = open("mbox-short.txt")
for line in fhand:
    if line.startswith("From:") :
        print (line)

#This will give a result where all the emails are separated by an empty line since the file contains a newline and the print function adds one on top.
#To solve this we use the following code:

fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if line.startswith("From:") :
        print (line)

#The line.rstrip() in the code clers any white space that is in the line variable, so now we only have one new line from the print function. 
#Skipping and continue
#We can conventionally skip a line by using the continue statement.

fhand = open ("mbox-short.txt")
for line in fhand :
    line = line.rstrip()
    if not line.startswith ("From: ") :
        continue
    print (line)

#This code does the same thing as before but it skips any lines that don't start with "From: ", making the proscess a little bit faster. 
#Using in to select lines. 
# We can look for string anywhere in a line as our selection criteria

fhand =open ("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if not "@uct.ac.za"  in line :
        continue
    print (line) 

#Prompt for file name

fname = input ("Enter the file name: ")
fhand = open(fname) 
count = 0 
for line in fhand :
    if line.startswith("Subject: ") :
        count = count + 1
print ("There were", count, "subject lines in", fname)

#Bad File names 

fname = input ("Enter the file name: ")
try :
    fhand = open (fname)
except:
    print ("File cannot be opened:", fname)
    quit()

count = 0
for line in fhand:
    if line.startswith("Subject: ") :
        count = count + 1
print ("There were", count, "subject lines in", fname)

#What is not a "Collection"
#Most of our variables have one value in them - when we put a new value in the variable, the old value is overwritten. 
#A list is a kind of Collection
#A collection allows us to put many values in a single "variable"
#A collection is nice because we can carry all many values around in one covinient package.

friends = ["Joseph", "Glenn", "Sally"]
carryon = ["Socks", "Short", "perfume"]

#List constants 
#List constants are surrounded by square brackets and the elements in the list are separated by commas.
#A list element can be any Python object - even other list 
#A list can be empty 
#A list can contain different types of variables 

#Lists and definite loops - best pals

friends = ["Joseph", "Glenn", "Sally" ]
for friend in friends :
    print ("Happy New Year", friend)
print ("Done!")

#Looking inside lists
#Just like strings, we can get at any single element in a list using an index specified in square brackets.
friends = ["Joseph", "Glenn", "Sally"] 
print (friends [1]) 
#Glenn

#List are Mutable (aka changeble)
#String are "immutable" - we cannot change the contents of a sstring - we must make a new string to make any change
#Lists are "mutable" - we can change an element of a list using the index operator 

#How long is a list
#The len() function takes a list as a parameter and returns the number of elements in the list 
#Actually len() tells us the number of elements of any set or sequence (such as a string...)

x = [ 1, 2 , "joe", 99]
print ( len(x) )
#4

#Using the range function
#The range function returns a list of numbers that range from zero to one less than the parameter
#We can construct an index loop using for and an integer iterator 

print (range(4))
#[0, 1, 2, 3]

friends = ["Joseph", "Glenn", "Sally"] 
print (len(friends))
#3

print (range (len(friends)))
#[0, 1, 2]

#A tale of two loops...

friends = ["Joseph", "Glenn", "Sally"] 

for friend in friends :
    print ("Happy New Year:", friend)

for i in range(len(friends)) :
    friend = friends[i]
    print ("Happy New Year:", friend)

#In the example both for loops give the same results 

#Concatenating (linking) lists using + 
#We can create a new list by adding two existing lists together 

a = [1, 2, 3]
b = [4, 4, 6]
c = a + b
print (c)
#[1, 2, 3, 4, 5, 6]

#Lists can be sliced using:
#t = [9, 41, 12, 3, 74, 15]
#[1:3]
#[41, 12]
#Remenber : just like in strings, the second number is "up to but not including"

#List methods 
x = list()
type (x)
#<type "list">
dir (x)
#Says all the things you can do to the list x

#Building list from scratch
#We can create an empty list and then add elements using the append method 
#The list stays in order and new elements are added at the end of the list 

stuff = list()
stuff.append("book")
stuff.append(99)
print (stuff)
#["book", "99"]

stuff.append ("cookkie")
print (stuff)
#["book", 99, "cookie"]

#Is something in a lis?
#Python provides two operators that let you check if an item is in a list
#These are logical operators that return True or False 
#They do not modify the list

some = [1, 9, 21, 10, 16]
9 in some
#True 

15 in some
#False

20 not in some 
#True 

#Lists are in order
#A list can hold many items and keeps those items in the order until we do something to change the order 
#A list can be sorted (i.e., change its order)
#The sort method (unlike in strings) means "sort yourself"

friends = ["Joseph", "Glenn", "Sally"] 
friends.sort()
print (friends)
#["Glenn", "Joseph", "Sally"]

print (friends [1])
#Joseph 

#Built-in functions and lists
#There are a number of functions built into Python that take lists as parameters

nums = [ 3, 41, 12, 9, 74, 15]

#The len function gives us the number of itmes in the list Ex: 6
#the max function looks for the highest value in the list Ex: 74
#The min function looks for the smalles t value of the list Ex: 3
#The sum function adds all the values of the list Ex: 154

total = 0
count = 0
while True:
    inp = input ("Enter a number: ")
    if inp == "done" : break
    value = float(inp)
    total = total + value 
    count = count + 1

average = total / count
print ("Averege: ", average)

#This will ask for a number until we input done, then it will calculate the average of the numbers inputed 

numlist = list()
while True :
    inp = input ("Enter a number: ")
    if inp == "done" : break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print ("Average: ", average)

#his code block creates an empty list to which the inputed values are added, so that it is easier to calculate the average
#The second code block uses more memory than the first one, however this is not really significant.

#Best friends: Strings and lists
abc = "With three words"
stuff = abc.split()
print (stuff)
#["With","three", "words"]
print (len(stuff))
#3
print (stuff[0])
#With

#Split breaks a string into parts and produces a list of strings. We think of these as words. We can access a particular word or loop through all the words.

print (stuff)
#["with", "three", "words"]
for w in stuff :
    print (w)
#with
#three
#words

#When you do not specify a delimiter, multiple spaces are treated like one delimeter
#You can specify what delimiter character to use in the splitting.
#The split function looks for spaces to know where to split, but this can be changed with the delimiter 

line = "A lot             of spaces"
etc = line.split()
print(etc)
#["A", "lot", "of", "spaces"]

line = "first;second;third"
thing = line.split()
print (thing)
#["first;second;third"]
print (len(thing))
#1
thing = line.split(";")
print (thing)
#["first", "second", "third"]
print (len(thing))
#3

#but with delimiters the split function does not "erase" multiple delimiters followed, so it considers the spaces between them as characters for the list.

#from stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if not line.startswith ("From ") : continue
    words = line.split()
    print (words[2])

#This opens the file runs through the lines looking for ones starting with "From", then it split the line in the empty spaces, and since we know that the 2 position includes the day of the week, we can print the thing on the list with position 2

#The double split pattern 
# Sometimes we split a line one way, and then grab one of the pieces of the line and split that piece again 

#from stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

words = line.split()
email = words [1] 
print (email) 
#stephen.marquard@uct.ac.za
pieces = email.split ("@")
print (pieces)
#["stephen.marquard", "uct.ac.za"]
print (pieces[1])
#uct.ac.za

#Python dictionaries 
#What is a clllectio?
#A collection is nice because we can put more than one value in it and carry them all around in one convenient package
#We have a bunch of values in a single "variable"
# We do this by having more than one place "in" the variable 
#We have ways of finding the different places in the variable 

#Waht is not a "Collection"?
#Most of our variables have one value in them - when we put a new value in the variable - the old value is overwritten

#A story of two collections...
#List : a linear collection of values that stay in order
#dictionary: a "bag" of values, each with its own label

#Disctionaries are Pythons most powerful data collection
#Dictionaries allow us to do fast database-like operations in Pyhton

#Lists index their entries based on hte position in the list
#Dictionaries are like bags - no order 
#So we index the things we put in the dictionary with a "lookup tag"

purse = dict()
purse ["money"] = 12
purse ["candy"] = 3
purse ["tissues"] = 75
print (purse)
#{'money': 12, 'candy': 3, 'tissues': 75}
print (purse ["candy"])
#3
purse ["candy"] = purse ["candy"] + 2 
print (purse)
#{'money': 12, 'candy': 5, 'tissues': 75}

#Comparing Lists and dictionaries
#Dictionaries are like lists except that they use keys instead of numbers to look up values 

lst = list()
lst.append(21)
lst.append(183)
print (lst)
#[21, 183]
lst [0] = 23
print (lst)
#[23, 183]

ddd = dict()
ddd ["age"] = 21
ddd ["course"] = 182
print (ddd)
#{'age': 21, 'course': 182}
ddd["age"] = 23
print (ddd)
#{'age': 23, 'course': 182} 

#Lists and dictionaries are basically the same, the main difference is the index. 
#In lists things are indexed by numbers from 0 up.
#In dictionaries things are index by the progammer.

#Dictionary Literals (Constants)
#Dictionary literals use curly braces and have a lis of key : value pairs 
#You can make an empty dictionary using empty curly braces or with dict()

jjj = {"chuck" : 1, "fred" : 42, "jan" : 100}
print (jjj)
#{'chuck': 1, 'fred': 42, 'jan': 100

ooo = { }
print (ooo)
#{}

#Many counters with a Dictionary
#One common use of dictionaries is counting how often we "see" something 

ccc = dict ()
ccc ["csev"] = 1
ccc ["cwen"] = 1
print (ccc)
#{'csev': 1, 'cwen': 1}

ccc["cwen"] = ccc["cwen"] + 1
print (ccc)
#{'csev': 1, 'cwen': 2}

#When we see a new name 
#When we encounter a new name, we need to add a new entry in the dictionary and if this second or later time we have the name, we simply add one to the count in the dictionary under that name 

counts = dict()
names = ["csev", "cwen", "csev", "zqian", "cwen"]
for name in names : 
    if name not in counts:
        counts [name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)

#The get method for dictionaries
#he pattern of checking to see if a key is already in a dictionary and assuming a default values if the key is not there is so common that there is a method caleed get() that does this for us 

if name in counts:
    x = counts [name]
else :
    x = 0 

#The four lines above can be replaced by the following line while still getting the same result

x= counts.get(name, 0)

#This line gets the key and if it is in the dictionary it adds one to the count if not it creates a new key with the pre-set default value in this case 0

#The following loop can be made samller with the get() function.
counts = dict()
names = ["csev", "cwen", "csev", "zqian", "cwen"]
for name in names : 
    if name not in counts:
        counts [name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)

#By replacing hte four lines of the line with a get() line
counts = dict()
names = ["csev", "cwen", "csev", "zqian", "cwen"]
for name in names : 
    counts[name] = counts.get(name, 0) + 1
print(counts)

#Both codes give the exact same result

#Counting words in Text 

counts = dict()
print ("Enter a line of text: ")
line = input (" ")
words = line.split()
print ("Words:", words)
print ("Counting...")
for word in words:
    counts[word] = counts.get (word, 0) + 1 
    print("Counts", counts)

#The general pattern to count the words in a line of text is to split the line into words, then loop through the words and use a dictionary to track the count of each word independently.

#Definite loops and dictionaries 
#Even thoughdictionaries are not stored in order, we can write a for loop that goes through all the entries in a dictionary - actually it goes through all the entries in a dictionary and looks up the values

counts = {"chuck" : 1, "fred" : 42, "jan" :100}
for key in counts:
    print(key, counts[key])

#Retrieving lists of keys and values 
#You can get a lis of keys, values, or items(both) from a dictionary

jjj = {"chuck" : 1, "fred" : 42, "jan" :100}
print (list(jjj))
#['chuck', 'fred', 'jan']
print (jjj.keys())
#dict_keys(['chuck', 'fred', 'jan'])
print (jjj.values())
#dict_values([1, 42, 100])
print (jjj.items())
#dict_items([('chuck', 1), ('fred', 42), ('jan', 100)])

#Two iteration Variables 
#We loop through the key-value pairs in a dictionary using two iteration variable
#Each iteration , the first variable is the key and the second variable is the corresponding value for the key 

jjj = {"chuck" : 1, "fred" : 42, "jan" :100}
for aaa,bbb in jjj.items() :
    print(aaa,bbb)
#chuck 1
#fred 42
#jan 100

#Open file, count words and find most common:
name = input ("Enter file: ")
handle = open (name)

counts = dict()
for line in handle :
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word,count in counts.items() :
    if bigcount is None or count > bigcount :
        bigword = word
        bigcount = count

print (bigword, bigcount)

#Tuples are like lists
#tuples are another kind of sequence that functions much like a list- they have elements which are indexed starting at 0

x = ("Gleen", "Sally", "Joseph")
print (x[2])
#Joseph

y = (1, 9, 2)
print (y)
#(1, 9, 2)

print (max(y))
#9

#However, tuples are "immutable"
#Unlike a list, once you create a tuple, you cannot alter its contents - similar to a string

x = [9, 8, 7]
x[2] = 6
print (x)
#[9, 8, 6]

y = "ABC" 
y[2] = "D"
#Traceback (error)

#Tuples are more efficient 
#Since python does not have to build tuple structures to be modifiable, they are simpler and more efficient in terms of memore use and performance than lists.
#So in our program when we are making "temporary variable" we prefer to use tuples over lists 

#Tuples and assignment
#We can put a tuple on the left-hand side of an assignmetn statement
#We can even omit parentheses

(x, y) = (4, "Fred")
print (y)
#Fred

(a, b) = (99, 98)
print (a) 
#99

#Tuples and dictionaries 
#The items() method in dictionaries returns a list of (key, value) tuples 

d = dict()
d["csev"] = 2
d["cwen"] = 4
for (k,v) in d.items() :
    print (k,v)
#csev 2
#cwen 4

tups = d.items()
print (tups)
#dict_items ([("csev, 2"), ("cwen", 4)])

#Tuples are comparable 
#The comparison operators work with tuples and other sequences. If the first item is equal, python goes on to the next element, and so on, until it finds elemnts that differ.

#Sorting lists of tuples 
#We can take advantage of the ability to sort a list of tuples to get a sorted version of a dictionary 
#First we sort the dictionary by the key using the items() method and sorted() fucntion

d = {"a": 10, "b":1, "c":22}
d.items()
#dict_items([('a', 10), ('b', 1), ('c', 22)])
sorted(d.items())
# [('a', 10), ('b', 1), ('c', 22)]

#Using sorted()
#we can do this even more directly using the built-in function sorted that takes a sequence as a parameter and returns a sorted sequence

d = {"a": 10, "b":1, "c":22}
t = sorted(d.items())
for k, v in sorted(d.items()): 
    print (k,v)
#a 10
#b 1
#c 22

#Sorting by values instead of key
#If we could construct a list of tuples of the form (value,key) we could sort by value
#We do this with a for loop that creates a list of tuples 

c = {"a": 10, "b":1, "c":22}
tmp = list()
for k, v in c.items() : 
    tmp.append( (v, k))
print (tmp)
#[(10, 'a'), (1, 'b'), (22, 'c')]

tmp = sorted (tmp, reverse = True)
print (tmp)
#[(22, 'c'), (10, 'a'), (1, 'b')]

#Counting words and finding the 10 most common ones:

fhand = open ("Writing.txt")
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts [word] = counts.get(word, 0) + 1

lst = list()
for key, val in counts.items() :
    newtup = (val, key)
    lst.append (newtup)

lst = sorted(lst, reverse=True) 

for val, key in lst [:10] : 
    print (key, val)
  
#to 15
#the 5
#our 5
#of 5
#do 5
#computers 5
#and 5
#you 4
#that 4
#can 4

#Even shorter version
c = {"a": 10, "b":1, "c":22}
print ( sorted( [(v,k) for k,v in c.items()]))
#[(1, 'b'), (10, 'a'), (22, 'c')]

#Regular expressions
#In computing, a regular expression, also reffered to as "regex" or "regexp", provides a concise and flexible means for matching strings of text, such as particular characters, words, or patterns of characters. A regular expression is written in a formal language that can be interpreted by a regular expression processor.

#Undesrtanding regular expressions
#Very powerful and quite cryptic
#fun once you understand them
#regular expressions are a language unto themselves
#a language of "marker characters" - programming with characters
#It is kind of an "old school" language - compact
