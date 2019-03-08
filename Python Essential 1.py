#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# # Python Programming: Essentials 1
# 
# #### Variables are used to store values. 
# 
# #### A string is a series of characters, surrounded by single or double quotes. 

# Hello world

# In[1]:


print("Hello World") # print() is your first function


# Hello world via a variable

# In[3]:


message= "i feel good" # assigning a string to a variable

print(message) # message is a variable


# 
# 
# Concatenation (combining strings) 

# In[4]:


first_name = 'Chisom' 
last_name = 'Izuka' 

full_name = first_name + ' ' + last_name 

print(full_name)


# In[5]:


full_name


# In[6]:


# little funny one: multiply words! 
print(full_name * 5)


# In[7]:


print(first_name , last_name ) # the comma adds a space automatically


# 
# 
# ## List
# 
# A list stores a series of items in a particular order. 
# 
# You access items using an index, or within a loop. 
# Make a list 

# In[8]:


bicycles = ['mountain', 'road', 'race', 'penny-farthing']

print(bicycles)


# In[9]:


hill = 'mountain'
bikes = [hill, 'road', 'race', 'penny-farthing']


# In[10]:


print(bikes)


# In[12]:


bikes[1]='tricycle'
print(bikes)


# In[13]:


addon = ['raleigh' , 'brompton']

bicycles = bicycles + addon # add a list to a list

print(bicycles)


# In[14]:


bicycles = bicycles + ['peugeot']


# In[15]:


print(bicycles)


# Get the first item in the list

# In[16]:


first_bike = bicycles[0]  # list[position]
print (first_bike)


# In[17]:


third_bike = bicycles[2]  # list[position]
print (third_bike,first_bike)


# Get the last item in the list

# In[ ]:


last_bike = bicycles[-1]
print(last_bike)


# In[18]:


# write code to print the penultimate (i.e. one before last) bike
second_last = bicycles [-2]
print(second_last)


# In[19]:


print(second_last)


# # Working with Strings
# 
# ## split() function

# In[20]:


# the function split() cuts a string at specified character position then store the result in a list

sentence = "'Jeff Bezos divorce: Amazon billionaire 'dating married former TV presenter'"

words = sentence.split(' ')

print(words)


# In[21]:


url = 'https://www.standard.co.uk/news/politics/brexit-secretary-dominic-raab-quits-his-post-a3990626.html'

elements = url.split('/')
print(elements)


# In[ ]:





# In[43]:


# adapt to get the first and second part from an email address

email = "trainingsupport@pairview.co.uk"

########## your code below#############

email_1 = email.split('@')
first_part = email_1[0]
second_part = email_1[1]
print('First part is =',first_part,',' 'Second part is =',second_part)


# In[34]:


# write code to get the first name and the last name from the full name that 
# can include 1 or many middle names

################your code################
myname = "Elizabeth Alexandra Mary Windsor"
new_name = myname.split(' ')
print(new_name)
first_name = new_name[0]
last_name = new_name[-1]

full_name = first_name +' '+ last_name
print (full_name)


# In[38]:


firstletter = first_name[0]
queen_email = firstletter+last_name+ '@'+ second_part
print(queen_email)


# ## join() function

# In[ ]:


words 


# In[44]:


# the function join() take a list of strings and concatenate its elements separated by the character passed to it
separator =' '

sentence = separator.join(words)

print(sentence)


# ## strip() function

# In[50]:


# the function strip() removes unwanted characters (spaces usually) 
# at the beginning and ending of a string
stri = "0000000@@   this is a polluted # string example   @@0000000"

x= stri.strip('0').strip('@').strip()
print(x)

# strip() is equivalent to strip(' ')


# ## replace(old_word,new_word) function

# In[55]:


# and now I present you the function replace
clean =x.replace('polluted # ','cleaned ')
print(clean)


# # for in statement
# ### Looping through a list 

# In[101]:


bicycles = ['mountain', 'road', 'race', 'penny-farthing']


for n in bicycles: 
    print(n)
    print ('still in the loop')
 
print('this is outside the loop')
by = [n for n in bicycles]
print (by)


# In[63]:


bicycles = ['mountain', 'road', 'race', 'penny-farthing']

c=1
word =bicycles[0]
print(c,' : ',word)
c=c+1

word =bicycles[1]
print(c,' : ',word)
c=c+1

word =bicycles[2]
print(c,' : ',word)
c=c+1

word =bicycles[3]
print(c,' : ',word)
c=c+1

print('this is outside the loop')


# ## range () function
#     

# In[65]:


# loop above equivalent to 

for i in range(0,4): #for i = 0 to 3 do in C++
    c = i + 1
    print(c ,' : ',bicycles[i])
    


# In[ ]:


# range function testers


# In[102]:


for number in range(8): # one only attribute = range(0,8)
    print(number)


# In[103]:


for number in range(2,8): # first is start , second the one before
    print(number)


# In[104]:


for number in range(2,8,2): # first is start , second the one before the last # 3rd the step
    print(number)


# ## Adding items to a list

# In[78]:


# add another string
bicycles.append('peugeot')
print(bicycles)


# In[68]:


# equivalent to 
bicycles = bicycles  +  ['peugeot']


# In[69]:


# aside: insert
bicycles.insert(2,'BMX')
print(bicycles)


# In[79]:


# add a number!
bicycles.append(22)
print(bicycles)


# In[72]:


bicycles.remove('BMX') #removes the 1st instance in the list of the attribute
print(bicycles)


# In[76]:


bicycles.pop(-2)


# In[80]:


bicycles.pop() # removes the last item in the list
print(bicycles)


# In[81]:


# add a list!!
bicycles.append(['derailleur','shimano']) 
print(bicycles)

#YOU CAN ADD ANYTHING!!!


# In[84]:


# Code for accessing the second item in the list inside the list
print(bicycles[-1][1])


# ## Making numerical lists

# In[85]:


# initialisation 
cubes = [] 

# loop
for number in range(1, 7): 
    cubes.append(number**3) 

print(cubes)

# ** operator is power


# In[99]:


# write code to calculate the average of numbers from 5 to 15
# the average is the sum divided by the number of elements

series = [5,6,7,8,9,10,11,12,13,14,15]
#range(5,16)
number = len(series)
total= 0
for x in range (5,16):
    total += x
print('Total =', total)
Avg = (total/number)
print ('Average =', Avg)


# In[ ]:





# ## len() function

# In[100]:


# the amazing Len function - aka the length of everything
#len()    
   
l = len (range(5,16)) # number of elements in the numerical series
print(l)

print( len (bicycles)) #number of items in list

print(len('guardian')) # number of character including spaces


# # List comprehensions : Advanced
# 

# In[ ]:


cubes = [x**3 for x in range(1, 7)] 
print(cubes)
# equivalent to 


# In[ ]:


cubes = [] 
for x in range(1, 7): 
    cubes.append(x**3) 
print(cubes)


# ## List comprehension exercise 
# 
# Write one line of Python that takes this list and makes a new list that has only the even elements of this list in it.

# In[ ]:


List = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# ## Slicing a list 

# In[105]:


finishers = ['Sue','Elliot', 'Kumiko','Damien','Aaron'] 
first_two = finishers[:2] # all up to 2 but not 2
print(first_two)


# In[107]:


last_two = finishers[3:] # from 3 (included) up to end
print(last_two)


# In[108]:


f = finishers[:2] + finishers[2:]
print(f)


# In[110]:


last_two = finishers[-2:]
print(last_two)


# In[116]:


reverse = finishers[: :-1]
print(reverse)


# ### Tuples
# 
# Tuples are similar to lists, but the items in a tuple can't be modified. 

# Making a tuple 

# In[117]:


# tuple of numbers
dimensions = (1920, 1080)

# tuples of tuples
pushbikes= ('mountain', 'road', 'race', 'penny-farthing')

#tuple of different types of variables
hold_all = (35, 'Data Science', [1,2,3,4,5], (1,7))

print(hold_all)


# In[118]:


t, x, y , z= hold_all  #puts the elements in the tuple in the assigned variables
print(x)


# In[119]:


#hold_all[0]= 34 square brackets are used to reference positions

print(hold_all[0])


# ### If statements are used to test for particular conditions and respond appropriately.
# 
# # if (condition) : action

# In[120]:


# If statement
age = 25
commonwealth = True

if age >= 18: 
    print("You may be able to vote")
    print("come vote for me!")


# In[121]:


if (age >= 18 and commonwealth == True): # or xor
    print("You can vote!") 
 


# In[126]:


#If-elif-else statements 
if age < 4: 
    price = 0
    print('Kids go free')
elif age < 18: price = 10 
elif age > 65: price = 12
else: price = 15
    

print('£',price)


# Conditions
# 
# tests equals
# x == 42 
# 
# not equal 
# x != 42  
# 
# greater than 
# x > 42 
# 
# greater than or equal to
# x >= 42 
# 
# less than
# x < 42 
# 
# less than or equal to
# x <= 42

# In[127]:


x = 57 #  assign 57 to x

# (x<42) is  a test with a value of True of False
#print('is x smaller than 42?', x < 42)

Var = (x > 42 )

print(Var)

print(x<42)


    


# In[128]:


grade = 80

x = (grade> 70) # pass rate. pass the result of a test to the variable x

if x :
    print("passed")
else :
    print("failed please retake")
    
if x :
    print("admission to uni")   


# ## Conditional test with lists 
# ## IN
# ## NOT IN

# In[129]:


print('downhill' in bicycles)


# In[130]:


print('downhill' not in bicycles)


# In[131]:


if 'downhill' not in bicycles:
    bicycles.append('downhill')


# In[132]:


# downhill tricycle
if 'downhill' not in bicycles and 'tricycle' not in bicycles :
    bicycles = bicycles + ['downhill','tricycle']


# In[133]:


print(bicycles)


# In[134]:


newbikes = ['downhill', 'tricycle', 'fixie']


# In[136]:


for b in bicycles:
    if b not in newbikes:
        newbikes.append(b)
    else: print(b,' already in')
        
print(newbikes)


# Assigning boolean values

# In[139]:


game_active = True
can_edit = False

if game_active or can_edit:
    print('yay')


# # Exercise
# 
# Take a list of numbers
# and write a program that prints out all the elements of the list that are less than 5.

# In[150]:


# set list

List = [1, 1, 25, 3, 55, 8, 13, 21, 3, 5, 89]
less = []
# your code below
for x in List:
    if x<5:
        less.append(x)
print (less)


# In[152]:


# i want to put in a new list the odd numbers
odd=[]
even = []
for x in List:
    if x%2 !=0:
        odd.append(x)
    else: even.append(x)
print (odd)
print (even)
    


# In[ ]:


odds =[]



print(odds)


# In[153]:


#  modulo operation % gives the remainder of division
# div operation // that performs an integer division

print(5 % 2)
print(5 // 2)


# # Dictionaries 
# they store connections between pieces of information
# 
# Each item in a dictionary is a key-value pair

# Simple dictionaries {}

# In[154]:


word_frequency = {'Data' : 14, 'Science': 10, 'Machine': 5, 'Learning' : 8}


real_dictionary = {'a': 'string that defines a', 'abc': 'definition of abc'}


# with different value types
car = {'make' : 'Mazda', 'model' : '3 sport', 'engine_size_cc': 2259,
       'colour': 'laser blue', 'dimensions_mm' : {'w':1795 , 'l':4465 , 'h':1465}}


# Accessing a value

# In[155]:


print( car['colour'])
# dict[key] accesses the value in key , value pair


# In[158]:


#write code to retrieve the dictionary inside the dictionary
print(car['dimensions_mm'])


# In[ ]:


# retrieve the value in the dictionary inside the dictionary
# width w
dict = {'w': 1795, 'l': 4465, 'h': 1465}
dict['w']


# In[159]:


print(car['dimensions_mm']['w'])


# In[160]:


# Adding / modifying a new key-value pair
car['transmission_type'] = 'automatic'

car['colour'] = 'blood red'
# dic[key] = value
print(car)


# In[165]:


numbers = [4,9,12,17]
numbers[2]=13
print (numbers)


# In[166]:


numbers = numbers +[10]
print (numbers)


# In[167]:


numbers.pop(4)
print (numbers)


# Values, Keys and Items

# In[161]:


print(car.items())


# In[168]:


print(car.keys())


# In[169]:


print(car.values())


# Looping through all keys

# In[170]:


# for keys in dictionary:

for k in car.keys(): 
    print(k + ' is a car characteristic') 


# Looping through all the values

# In[171]:


# write code to loop through all the values
for v in car.values(): 
    print(v, "is a characteristic") 


# Looping through all key-value pairs

# In[172]:


for k,v in car.items():
    print(k , 'is', v)


# In[178]:


Tuples_List = [(1,2,3) , (4,5,6) , (7,8,9)]

for a , b , c in Tuples_List:
    print(a*b/c)
cubic = [(round(a*b/c,2)) for a,b,c in Tuples_List]
print (cubic)


# In[188]:


#Write a Python script to concatenate following dictionaries to create a new one. 

#Sample Dictionary : 
dic1={1:'Royal Dutch Shell', 2:'BP'} 
dic2={3:'Total', 4:'Volkswagen'} 
dic3={5:'Glencore Xstrata',6:'Gazprom'}

dic_final = dic1

for k,v in dic2.items():
    dic_final[k] = v
for k,v in dic3.items():
    dic_final[k]=v
    
print(dic_final)
    


# In[191]:


# Write a Python script to check if a given key already exists in a dictionary.

test_number = 7
key_in_dictionary = False

### your code ####
if test_number in dic_final.keys():
    print ('got it')
else : print('please add to dictionary')


# ### Programs can prompt the user for input. 
# All input is stored as a string. 
# 
# Prompting for a value

# In[192]:


# prompting for a value  input always returns a string
name = input("What's your name? ") 
print("Hello, " + name + "!") 


# In[194]:


# prompting for a number

age = int(input("How old are you? ")) #return a string
print(age*7)


# In[195]:


pi = input("What's the value of pi? ") 
print(pi)
pi = float(pi)


# # Exercise
# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

# In[200]:


#initialisation
current_year = 2019
age = int(input('What is your age? '))
Diff = 100 - age
Centinary = current_year + Diff
print ('You will turn 100 in', Centinary)


# In[211]:


# Write a Python program that prompts for a month name and converts it to a number
# of days.
#List of months: January, February, March, April, May, June, July, August
#, September, October, November, December                                

# Example
#Input the name of Month: February                                       
#No. of days: 28/29 days 

Month = {'January': 31, 'February': '28/29', 'March': 31, 'April':30, 'May': 31, 'June': 30, 'July':31, 'August': 31, 
        'September': 30, 'October': 31, 'November': 30, 'December': 31}
mth = input('Give a month = ')
print ('Number of days is', Month[mth])


# In[ ]:




