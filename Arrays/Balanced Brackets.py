
# coding: utf-8

# Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).
# For example, given the string "([])[]({})", you should return true.
# Given the string "([)]" or "((()", you should return false.

# In[44]:


def balanced(s):
    stack = []
    for char in s:
        if char in ['{','(','[']:
            stack.append(char)
            #print(stack[-1])
        else:  
            if not stack:
                return False
            if ((char == '}' and stack[-1] != '{') or (char == ']' and stack[-1] != '[') or (char == ')' and stack[-1] != '(')):
                return False

            stack.pop()
    
    return True
            


# In[45]:


string = "())(" 
balanced(string)

