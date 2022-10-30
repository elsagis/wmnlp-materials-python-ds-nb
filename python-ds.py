#!/usr/bin/env python
# coding: utf-8

# # Web Mining and Applied NLP (44-620)
# 
# ## Python Notebooks, Basics, and Data Structures
# 
# ### Student Name: Elsa Ghirmazion
# 
# Perform the tasks described in the Markdown cells below.  When you have completed the assignment make sure your code cells have all been run (and have output beneath them) and ensure you have committed and pushed ALL of your changes to your assignment repository.
# 
# Every question that requires you to write code will have a code cell underneath it; you may either write your entire solution in that cell or write it in a python file (`.py`), then import and run the appropriate code to answer the question.
# 
# Do not use external modules (`math`, etc) for this assignment unless you are explicitly instructed to, though you may use built in python functions (`min`, `max`, etc) as you wish.

# 1. Modify the Markdown cell above to put your name after "Student Name:"; you will be expected to do this in all assignments presented in this format for this class.

# 2. Write code that divides any two numbers, stores the result in a variable, and prints the result with an appropriate label.

# In[6]:


x=60
y=4
result = x/y
print(result)


# 3. Using loops (and potentially conditionals), write Python code that prints the factorial of each integer from 1 through 10 (which you can store in a variable if you want). The factorial of an integer is the product of all of the integers of 1 through the number. Print the result with an appropriate label.

# In[74]:


# Python program to find the factorial of a number provided by the user
# using recursion

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        # recursive call to the function
        return (x * factorial(x-1))


# change the value for a different result
num = 10

# to take input from the user
# num = int(input("Enter a number: "))

# call the factorial function
result = factorial(num)
print("The factorial of", num, "is", result)


# 4. Write a python function that takes a single parameter and calculates and returns the average (mean) of the values in the parameter (which you may assume is iterable).  Show that your function works by printing the result of calling the function on the list in the cell below.

# In[75]:


testlist = [1,-1,2,-2,3,-3,4,-4]
print(sum(testlist))
print(len(testlist))
mean = sum(testlist)/ len(testlist)
print(mean)
list_avg = mean
print(list_avg)


# 5. Using your mean function above, write a function that calculates the variance of the list of numbers (see https://en.wikipedia.org/wiki/Variance for more information on the formula). In short:
# * subtract the mean of the elements in the list from every element in the list; store these values in a new list
# * square every element in the new list and sum the elements together
# * divide the resulting number by N (where N is the length of the original list)
# 
# Show the result of calling your function in the lists in the code cell. You must use one or more list comprehensions or map/filter in your code.
# 

# In[76]:


list1 = [ 5.670e-1, -1.480e+0, -5.570e-1, -1.470e+0, 7.340e-1, 1.050e+0, 4.480e-1, 2.570e-1, -1.970e+0, -1.460e+0]
list2 = [-1.780e+0, 2.640e-1, 1.160e+0, 9.080e-1, 1.780e+0, 1.080e+0, 1.050e+0, -4.630e-2, 1.520e+0, 5.350e-1]
# the variances of both lists should be relatively close to 1 (off by less than .15)
print(sum(list1))
print(len(list1))
mean = sum(list1)/ len(list1)
print(mean)
print(sum(list2))
print(len(list2))
mean = sum(list2)/ len(list2)
print(mean)
print(list(map(lambda x: x- mean, list1)))
squares =[]
for x in (list1):
 squares.append(x**2)
print(squares)
n = len(list1)
print(sum(squares)/ n)


# 6. Create a list with at least 15 elements in it. Use list slicing to print the following:
# * The first 5 elements of the list
# * The last 5 elements of the list
# * The list reversed (hint, show the entire list with a stride of -1)
# * Every second element in the list
# * Every third element in the list (stride of 3)

# In[77]:


my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(my_list[0:5])
print(my_list[-5::])
print(my_list[::-1])


# 7. Build a dictionary that contains the following information about this class (with appropriate names as keys):
# * The name
# * The course number
# * The semester/term in which you are taking this course
# * The number of credit hours this course counts for
# * A list of the course learning objectives
# 
# The majority of this information can be found in the syllabus. Print the dictionary.

# In[78]:


my_dict = {'name':'EsaGhirmazion', 'CSID': 44620, 'term':'Fall', 'credit': 3, 'ojectives':{'work with python Data tructures', 'Interact with Python Notebook', 'Use Git to manage source code'}}
print(my_dict['name'])
print(my_dict['CSID'])
print(my_dict)


# 8.  Given the dictionary defined in the code cell below, print the list of level 3 spells the character has.

# In[79]:


player_character = {'name': 'Kitab',
                   'class': [('Cleric: Knowledge', 7)],
                   'spells': {'cantrip': ['Guidance', 'Light', 'Thaumaturgy', 'Toll the Dead', 'Word of Radiance'],
                             'level 1': ['Command', 'Detect Magic', 'Healing Word', 'Identify', 'Sleep'],
                             'level 2': ['Augury', 'Calm Emotions', 'Command', 'Invisibility', 'Lesser Restoration'],
                             'level 3': ['Mass Healing Word', 'Nondetection', 'Revivify', 'Feign Death', 'Speak with Dead'],
                             'level 4': ['Banishment', 'Confusion']}
                   }
print(player_character['spells']['level 3'])


# 9. Write code to determine the number of unique elements in the list below.  You MUST use a set in finding your solution.  Print the number of unique values in the list with an appropriate label.

# In[80]:


values = [10, 11, 10, 8, 1, 12, 0, 1, 6, 5, 5, 13, 6, 15, 0, 0, 1, 1, 9, 7]
seta = {10, 11, 10, 8, 1, 12, 0, 1, 6, 5}
setb = {5, 13, 6, 15, 0, 0, 1, 1, 9, 7}
print('Symetric Difference', seta ^ setb)


# 10. Create a new Jupyter Notebook (the name of the notebook should be your S number). Add a Markdown cell that contains your name. Add a Code cell and write Python that uses loops to draw the following pattern:
# 
# ```
# *      *
# **    **
# ***  ***
# ********
# ```
# Make sure to add and submit both the new notebook and the changes to this notebook for this assignment.
