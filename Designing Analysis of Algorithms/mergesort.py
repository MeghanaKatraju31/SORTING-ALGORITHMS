#!/usr/bin/env python
# coding: utf-8

# In[1]:


# - importing required packages
# - math for average calculations
# - time for calculating time taken for the sorting algorithm
# - sys for getting the max value of the system (place holder for infinite value)

import math
import time
import sys


# In[2]:


# - read_file : function => reads the data instde the files generated
# - number : argument => A number is given to specify the no. of rows (20, 100, 1000, 4000 as per the problem statement)

def read_file(number):
    file = open('arr'+str(number)+'.txt', 'r')
    data = file.readlines()
    for i in range(number):
        data[i] = list(map(int, data[i].strip().split(' '))) #to convert str data to int (data is stored as str in txt file)
    file.close()
    return(data)


# In[3]:


# - find_sum_for_row : function => finds the sum of each row in the files and appends to that row
# - data : argument => contains the data of the files as list of lists format

def find_sum_for_row(data):
    for i in range(len(data)):
        data[i].append(sum(data[i]))
    return(data)


# In[4]:


# - generate_output_files : function => writes the sorted data into a file along with the time taken by the sorting algorithm
# - number : argument => A number is given to specify the no. of rows (20, 100, 1000, 4000 as per the problem statement)
# - data : argument => contains the data of the files as list of lists format (sorted)
# - time_taken : argument => variable that holds the time taken by the sorting algorithm

def generate_output_files(number, data, time_taken):
    with open('arrMR_O_'+str(number)+'.txt', 'w') as file:
        for row in data:
            file.write(" ".join(map(str, row)) + "\n") #convert int data to str (data is stored as str in txt file)
        file.write("Time Taken for sorting (merge) "+str(number)+" rows: " + time_taken +" Nano secs")
    
    file.close()


# In[5]:


# - mergesort : function => mergesort algorithm is defined
# - data_sum : argument => unsorted data is in the for of list of lists
# - p : argument => starting index of array ( or list) 
# - r : argument => ending index of array (or list)
# - q : argument => middle index of the array ( or list)

def merge(data_sum, p, q, r):
    n1 = q - p 
    n2 = r - q - 1
    Left = []
    Right = []
    for i in range(n1 + 1):
        Left.append(data_sum[p + i])
    for j in range(n2 + 1):
        Right.append(data_sum[q + j + 1])
    Left.append([sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize]) #adding inf to the lists for end condition of comparing
    Right.append([sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize]) #adding inf to the lists for end condition of comparing
    i = 0
    j = 0
    for k in range(p, r + 1):
        if Left[i][3] <= Right[j][3]:
            data_sum[k] = Left[i]
            i = i + 1
        else:
            data_sum[k] = Right[j]
            j = j + 1


# In[6]:


# - mergesort : function => mergesort algorithm is defined
# - data_sum : argument => unsorted data is in the for of list of lists
# - p : argument => starting index of array ( or list) 
# - r : argument => ending index of array (or list)

def mergesort(data_sum, p, r):
   
    #sorting
    if p < r:
        q = math.floor((p + r) / 2)
        mergesort(data_sum, p, q) #recursive calls for the algorithm
        mergesort(data_sum, q + 1, r)
        merge(data_sum, p, q, r) # a function call to merge two arrays inplace of the parent array


# In[7]:


# - call_mergesort : function => function that calls the merge sort algorithm function
# - number : argument => A number is given to specify the no. of rows (20, 100, 1000, 4000 as per the problem statement)

def call_mergesort(number):
    data = read_file(number)
    data_sum = find_sum_for_row(data)
    
    print("Data before sorting: ", data_sum)
    
    #sorting
    start_time = time.time_ns() #start time of algorithm
    
    #merge sort algorithm begins
    mergesort(data_sum, 0, len(data_sum) - 1)
    #merge sort algorithm ends
    
    end_time = time.time_ns() #end time of algorithm
    
    time_taken = str(end_time - start_time) #calculating the time taken by the algorithm
    
    print("Data after sorting: ", data_sum)
    print("Time Taken for sorting (merge) "+str(number)+" rows: " + time_taken +" Nano secs")
    
    generate_output_files(number, data_sum, time_taken)


# In[8]:


call_mergesort(20)
call_mergesort(100)
call_mergesort(1000)
call_mergesort(4000)

