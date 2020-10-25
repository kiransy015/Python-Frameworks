import re

str = "The rain in Spain 005 11:35 PM"
# MetaCharacters
# []
# x = re.findall("[abc]",str)
# print(x)

# .
# x = re.findall("Sp..n",str)
# print(x)

# +
# x = re.findall("Sp.+n",str)
# print(x)

# *
# x = re.findall("Sp.*n",str)
# print(x)

# ^
# x = re.findall("^The",str)
# print(x)

# $
# x = re.findall("Spain$",str)
# print(x)


# {}
# x = re.findall("Spa{1}in",str)
# print(x)


# |
# x = re.findall("rains|Spain",str)
# print(x)



# Metacharacters
# \A
# x = re.findall("\AThe",str)
# print(x)

# \Z
# x = re.findall("Spain\Z",str)
# print(x)


# \b
# x = re.findall(r"\bain",str)
# print("Begining of the word :",x)
# x = re.findall(r"ain\b",str)
# print("End of the word :",x)

# \B
# x = re.findall(r"\Bain",str)
# print(x)
# x = re.findall(r"ain\B",str)
# print(x)

# \d
# x = re.findall("\d",str)
# print(x)

# \D
# x = re.findall("\D",str)
# print(x)


# \s
# x = re.findall("\s",str)
# print(x)


# \S
# x = re.findall("\S",str)
# print(x)


# \w
# x = re.findall("\w",str)
# print(x)

# \W
# x = re.findall("\W",str)
# print(x)


# Sets
# [abc]
# x = re.findall("[abc]",str)
# print(x)


# [a-z]
# x = re.findall("[a-z]",str)
# print(x)

# [012]
# x = re.findall("[012]",str)
# print(x)

# [0-9]
# x = re.findall("[0-9]",str)
# print(x)

# [0-5][0-9]
# x = re.findall("[0-5][0-9]",str)
# print(x)

# [a-zA-Z]
# x = re.findall("[a-zA-Z]",str)
# print(x)

# [^abc]
# x = re.findall("[^abc]",str)
# print(x)
















