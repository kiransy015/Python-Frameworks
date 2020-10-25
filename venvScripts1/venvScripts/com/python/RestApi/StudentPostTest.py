import requests

print('--------------------Post Call with header and body------------------------------')
stdcourses=['Accounting','Statistics']

response = requests.post('http://localhost:8085/student',json={"firstName":"Kiran","lastName":"Kumar","email":"kiran@gmail.com","programme":"Computer Science","courses":stdcourses})
# Print request details
print("Request header :",response.request.headers['Content-Type'])
print("Request body :",response.request.body)
print("Request url :",response.request.url)

# Print the response status
print(response.status_code)
# Print response text
print(response.text)