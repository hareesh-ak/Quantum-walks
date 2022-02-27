# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 11:37:44 2021

@author: Hareesh
"""

from qutip import *
import numpy as np
import matplotlib.pyplot as plt
pi=np.pi



def B(theta):
    b= np.array([[np.cos(theta) , 1j*np.sin(theta)],
                 [1j*np.sin(theta), np.cos(theta)]],dtype=complex)
    return b


th0=pi/4
steps=50
a=0.0
sites=2*steps+1

N=sites

X = [-steps+i for i in range(N)]

Up = Qobj([[1],[0]])
Down = Qobj([[0],[1]])

Pos_gen =lambda k : basis(N,int(N/2)-k)

Pos_i = Pos_gen(0)#*0.5**0.5 + basis(N,int(N/2)+2)*0.5**0.5
Coin_i = 2**-0.5*(Up-1*Down)


psi_i = tensor(Coin_i,Pos_i)
rho_i = ket2dm(psi_i)

Cproj_up = ket2dm(Up)
Cproj_down = ket2dm(Down)

Shift_right = Qobj(np.eye(N,k=1))
Shift_left = Qobj(np.eye(N,k=-1))

S = tensor(Cproj_up,Shift_right) + tensor(Cproj_down,Shift_left)

Coin_op = lambda theta : tensor(Qobj(B(theta)),qeye(N))

def QW(rho_init, n):
    for t in range(n):
        W = S*Coin_op(th0*np.exp(-a*t))
        rho_init = W*(rho_init*W.dag())
    return rho_init

def Measure_pos(rho):
    p=[]
    for i in range(N):
        projector = tensor(qeye(2),ket2dm(basis(N,i)))
        p.append((rho*projector).tr())
    return p


if __name__ =="__main__":
    r = QW(rho_i,steps)
    y = Measure_pos(r)
    plt.plot(X,y,label='$\\theta = 0$')
    plt.legend()
    plt.ylabel('Probability amplitude',fontsize=20)
    plt.xlabel('Position space',fontsize=20)
    plt.title(' Maximum spread ',fontsize=20)
    print(sum(y))

    
