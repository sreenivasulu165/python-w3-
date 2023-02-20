import json
import requests
user_response = requests.get('https://dummyjson.com/users')
print(user_response)
user = user_response.json()
print(user)
