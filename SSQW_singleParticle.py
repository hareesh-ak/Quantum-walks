# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 19:09:10 2021

@author: Hareesh
"""

from QW_qutip import *


S_plus = tensor(Cproj_up,Shift_right) + tensor(Cproj_down,qeye(N))
S_minus = tensor(Cproj_up,qeye(N)) + tensor(Cproj_down,Shift_left)

theta1=0.
theta2=pi/20

a1=0.2
a2=0.2

def SSQW(rho_i,th1,th2,n):
    
    for i in range(n):
        W = S_plus*Coin_op(th2*np.exp(-a2*i))*S_minus*Coin_op(th1*np.exp(-a1*i))
        rho_i = W*(rho_i*W.dag())
    return rho_i

if __name__ =="__main__":
    r = SSQW(rho_i,theta1,theta2,steps)
    #r=QW(rho_i,steps)
    y = Measure_pos(r)
    plt.plot(X[::1],y[::1])
    print(sum(y))
