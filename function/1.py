'''def add_num(num1,num2):
    return num1+num2
results=add_num(4,6)
print(results+results)
'''

x = [1,3,4,45,6]

'''def check_even_list(num_list):
    for num in num_list:
        if num % 2 == 0:
            print(num)
        else:
            pass
        
check_even_list(x)
'''


'''def check_even_numbers(num_list):
    even_numbers=[]
    
    for number in num_list:    
        if number%2==0:
            even_numbers.append(number)
        
    print(even_numbers)

check_even_numbers([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
'''
'''work_hours=[('abby',200),('vasu',400),('vignesh',500)]
def  employee_check(work_hours):
    current_max=0
    employee_of_month=""
    for employee,hours in work_hours:
        if hours>current_max:
            current_max=hours
            employee_of_month=employee        
        print(employee_of_month)

employee_check(work_hours)
'''


        
# def myfunc(a,b):
#     return sum((a,b))*0.05
# print(myfunc(40,60))


'''def myfunc(*args):
    for item in args:
        
        print(item)
    
myfunc(20,4,67,45)'''


'''def myfunc(**kwargs):
    print("it is true give name"+kwargs["fruits"])
    
myfunc(fruits="apple",vegetables="mango")    
'''
'''def my_func(food):
    for x in food:
        print(x)
    
food=["kamal","vasu","vimal"]
my_func(food)
'''

'''def my_func(x):
    return 5*x
print(my_func(3))'''

'''def lesser_of_two_even(a,b):
    if a%2==0 and b%2==0:
        
        # print(min(a,b))
        
        return min(a,b)
    else:
        # print (max(a,b))
        return max(a,b)
        
# lesser_of_two_even(4,5)

print(lesser_of_two_even(4,5))
'''


# def animal_crack_list(text):
#     wordlist=text.split() 
#     print(wordlist[0][0]==wordlist[1][0])

# animal_crack_list("lion liger")
    
    
def old(name):
    if len(name)>3:
        return name[:3].capitalize() + name[3:].capitalize()
    
print(old("mecdonalds"))
    
    
