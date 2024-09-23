#Ramli (1227030027)
import numpy as np
#menghitung jarak fokus lensa 1/f=(n-1)[1/R1 + 1/R2]
r1 = 22 #cm
r2 = 17.5 #cm
n = 1.5
R = (1/r1) + (1/r2)
f = 1/((n-1)*R)
print (" Jarak fokus lensa cara 1",f,"cm")

a = 1/ (( n - 1 ) * ( 1/r1 + 1/r2 ))
print (" Jarak fokus lensa cara 2",a,"cm")


