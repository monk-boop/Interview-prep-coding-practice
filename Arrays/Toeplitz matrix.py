
# coding: utf-8

# In linear algebra, a Toeplitz matrix is one in which the elements on any given diagonal from top left to bottom right are identical. Write a program to check whether a given matrix is a toeplitz matrix or not.

# In[19]:


def toeplitz(a):
    values = {}
    
    for i, row in enumerate(a):
        for j, col in enumerate(row):
            if i-j not in values:
                values[i-j] = col
            else:
                if values[i-j] != col:
                    return False
                
        
    return True
    
    
    
    
    

    
    
    


# In[22]:


a = [[1,2,3],
     [4,1,2]]


# In[23]:


toeplitz(a)

