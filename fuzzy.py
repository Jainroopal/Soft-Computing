#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 14:44:47 2018

@author: roopal
"""
# algebric addition of two fuzzy sets
A = {1:0.2, 2:0.3 , 3:0.4 , 4:0.5 , 5:0.8 , 6:0.7}
B = {1:0.3 , 2:0.4 , 3:0.5 ,4:0.9 , 5:0.6 , 6:0}

s = {1:0 , 2:0 , 3:0 , 4:0 , 5:0 , 6:0}
for i in range(1,7):
    s[i] = round((A[i] + B[i]) - (A[i]*B[i]),2)
print(s)

#%%
# algebric diffrence
A = {1:0.2, 2:0.3 , 3:0.4 , 4:0.5 , 5:0.8 , 6:0.7}
B = {1:0.3 , 2:0.4 , 3:0.5 ,4:0.9 , 5:0.6 , 6:0}
s = {1:0 , 2:0 , 3:0 , 4:0 , 5:0 , 6:0}
for i in range(1,7):
    s[i] = round((A[i] - B[i]),2)
print(s)

#%%
# cartision product
def cartision(x,y):
    s = {}
    for i in range(1,6):
        for j in range(1,6):
            s[i] = min(x[i],y[j])
            print( s[i])

x = {1:0.2, 2:0.3 , 3:0.4 , 4:0.5 , 5:0.8 , 6:0.7}
y = {1:0.3 , 2:0.4 , 3:0.5 ,4:0.9 , 5:0.6 , 6:0}            

#%%
#unioun 
A = {1:0.2, 2:0.3 , 3:0.4 , 4:0.5 , 5:0.8 , 6:0.7}
B = {1:0.3 , 2:0.4 , 3:0.5 ,4:0.9 , 5:0.6 , 6:0}
s = {1:0 , 2:0 , 3:0 , 4:0 , 5:0 , 6:0}
for i in range(1,7):
    s[i] = max(A[i], B[i])
print(s)

#%%
#intersection of a and b
A = {1:0.2, 2:0.3 , 3:0.4 , 4:0.5 , 5:0.8 , 6:0.7}
B = {1:0.3 , 2:0.4 , 3:0.5 ,4:0.9 , 5:0.6 , 6:0}
s = {1:0 , 2:0 , 3:0 , 4:0 , 5:0 , 6:0}
for i in range(1,7):
    s[i] = min(A[i], B[i])
print(s)
#%%
#compliment
A = {1:0.2, 2:0.3 , 3:0.4 , 4:0.5 , 5:0.8 , 6:0.7}
s = {1:0 , 2:0 , 3:0 , 4:0 , 5:0 , 6:0}
for i in range(1,7):
    s[i] = 1-A[i]
print(s)

#%%

#Triangular
import matplotlib.pyplot as plt
a = int(input("enter a value of a:"))
b = int(input("enter a value of b:"))
c = (a+b)/2
x_c = [a,c,b]
y_c = [0,1,0]
plt.plot(x_c , y_c)
plt.show()
print("Enter the value of x")
y=float(input())

if(y<=a):
    mem = 0
elif(y>a and y<=c):
    me = float(y-a)/float(c-a)

elif(y>m and y<b):
    me = float(b-y)/float(b-c)

else:
    mem = 0

print("Its membership function is ",me)

#%%
#trapizoidal
import matplotlib.pyplot as plt
a = int(input("enter a value of a:"))
b = int(input("enter a value of b:"))
c = int(input("enter a value of c:"))
d = int(input("enter a value of c:"))
x_c = [a,b,c,d]
y_c = [0,1,1,0]
plt.plot(x_c,y_c)
plt.show()

print("Enter the value of x :")
x=float(input())

if(x<a or x>d):
    mem = 0

elif(x>=a and x<=b):
    mem = float(x-a)/float(b-a)

elif(x>=c and x<=d):
    mem = float(d-x)/float(d-c)

else:
    mem = 1

print("Its membership function is ",mem)
#%%
#gaussion
import numpy as np
import matplotlib.pyplot as plt

def plot_gmf(mean,std):
    x = [i for i in range(int(mean)-50,int(mean)+50)]
    y = []

    for i in range(len(x)):
        y.append(float(np.exp(-(((i-mean)**2)/float(std**2)/2))))

    plt.plot(x,y)
    plt.show()

def gmf(x,mean,std):
    return float(np.exp(-(((x-mean)**2)/float(std**2)/2)))
#%%
#sigmoid
import numpy as np
import matplotlib.pyplot as plt

def plot_sigm(a,b):
    x = [i for i in range(-2,8)]
    y = []

    for i in range(-2,8):
        y.append(float((1 / (1 + np.exp(-float(a)*(float(i)-float(a)))))))

    plt.plot(x,y)
    plt.show()

def sigm(x,a,c):
    return float((1 / (1 + np.exp(-a*(x-a)))))
#%%



