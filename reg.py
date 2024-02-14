# A RegEx, or Regular Expression, is a sequence of characters
#  that forms a search pattern.

# RegEx can be used to check if a string contains the
#  specified search pattern.


# Python has a built-in package called re,
#  which can be used to work with Regular Expressions.

# Import the re module:

import re

# # The findall() function returns a list 
# containing 
# all matches.

# txt = "The rain in Spain"
# x = re.findall("Sp", txt)
# print(x)

#--------------------------
# The search() function searches the string 
# for a match, 
# and returns a Match object if there is a match.

# If there is more than one match, only
#  the first occurrence
#  of the match will be returned:


# txt = "The rain in Spain"
# x = re.search("rr", txt)
# print(x)
# print('''The first space character 
# is located in position:''', x.start())


#-------------
# # []	A set of characters	"[a-m]"
# txt = "T1hme raIn in Sp4ain"
# #Find all lower case characters 
# # alphabetically between "a" and "m":
# x = re.findall("[1-9]", txt)
# print(x)

#---------------------
#Replace all white-space characters with 
# # the digit "9":

# txt = "The rain in Spain"
# x = re.sub("/s", "9", txt,2)
# print(x)

#------------------------------

# # Replace the first 2 occurrences:

# txt = "The rain in Spain"
# x = re.sub("\s", "9", txt, 2)
# print(x)

#-----------------------

# 7ww

#---------------------
# txt = "Th5e ra20in in1 Spain"

# # #Check if the string has any 0, 1, 2, or 3 digits:

# x = re.findall("[ain1450]", txt)

# print(x)

#----------------------------

# # ^	Starts with
# txt = " in1 Spain rain"
# x = re.findall("^rain", txt)
# print(x)
# if x:
#   print("Yes, the string starts with 'hello'")
# else:
#   print("No match")

#-----------------
# txt = "Th#e rain in Sp9ain"
# #Check if the string has other characters than a, r, or n:
# x = re.findall("[^arn]", txt)
# print(x)


#-----------------------rrrr

# # $	Ends with	"world$
# txt = "hellod worl"
# #Check if the string ends with 'world':
# x = re.findall("d$", txt)
# print(x)
# if x:
#   print("Yes, the string ends with 'world'")
# else:
#   print("No match")

#-----------------------------
# Print the position (start- and end-position) of
#  the first match occurrence.

# The regular expression looks for any words 
# that starts with an upper case "S":

# txt = "he She T*5a_ Tinmm in Spa9in"
# x = re.search(r"\bSp\w+", txt)
# print(x)
# print(x.span())
# print(x.start())
# print(x.string)
# print(x.group())
# # #-----------------------------

# # # #The string property returns the search string:

# # # txt = "The rain in Spain"
# # # x = re.search(r"\bS\w+", txt)
# # print(x.string)

# # #------------------------------


# # # # Print the part of the string where there was a match.

# # # # The regular expression looks for any words
# # #  that starts with an upper case "S"


# # # txt = "The rain in Spain"
# # # x = re.search(r"\bS\w+", txt)
# print(x.group())

#-----------------------------
# # Metacharacters
# #----------------------------

# # {}	Exactly the specified number of
# #  occurrences

# txt = "The raallin in Spaaialln fathells mainaly in the pallain!"

# # # # #Check if the string contains "a" followed
# # # #  by exactly two "l" characters:

# # x = re.findall("al{2}p", txt)
# x = re.findall("in|the", txt)

# print(x)


#----------------------------------
# –––
#-------------------------------------------

# \A	Returns a match if the specified characters 
# are at the beginning of the string	"\AThe"	  ^
	
# \d	Returns a match where the string 
# contains digits (numbers from 0-9)	"\d"
# 	
# \D	Returns a match where the string
#  DOES NOT contain digits	"\D"	

# \s	Returns a match where the string
#  contains a white space character	"\s"
# 	
# \S	Returns a match where the string 
# DOES NOT contain a white space character	"\S"
# 	
# \w	Returns a match where the string 
# contains any word characters (characters from a to Z,
#  digits from 0-9, and the underscore _ character)	"\w"
# 	
# \W	Returns a match where the string
#  DOES NOT contain any word characters	"\W"
# 	
# \Z	Returns a match if the specified 
# characters are at the end of the string  $

txt = "The r4ai_n in The S#pai7n"
# x = re.findall("\W", txt)
x = re.findall("e\Z", txt)

print(x)