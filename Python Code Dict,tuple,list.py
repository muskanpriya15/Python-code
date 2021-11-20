#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = [2,4,6,8,10]


# In[2]:


print(a)


# In[3]:


type(a)


# In[4]:


a[0]*a[1]*a[2]*a[3]*a[4]


# In[5]:


b = [20,100,60,50,5,12]


# In[6]:


b


# In[7]:


b.sort()


# In[8]:


b


# In[9]:


b.pop()


# In[10]:


b = [20,100,60,50,5,12]
b.sort()
b.pop()


# In[12]:


b = [20,100,60,50,5,12]
b.sort()
b.reverse()
b.pop()


# In[13]:


c = []


# In[14]:


print(c)


# In[15]:


type(c)


# In[19]:


a = [2,4,6,8,10]
b = [4,100,60,50,2]
for i in range(a):
    if(a.index==b.index):
        print("True")


# In[23]:


a = [2,4,6,8,10,12,14,16,18,20]
a.pop(0)
a.pop(3)
a.pop(3)
print(a)


# In[68]:


dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4={
    'out':[dic1,dic2,dic3]
}
dic4.values()
print(dic4)


# In[69]:


a = (1,'Ram',True,False,55.5)


# In[70]:


print(a)


# In[71]:


type(a)


# In[72]:


a = (2,6.5,5,60,50,45,46,5,4)


# In[73]:


a


# In[74]:


type(a)


# In[82]:


a[1]


# In[83]:


a = (1,1.5,'Ram',True,False,34)


# In[84]:


a


# In[85]:


type(a)


# In[90]:


a = ('Ram')


# In[91]:


a


# In[92]:


type(a)


# In[93]:


a = (1,2,3,4,5,6,7,8,9,10)


# In[94]:


a


# In[95]:


type(a)


# In[101]:


a[4],a[-4]


# In[108]:


a=[1,2,3,4,5,6,7,8,9,10]
a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+a[8]+a[9]


# In[107]:


a = (8, 2, 3, -1, 7)
a[0]*a[1]*a[2]*a[3]*a[4]


# In[111]:


a = print(input("Enter the table you want to print"))
for i in range(a):
    print(i)
    i=i*2


# In[ ]:




