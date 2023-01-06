#range
'''for num in range(0,10,3):
    print(num)'''
    
    #index count
    
'''index_count=0
word= 'abcde'
for letter in word:
    print(word[index_count])
    index_count+=1'''
    #zip

'''mylist=[1,2,3,4]
mylist2=['a','b','c','d']
mylist3=[100,200,300,400]
for a,b,c in zip(mylist,mylist2 ,mylist3):
    print(b)'''
    
    #list comparehsensions
    
    

'''results=[x if x%2==0 else 'odd' for x in range(0,11)]
print(results)'''

'''celcius=[0,10,20,34.5]
fahrenheit=[((9/5)*temp+32)for temp in celcius]
print(fahrenheit)
    '''
    
mylist=[x*y for x in [2,4,6]for y in[1,10,1000]]
print(mylist)



