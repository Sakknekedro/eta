#!/usr/bin/python3

from cmath import *
import sys

# fix values
u = 80+30j
f = 50
 
# given values
z_1 = 15+12.5j
z_2 = 15
z_3 = 10
z_4 = 10
z_l = 10+5j

# delta->star
summa = z_l+z_4+z_2
D_a=(z_l*z_2)/summa
D_b=(z_l*z_4)/summa
D_d=(z_4*z_2)/summa

# result impedance
z_a = z_1+D_a
z_b = z_3+D_b

z_cp = pow( (pow(z_a,-1)+pow(z_b,-1)) ,-1)

Z = z_cp+D_d

print('Z=',Z)

# from that the 
i = u/Z

print('i=',i)

z_1a = z_1+D_a
z_3d = z_3+D_d

u_d = i*D_d
u_p = u - u_d

i_o = u_p/z_1a
i_u = u_p/z_3d

print ('i_o=',i_o)
print ('i_u=',i_u)
print ('i_o+i_u=',i_o+i_u)

u_1 = i_o*z_1
u_3 = i_u*z_3

print ('u_1',u_1)
print ('u_3',u_3)
