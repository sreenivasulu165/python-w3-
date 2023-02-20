'''st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word[0]=='s':
        print(word)
        '''
        
'''st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word)%2==0:
        print(word)
        '''
        
'''for num in range(1,100):
    if num % 3==0 and num %5==0:
        print("fizz,buzz")
    elif(num % 3==0):
        print("fizz=divisible by 3")
    elif(num % 5==0):
        print("buzz = divsible by5")
    else:
        print(num)'''
        
st = 'Create a list of the first letters of every word in this string'
[word[0] for word in st.split()]



    
