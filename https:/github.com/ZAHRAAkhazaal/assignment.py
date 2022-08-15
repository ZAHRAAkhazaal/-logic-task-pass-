# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 20:42:52 2022

@author: asus
"""

#Q1:
String_one="python"
removed=String_one.replace('p'," ")
print(removed)
print('---------------end of Q1----------')
#Q2:
x=11

for i in range (2,x):
    
    if ((x % i) == 0): 
       
        
        print('n0')
        break
    else:
         
         print('prime')
print('------end of Q2')
#Q3
def ff (x,s):
     j=0
     for i in range (len(x)):
        
        
        if (x[i] == s):
            j+=1
        else:
         print(j)
    
     return j 
        
        
ff('banana','a')
print('------end of Q3')


