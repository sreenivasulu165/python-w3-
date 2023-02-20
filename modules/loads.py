import json
emp = '''  { "id":102, "name":"Govind" , "sal":55000} '''
emp_dict = {"id": 101, "name": "Rahul", "sal": 45000}


# convert json sting to python dict
emp_dict1 = json.load(emp)
print(emp_dict1)
