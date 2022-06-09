#!/usr/bin/env python
# coding: utf-8

# In[27]:


def palindromestring(s):
    if len(s)<1:
        return True
    if s[0] == s[-1]:
        return palindromestring (s[1:-1])
    else:
        return False
    
a = str(input("Enter your string : "))

if palindromestring(a) == True:
    print("Yes! this is a palindrome string")
else:
    print("No! this is not a palindrome string")
    
b = str(input("Enter your string : "))
if palindromestring(b) == True:
    print("Yes! this is a palindrome string")
else:
    print("No! this is not a palindrome string")
    


# In[ ]:




