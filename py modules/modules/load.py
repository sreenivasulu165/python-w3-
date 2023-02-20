import json
fp = open('d:\py modules\modules\srinu.json', 'r')
emp_dict = json.load(fp)
print(emp_dict)
fp.close()
# for emp_list in emp_dict:
#     print(emp_list)
