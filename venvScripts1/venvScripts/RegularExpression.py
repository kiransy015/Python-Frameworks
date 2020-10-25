import re


txt = "The rain in winter sestrason in Spain"


# search - Returns a Match object if there is a match anywhere in the string
# x = re.search("^The.*Spain$",txt)
# if(x):
#     print('Match found!!!',x)
# else:
#     print('Match not found!!!',x)


# findall - Returns a list containing all matches
# x = re.findall("in",txt)
# if(x):
#     for i in range(0,len(x)):
#         print(i+1," :",x[i])
# else:
#     print("No macthing items found!!!")


# split - Returns a list where the string has been split at each match
# x = re.split("in",txt)
# if(x):
#     for i in range(0,len(x)):
#         print(i+1," :",x[i])
# else:
#     print('No matching text to split')


# sub - Replaces one or many matches with a string
# x = re.sub("The","That",txt)
# print('Original string :',txt)
# print('replaced string :',x)


# A set of characters
#Find all upper case characters alphabetically between "A" and "Z":
# x = re.findall("[A-Z]",txt)
# if(x):
#     for i in range(0,len(x)):
#         print(i+1," :",x[i])
# else:
#     print('No matching charcters found')


# Any character (except newline character)
#Search for a sequence that starts with "ai", followed by one (any) characters:
# x = re.findall("ai.",txt)
# if(x):
#     for i in range(0,len(x)):
#         print(i+1," :",x[i])
# else:
#     print('')


# Starts with
#Check if the string starts with 'The':
# x = re.findall("^The",txt)
# if(x):
#     print('The string is starting with The :',x)
# else:
#     print('The string is not starting with The :')

# Ends with
# Check if the string ends with 'Spain':
# x = re.findall("Spain$",txt)
# if(x):
#     print('The string is ending with Spain :',x)
# else:
#     print('The string is not ending with Spain :')


# Zero or more occurrences
#Check if the string contains "Spain" followed by 0 or more "x" characters:
# x = re.findall("Spain*",txt)
# if(x):
#     for i in range(0,len(x)):
#         print(i+1," :",x[i])
# else:
#     print("No matching found")


# One or more occurrences
#Check if the string contains "Spain" followed by 1 or more "x" characters:
# x = re.findall("Spain+",txt)
# if(x):
#     for i in range(0,len(x)):
#         print(i+1," :",x[i])
# else:
#     print('No matching found')


# Exactly the specified number of occurrences
#Check if the string contains "a" followed by exactly two "l" characters:
# str1 = "The all rain in Spain"
# x = re.findall("al{2}",str1)
# if(x):
#     for i in range(0,len(x)):
#         print(i+1," :",x[i])
# else:
#     print("no match found")


# Either or
#Check if the string contains either "rain" or "falls":
# x = re.findall("rain|falls",txt)
# if(x):
#     print('Yes atleast there is one match',x)
# else:
#     print('None of the string we have a match')


# Returns a match if the specified characters are at the beginning of the string
#Check if the string starts with "The":
# x = re.findall("\AThe",txt)
# if(x):
#     print('The string is starting with :',x)
# else:
#     print('The string is not starting with The')


# Returns a match if the specified characters are at the end of the string
#Check if the string ends with "Spain":
# x = re.findall("Spain\Z",txt)
# if(x):
#     print('Yes string ends with expected value',x)
# else:
#     print('String not ends with expected value')


# Returns a match where the specified characters are at the beginning or at the end of a word
#Check if "The" is present at the beginning of a WORD:
# x = re.findall(r"\bin",txt)
# print(x)

# Check if "in" is present at the end of a WORD:
# x = re.findall(r"in\b",txt)
# print(x)


# Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
#Check if "in" is present, but NOT at the beginning of a word:
# x = re.findall(r"\Bin",txt)
# print(x)

#Check if "in" is present, but NOT at the end of a word:
# x = re.findall(r"in\B",txt)
# print(x)


# Returns a match where the string contains digits (numbers from 0-9)
#Check if the string contains any digits (numbers from 0-9):
# str2 = "The spain code 003"
# x = re.findall("\d",str2)
# if(x):
#     print(x)
#     print('String is having integer value',x)
# else:
#     print(x)
#     print('String is not having any integer value')

# Returns a match where the string DOES NOT contain digits
#Return a match at every no-digit character:
# str2 = "The spain code 003"
# x = re.findall("\D",str2)
# if(x):
#     print(x)
# else:
#     print(x)


# Returns a match where the string contains a white space character
#Return a match at every white-space character:
# x = re.findall("\s",txt)
# print(x)

# Returns a match where the string DOES NOT contain a white space character
#Return a match at every NON white-space character:
# x = re.findall("\S",txt)
# print(x)


# Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
# str2 = "The spain code 003"
# x = re.findall("\w",str2)
# print(x)

# Returns a match where the string DOES NOT contain any word characters
# str2 = "The spain code 003"
# x = re.findall("\W",str2)
# print(x)


# Returns a match where one of the specified characters (a, r, or n) are present
#Check if the string has any a, r, or n characters:
# str2 = "The spain code 003"
# x = re.findall("[arn]",str2)
# print(x)


# Returns a match for any lower case character, alphabetically between a and n
# Check if the string has any characters between a and n:
# str2 = "The spain code 003"
# x = re.findall("[a-n]",str2)
# print(x)


# Returns a match where any of the specified digits (0, 1, 2, or 3) are present
#Check if the string has any 0, 1, 2, or 3 digits:
# str2 = "The spain code 003"
# x = re.findall("[0123]",str2)
# print(x)

# Returns a match for any digit between 0 and 9
# Check if the string has any digits:
# str2 = "The spain code 003"
# x = re.findall("[0-9]",str2)
# print(x)


# Returns a match for any two-digit numbers from 00 and 59
# Check if the string has any two-digit numbers, from 00 to 59:
# str3 = "8 times before 11:45 AM"
# x = re.findall("[0-5][0-9]",str3)
# print(x)


# Returns a match for any character alphabetically between a and z, lower case OR upper case
# Check if the string has any characters from a to z lower case, and A to Z upper case:
# str2 = "The spain code 003"
# x = re.findall("[a-zA-Z]",str2)
# print(x)


# Verify is this a valid mobile no
# mob = "9035579869"
# x = re.match("[0-9]{10}$",mob)
# print(x)
# if x:
#     print("Valid mobile no :",x)
# else:
#     print("Invalid mobile no :")


# .
# +
# *
#
# \d
# \D
#
# \w
# \W
#
# \s
# \S
#
# r"\bin"
# r"in\b"
# r"\Bin"
# r"in\B"
#
# [abc]
# [a-e]
# [a-zA-Z]
# [0123]
# [0-4]
# [0-5][0-5]
# {2} or {1,3}
#  |
#
# ^ , \A
# $ , \Z
#
# search
# findall
# split
# sub





lst = re.match(r".*=$\b","int x =    string y =    abc    boolean z =")
print(lst)


































