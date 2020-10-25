import json


# Read text file
# file = open("C:/Users/ksy/Desktop/PyFiles/textfile.txt")
# print(file.read())

    # Read only few characters
# file = open("C:/Users/ksy/Desktop/PyFiles/textfile.txt")
# print(file.read(10))

# Read only first line
# file = open("C:/Users/ksy/Desktop/PyFiles/textfile.txt")
# print(file.readline())

# Read all lines
# file = open("C:/Users/ksy/Desktop/PyFiles/textfile.txt")
# print(file.readlines())

# OverWrite the existing text file
# file = open("C:/Users/ksy/Desktop/PyFiles/textfile.txt",mode='w')
# str = "Welcome to Java class"
# file.write(str)
# file.close()


# Append content to existing text file
# file = open("C:/Users/ksy/Desktop/PyFiles/textfile.txt",mode='a')
# str = "Welcome to Java class"
# file.write("\n")
# file.write(str)
# file.close()


# Read Json file content
# file = open("C:/Users/ksy/Desktop/PyFiles/textfile.json")
# data = file.read()
# json_data = json.loads(data)
# print(json_data)


# Fetch Json file content
# file = open("C:/Users/ksy/Desktop/PyFiles/textfile.json")
# data = file.read()
# json_data = json.loads(data)
# print("Company :",json_data['Company'])


# Add data to existing Json file
# file = open("C:/Users/ksy/Desktop/PyFiles/textfile.json")
# data = file.read()
# json_data = json.loads(data)
# print(json_data)
# file.close()
#
# file = open("C:/Users/ksy/Desktop/PyFiles/textfile.json",mode='w')
# str = {'Addrs': 'AOR'}
# json_data.update(str)
# print(json_data)
# json.dump(json_data,file)
# file.close()



# Update json file content
# str = {'Addrs': 'Hebbal'}
# file = open("C:/Users/ksy/Desktop/PyFiles/textfile.json")
# data = file.read()
# json_data = json.loads(data)
# json_data.update(str)
# file = open("C:/Users/ksy/Desktop/PyFiles/textfile.json",mode='w')
# json.dump(json_data,file)
# file.close()


# Update json file content
# file = open("C:/Users/ksy/Desktop/PyFiles/textfile.json")
# data = file.read()
# json_data = json.loads(data)
# json_data['Addrs']="Hebbal"
# file = open("C:/Users/ksy/Desktop/PyFiles/textfile.json",mode='w')
# json.dump(json_data,file)
# file.close()


# Convert txt file to json file
# file = open("C:/Users/ksy/Desktop/PyFiles/txtTojson.txt")
# data = file.readline()
# dict = {}
#
# while data:
#     key,val = data.split(' ', 1)
#     dict[key] = val
#     data = file.readline()
#
# print(dict)
# file.close()
#
# file = open("C:/Users/ksy/Desktop/PyFiles/jsonfile.json",mode='w')
# json.dump(dict,file)
# file.close()


# How will you use Python to read a random line from a file?
# import random
# file = open("C:/Users/ksy/Desktop/PyFiles/TestFile1.txt")
# data = file.read()
# print(random.choice(data.split()))





