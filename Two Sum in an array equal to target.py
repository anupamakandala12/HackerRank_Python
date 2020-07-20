#!/usr/bin/env python
# coding: utf-8
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Given nums = [2, 7, 11, 15], target = 9
# In[1]:


def two_sum(nums,target):    
    for j in range(0,len(nums)-1):
        for k in range(j+1, len(nums)):
            if(nums[j]+nums[k]==target):
                break
    return(1)
            
nums = list(map(int, input( ).split()))
target=9
print(two_sum(nums,target))


# In[ ]:




