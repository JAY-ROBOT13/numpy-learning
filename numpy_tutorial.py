#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[11]:


##creating array


# In[3]:


list1=[1,2,3]
print(list1)


# In[4]:


arr_list1=np.array(list1)
print(arr_list1)


# In[5]:


print(type(arr_list1))


# In[6]:


list1=[1,2,3]
list2=[4,5,6]
arr_list1_2=np.array([list1,list2])
print(arr_list1_2)


# In[7]:


print(arr_list1_2.ndim)


# In[8]:


list1=[1,2,3]
list2=[4,5,6]
list3=[7,8,9]
arr_list1_3=np.array([[list1,list2,list3]])
print(arr_list1_3)


# In[9]:


print(arr_list1_3.ndim)


# In[10]:


# 2.numpy array attribute


# In[11]:


arr1=np.array([[1,2,3],[4,5,6]])
print(arr1)


# In[12]:


print("shape:",arr1.shape)
print("size:",arr1.size)
print("ntype:",arr1.dtype)
print("n_dim:",arr1.ndim)


# #crate 2 array:1D and 3D and find it's attribute

# In[13]:


#3.Array initialisation methods


# In[14]:


# Zero array

zero_arr=np.zeros((2,3))
print(zero_arr)


# In[15]:


# one array

ones_arr=np.ones((2,3))
print(ones_arr)


# In[16]:


#full array:

full_arr=np.full((3,2),8)
print(full_arr)


# In[17]:


#Identity  matrix(3 * 3):There diagonal element is one and other element is zero

id_arr=np.eye(3)
print(id_arr)


# In[18]:


# Empty array:
print(np.empty(3))


# In[19]:


# Evenly spaced array
print(np.arange(1,10,1))  # not include 10


# In[20]:


# specific number of equally (spaced) values between a range
print(np.linspace(1,10,6))   # spilt value into specific range


# In[21]:


#Random value generate array:  All values in float 

r_arr=np.random.rand(3,2)
print(r_arr)


# In[22]:


# Random values array in int
rint_arr=np.random.randint(1,8,(3,3))
print(rint_arr)


# In[23]:


#Array indexing and slicing:


# In[24]:


a=np.array([1,3,5,7,9])
print(a)

# slicing in array:
# array[start:stop:step]     
# stop-index that is not included in output
# In[26]:


a=np.array([1,2,3,4,5,6])
print(a[0:3])          #first three element


# In[28]:


print(a[-3:])       #last three element


# In[30]:


print(a[1:4])      #middle three element


# In[33]:


print(a[0::2])       # 2 step between number


# In[35]:


print(a[::])        #It take bidefault 1 step


# In[36]:


# two dimensional array:


# In[38]:


arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)


# In[41]:


print(arr2[0])      #slicing in 2D array
print(arr2[1])


# In[42]:


print(arr2[0][1])


# In[43]:


print(arr2[1][2])


# In[47]:


print(arr2[1])
print(arr2[1:])      #Dimension vary


# In[49]:


print(arr2[:,0])

#  2D:[rows,columns]
# 3D:[layers/height,rows,columns]


# In[52]:


arr3=np.array([[1,2,3],         # dimensional array
               [4,5,6],
               [7,8,9]])
print(arr3)


# In[54]:


print(arr3[0])
print(arr3[1])
print(arr3[2])


# In[55]:


print(arr3[0][2])
print(arr3[2][2])


# In[59]:


print(arr3[:,0])           #1st column value
print(arr3[:,1])          # 2nd coulmn value
print(arr3[:,2])          #2nd column value


# In[62]:


print(arr3[::2,0])       #Jump the value after colon(;) all values are  columns and
                         #before colon(;) all values are row
print(arr3[::,1:2])      # all values taken from first row element


# In[63]:


print(arr3[2::,1:2])


# In[69]:


print(arr3[1::,1:2])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




