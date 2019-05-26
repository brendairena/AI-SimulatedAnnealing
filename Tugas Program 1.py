import math
import random
from random import uniform


def func(x1,x2): 
    return -1 * (math.sin(x1)*math.cos(x2) + (4/5)*math.exp(1 - math.sqrt(x1*x1 + x2*x2)))

def value(koordinat):
    return func(koordinat[0],koordinat[1])

def prob(n_minimum, c_minimum, temp):   # n = new; c = current
    dt = n_minimum - c_minimum          # dt = delta_e
    return math.exp(-(dt)/temp)         # temp = temperature

step   = 0.9999
temp   = 100
f_temp = 0.1

x1 = uniform(-10,10)
x2 = uniform(-10,10)

c_koordinat = [x1,x2]
c_minimum   = value(c_koordinat)
b_minimum   = c_minimum                   # b = best
b_koordinat = c_koordinat

print("----------------------------------------------------------------------") 
print("                 TUGAS PROGRAM 1 KECERDASAN BUATAN                    ")
print("               BRENDA IRENA - IFIK 40 03 - 1301164641                 ")
print("----------------------------------------------------------------------")

# i=0
# for i in range(100):
while (temp > f_temp):
    x1 = uniform(-10,10)
    x2 = uniform(-10,10)
    n_koordinat = [x1,x2]
    n_minimum   = value(n_koordinat)
    
    if (n_minimum < c_minimum):
        c_minimum   = n_minimum
        c_koordinat = n_koordinat
        
        if (c_minimum < b_minimum):
            b_minimum   = c_minimum
            b_koordinat = c_koordinat
            
            print(b_minimum, b_koordinat)
           
    else:
        p = prob(n_minimum, c_minimum, temp)
        if (p > random.uniform(0,1)):
            c_minimum   = n_minimum
            c_koordinat = n_koordinat
    
    temp = temp * step
   
print("----------------------------------------------------------------------")
print("                            HASIL AKHIR                               ")
print("----------------------------------------------------------------------")
print("Nilai minimum fungsi    : ",b_minimum)
print("Pada koordinat [x1, x2] : ",b_koordinat)