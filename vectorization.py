#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
a=np.array([1,2,3,4,5])
print(a)


# In[4]:


import time
a=np.random.rand(10000000)
b=np.random.rand(10000000)#million dimension array

tic=time.time()
c=np.dot(a,b)
print(c.shape)
toc=time.time()
print(c)
print("vector"+str(1000*(toc-tic))+"ms")
#non vector
c=0
tic=time.time()
for i in range(100000000):
    c+=a[i]*b[i]
toc=time.time()
print(c)
print("vector"+str(1000*(toc-tic))+"ms")


# In[11]:


import numpy as np
v=np.array([1,2,3,4,5])
u=np.exp(v)
print(u)


# In[5]:


import numpy as np
a=np.random.randn(12288,150)
b=np.random.randn(150,45)
c=np.dot(a,b)
print(c.shape)


# In[6]:


a=np.random.randn(3,3)
b=np.random.randn(3,1)
c=a*b
print(c)


# In[9]:


a=np.random.randn(4,3)
b=np.random.randn(3,2)
c=a*b
print(c.shape)


# In[ ]:




