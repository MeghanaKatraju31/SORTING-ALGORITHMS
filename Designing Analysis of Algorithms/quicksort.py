#!/usr/bin/env python
# coding: utf-8

# In[1]:


# - importing required packages
# - math for average calculations
# - time for calculating time taken for the sorting algorithm

import math
import time


# In[2]:


# - read_file : function => reads the data instde the files generated
# - number : argument => A number is given to specify the no. of rows (20, 100, 1000, 4000 as per the problem statement)

def read_file(number):
    file = open('arr'+str(number)+'.txt', 'r')
    data = file.readlines()
    for i in range(number):
        data[i] = list(map(int, data[i].strip().split(' ')))
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
    with open('arrQK_O_'+str(number)+'.txt', 'w') as file:
        for rows in data:
            file.write(" ".join(map(str, rows)) + "\n") #convert int data to str (data is stored as str in txt file)
        file.write("Time Taken for sorting (quick) "+str(number)+" rows: " + time_taken +" Nano secs")
    
    file.close()


# In[5]:


# - partition : function => function to find the location where pivot element swaps
# - data_sum : argument => unsorted data is in the for of list of lists
# - p : argument => starting index of array ( or list) 
# - r : argument => ending index of array (or list)

def partition(data_sum, p, r):
    x = data_sum[r]
    i = p - 1
    for j in range(p, r):
        if data_sum[j][3] <= x[3]:
            i = i + 1
            data_sum[i], data_sum[j] = data_sum[j], data_sum[i] #swapping elements in the array is less than pivot
    data_sum[i + 1], data_sum[r] = data_sum[r], data_sum[i + 1] #swapping pivot value
    return i + 1


# In[6]:


# - quicksort : function => quicksort algorithm is defined
# - data_sum : argument => unsorted data is in the for of list of lists
# - p : argument => starting index of array ( or list) 
# - r : argument => ending index of array (or list)

def quicksort(data_sum, p, r):
   
    #sorting
    if p < r:
        q = partition(data_sum, p, r)
        quicksort(data_sum, p, q - 1)
        quicksort(data_sum, q + 1, r)


# In[7]:


# - call_mergesort : function => function that calls the merge sort algorithm function
# - number : argument => A number is given to specify the no. of rows (20, 100, 1000, 4000 as per the problem statement)

def call_quicksort(number):
    data = read_file(number)
    data_sum = find_sum_for_row(data)
    
    print("Data before sorting: ", data_sum)
    
    #sorting
    start_time = time.time_ns() #start time of algorithm
    
    #quick sort algorithm begins
    quicksort(data_sum, 0, len(data_sum) - 1)
    #quick sort algorithm ends
    
    end_time = time.time_ns() #end time of algorithm
    
    time_taken = str(end_time - start_time) #calculating the time taken by the algorithm
    
    print("Data after sorting: ", data_sum)
    print("Time Taken for sorting (quick) "+str(number)+" rows: " + time_taken +" Nano secs")
    
    generate_output_files(number, data_sum, time_taken)


# In[8]:


call_quicksort(20)
call_quicksort(100)
call_quicksort(1000)
call_quicksort(4000)

