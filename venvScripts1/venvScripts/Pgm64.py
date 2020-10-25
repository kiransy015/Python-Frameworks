#Reading data from a text file
# file = open("C:\Kiran Kumar SY\Python\Scripts\DATA.txt")
# print(file)
# data = file.read()
# print(data)

# To fetch/get specific no of characters from a file
# file = open("C:\Kiran Kumar SY\Python\Scripts\DATA.txt")
# print(file)
# data = file.read(10)
# print(data)

# Reading content of First line in a text file
# file = open("C:\Kiran Kumar SY\Python\Scripts\DATA.txt")
# print(file)
# data = file.readline()
# print(data)

# file = open("C:\Kiran Kumar SY\Python\Scripts\DATA.txt")
# print(file)
# data = file.readlines()
# print(data)

# Appending data to a text file
# str = "Japan"
# file = open("C:\Kiran Kumar SY\Python\Scripts\DATA.txt",mode='a')
# file.write("\n")
# file.write(str)
# file.close()


# writing data to Json file
# import json
# info = {"age": 30, "name": "ram"}
# file = open("C:\Kiran Kumar SY\Python\Scripts\DATA.json",mode='w')
# json.dump(info,file)
# file.close()



# Update json file
# import json
# file = open("C:\Kiran Kumar SY\Python\Scripts\DATA.json",mode='r')
# info = json.load(file)
# file.close()
#
# file = open("C:\Kiran Kumar SY\Python\Scripts\DATA.json",mode='w')
# info.update({'dob':'12-12-2019'})
# json.dump(info,file)
# file.close()


# Read data from json file
# import json
# file = open("C:\Kiran Kumar SY\Python\Scripts\DATA.json")
# print(file)
# data = json.load(file)
# print(type(data))
# print(data)


# Write data to json file
# import json
# info = {"name":"Ram","age":33}
# file = open("C:\Kiran Kumar SY\Python\Scripts\DATA.json",mode='w')
# json.dump(info,file)


# Update json file content
import json
file = open("C:\Kiran Kumar SY\Python\Scripts\DATA.json")
print(file)
data = json.load(file)
print(type(data))
print(data)















