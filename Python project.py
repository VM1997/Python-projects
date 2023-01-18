#!/usr/bin/env python
# coding: utf-8

# # Python Project
Q1: You are working in a bank and you have been given two lists of the employees who worked in 2021.
Employee’s name in list 1 are Ramesh, Suresh, Mahesh, Ali, Jacob and Saritha. 
List 2 contains the names of Ali, Mukesh, Mahesh, Jacob, Sai, Sarita.
Please write a program which helps to identify people who are common in both lists. Please do not use any in-built function.


# In[30]:


List1=['Ramesh','Suresh','Mahesh','Ali','Jacob','Sritha']
List2=['Ali','Mukesh','Mahesh','Jacob','Sai','Saritha']
set(List1).intersection(List2)


# In[ ]:


OR


# In[26]:


def common(): 
    List1=['Ramesh','Suresh','Mahesh','Ali','Jacob','Sritha']
    List2=['Ali','Mukesh','Mahesh','Jacob','Sai','Saritha']
    common_name = [name for name in List1 if name in List2] 
    print('Common name in both the lists are',common_name)
    
common()   


# Q2: While entering data, someone entered a few names as a common string “Ramesh Suresh Mohit”. 
#     Please write a program which separates all the names and convert them into a list. 
#     Once converted in a list, please write a program which adds their age.
# 
# 

# In[16]:


common_string=('Ramesh Suresh Mohit')
Names=list(common_string.split())

Names=['Ramesh', 'Suresh', 'Mohit']
age=[25,22,26]
print(Names[0],':',age[0])
print(Names[1],':',age[1])
print(Names[2],':',age[2])


# Q3: A few students from a university have taken three exams
# 
# Name = Sam, Jacy, Tom, Steve
# 
# Python = 25, 26, 29, 28
# 
# Statistics = 23, 21, 19, 25
# 
# SQL = 29, 27, 28, 25
# 
#  
# 
# Please write a program which calculates mean values (no in-built function for mean) of all three tests and print the highest mean value. Addition and other functions are allowed. Please also report who scored the highest mark in python using programming construct. 
# 
# 

# In[97]:


python=[25,26,29,28]
Statistics = [23, 21, 19, 25]
SQL = [29, 27, 28, 25]


total_py= sum(python)
total_stats= sum(Statistics)
total_sql= sum(SQL)

n_py=len(python)
n_stats=len(Statistics)
n_sql=len(SQL)

mean_py= total_py/n_py
mean_stats= total_stats/n_stats
mean_sql=total_sql/n_sql

print('Mean value for python is',mean_py)
print('Mean value for Statistics is',mean_stats)
print('Mean value for SQL is',mean_sql)

highest_mean=max(mean_py,mean_stats,mean_sql)
print('The highest mean value is',highest_mean)


python_marks ={'Sam':25, 'Jacy':26, 'Tom':29, 'Steve':28}
highest_marks=max(python_marks)
print('The highest marks in python is obtained by', highest_marks)


# 

# In[ ]:


Q4: You are working in a medical store. 
    A patient came to your medical store and asked to buy 2 strips of paracetamol, 
    3 strips of azithromycin and 5 strips of Vitamin C. One strip of paracetamol costs Rs 35,
    one strip of azithromycin costs Rs 49 and one strip of vitamin c costs Rs. 33.
    Patient gave you Rs 2000. Please tell us what is the total cost of each medicine, 
    total cost of all medicine and how much money you refunded to the patient?  


# In[16]:


cost_of_paracetamol =35
cost_of_azithromycin = 49
cost_of_vitamin_C=33

quantity_of_paracetamol=2
quantity_of_azithromycin=3
quantity_of_vitamin_c=5

total_cost_of_paracetamol= cost_of_paracetamol * quantity_of_paracetamol
total_cost_of_azithromycin= cost_of_azithromycin * quantity_of_azithromycin
total_cost_of_vitamin_C= cost_of_vitamin_C * quantity_of_vitamin_c

print('Total_cost_of_paracetamol is',total_cost_of_paracetamol)
print('Total_cost_of_azithromycin is',total_cost_of_azithromycin)
print('Total_cost_of_vitamin_C is',total_cost_of_vitamin_C)

total_cost_of_medicines = total_cost_of_paracetamol+total_cost_of_azithromycin+total_cost_of_vitamin_C
print('The total cost of medicines is',total_cost_of_medicines)

Patient_paid= 2000
Refund_amount= Patient_paid - total_cost_of_medicines
print('Money refunded to the customer is',Refund_amount)


# In[ ]:





# Q5: Accept a sentence as input and find the number of vowels in it.
#     Assume that the sentence has no punctuation marks. 
#     For example: I am learning python contains 6 vowels. 
#     This function should be applicable for all other different sentences.
# 
# 

# In[14]:


str1 = input("Please Enter Your Own String : ")
vowels = 0

for i in str1:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'
       or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowels = vowels + 1 
print("Total Number of Vowels in this String = ", vowels)


# In[ ]:





# In[ ]:


Q6: You have been appointed by the election commission to create a website. 
    Your first task is to work on a program which tells candidates if they are eligible for voting or not.
    If they are eligible your output should be ‘Congrats! You are eligible’, 
    otherwise it should tell that you have to return after X number of years.
    Eligibility criteria for voting is 18 years.


# In[12]:


n=int(input('enter number to check eligibility criteria=', ))
i=18
if n>=i:
    print('Congrats you are eligible')
else:
    print('return after', (i-n),'years')

