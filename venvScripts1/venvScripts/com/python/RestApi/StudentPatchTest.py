import requests

stdcourses = ['Accounting','Statistics']
response = requests.patch('http://localhost:8085/student/107',json={"firstName":"Kiran","lastName":"Kumar","email":"kiran@gmail.com","programme":"Computer Science","courses":stdcourses})

print(response.status_code)
print(response.text)