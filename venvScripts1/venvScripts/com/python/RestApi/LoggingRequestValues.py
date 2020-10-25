import requests

# print("------------- Printing Request Headers ----------------")
# response = requests.get('http://localhost:8085/student/list')
# print("Request header :",response.request.headers)


# print("------------- Printing Request Parameters ----------------") ------------------ > Not Working
# response = requests.get('http://localhost:8085/student/list?programme=Computer Science&limit=3')
# print("Request parameters :",response.request.params)


# print("------------- Printing Request Body ----------------") ------------------ > Not Working
# stdcourses = ['Accounting','Statistics']
# response = requests.post('http://localhost:8085/student',json={"firstName":"Kiran","lastName":"Kumar","email":"kiran@gmail.com","programme":"Computer Science","courses":stdcourses})
# print("Request body :",response.request.data)


# print("------------- Printing All the Request Details ----------------") ------------------ > Not Working
# stdcourses = ['Accounting','Statistics']
# response = requests.post('http://localhost:8085/student',json={"firstName":"Kiran","lastName":"Kumar","email":"kiran@gmail.com","programme":"Computer Science","courses":stdcourses})
# print("Request body :",response.request)
