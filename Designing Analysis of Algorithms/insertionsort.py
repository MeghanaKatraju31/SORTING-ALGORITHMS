#!/usr/bin/env python
# coding: utf-8

# In[1]:


# - importing required packages
# - random for generating random numbers for the input files
# - time for calculating time taken for the sorting algorithm

from random import *
import time


# In[2]:


# - generate_files : function => Generates files with random numbers as per the problem statement
# - number : argument => A number is given to specify the no. of rows (20, 100, 1000, 4000 as per the problem statement)

def generate_files(number):
    data = []
    for i in range(number):
        data.append([randint(0,99), randint(0,99), randint(0,99)])
    with open('arr'+str(number)+'.txt', 'w') as random_number_file:
        for row in data:
            random_number_file.write(" ".join(map(str, row)) + "\n")
    
    random_number_file.close()
    print('File created')


# In[3]:


# - read_file : function => reads the data instde the files generated
# - number : argument => A number is given to specify the no. of rows (20, 100, 1000, 4000 as per the problem statement)

def read_file(number):
    file = open('arr'+str(number)+'.txt', 'r')
    data = file.readlines()
    for i in range(number):
        data[i] = list(map(int, data[i].strip().split(' '))) #to convert str data to int (data is stored as str in txt file)
    file.close()
    return(data)


# In[4]:


# - find_sum_for_row : function => finds the sum of each row in the files and appends to that row
# - data : argument => contains the data of the files as list of lists format

def find_sum_for_row(data):
    for i in range(len(data)):
        data[i].append(sum(data[i]))
    return(data)


# In[5]:


# - generate_output_files : function => writes the sorted data into a file along with the time taken by the sorting algorithm
# - number : argument => A number is given to specify the no. of rows (20, 100, 1000, 4000 as per the problem statement)
# - data : argument => contains the data of the files as list of lists format (sorted)
# - time_taken : argument => variable that holds the time taken by the sorting algorithm

def generate_output_files(number, data, time_taken):
    with open('arrIS_O_'+str(number)+'.txt', 'w') as file:
        for rows in data:
            file.write(" ".join(map(str, rows)) + "\n") #convert int data to str (data is stored as str in txt file)
        file.write("Time Taken for sorting (insertion) "+str(number)+" rows: " + time_taken +" Nano secs")
    
    file.close()


# In[6]:


def insertionsort(number):
    data = read_file(number)
    data_sum = find_sum_for_row(data)

    print("Data before sorting: ", data_sum)
    
    #sorting
    start_time = time.time_ns() #start time of algorithm
    
    #insertion sort algorithm begins
    for j in range (1, number):
        key = data_sum[j]
        i = j - 1
        while i > -1 and data_sum[i][3] > key[3]:
            data_sum[i + 1] = data_sum[i]
            i = i - 1
        data_sum[i + 1] = key
    #insertion sort algorithm begins    
    
    end_time = time.time_ns() #end time of algorithm
    
    time_taken = str(end_time - start_time) #calculating the time taken by the algorithm
    
    print("Data after sorting: ", data_sum)
    print("Time Taken for sorting (insertion) "+str(number)+" rows: " + time_taken +" Nano secs")
    
    generate_output_files(number, data_sum, time_taken)
    


# In[7]:


generate_files(20)
generate_files(100)
generate_files(1000)
generate_files(4000)


# In[8]:


insertionsort(20)
insertionsort(100)
insertionsort(1000)
insertionsort(4000)

