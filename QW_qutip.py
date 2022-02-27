# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 11:37:44 2021

@author: Hareesh
"""

from qutip import *
import numpy as np
import matplotlib.pyplot as plt
pi=np.pi


# Function defined to return matrix for Coin toss operation.
def B(theta):
    b= np.array([[np.cos(theta) , 1j*np.sin(theta)],
                 [1j*np.sin(theta), np.cos(theta)]],dtype=complex)
    return b

"""
The parameters given below characterise the nature of the 
probability distribution of quantum walker's position after N steps

th0 --> fixes the matrix used to simulate the coin toss operation.
steps --> number of iterations for which the quantum walk operations are applied.
a --> acceleration parameter; when initialized as non-zero, it results in accelerated quantum walk
sites --> number of lattice points in which the quantum walker is allowed to travel 
"""
th0=pi/4    
steps=50
a=0.0
sites=2*steps+1
N=sites


X = [-steps+i for i in range(N)]  # Array containing the lattice sites labelled as -N/2 to N/2

Up = Qobj([[1],[0]])  # Spin up state / 'Heads' state
Down = Qobj([[0],[1]])  # Spin down state / 'Tails' state

Pos_gen =lambda k : basis(N,int(N/2)-k) # Generates the basis vector for position k in standard basis form

Pos_i = Pos_gen(0)  # initial position of walker at site '0'
Coin_i = 2**-0.5*(Up-1*Down) # initial coin state 

# Initial composite state and the corresponding density matrix defined below
psi_i = tensor(Coin_i,Pos_i)
rho_i = ket2dm(psi_i)

#  projection operators for the basis states defined on coin space
Cproj_up = ket2dm(Up) 
Cproj_down = ket2dm(Down)

#  right and left position shift operators
Shift_right = Qobj(np.eye(N,k=1))
Shift_left = Qobj(np.eye(N,k=-1))

#  position dependent conditional shift operator
S = tensor(Cproj_up,Shift_right) + tensor(Cproj_down,Shift_left)

# Coin toss operator defined on the composite hilbert space
Coin_op = lambda theta : tensor(Qobj(B(theta)),qeye(N))


def QW(rho_init, n):
    """
    input: inital density matrix of the composite system, number of steps of the walk  
    output: final density matrix after n steps of the walk
    """
    for t in range(n):
        W = S*Coin_op(th0*np.exp(-a*t))
        rho_init = W*(rho_init*W.dag())
    return rho_init

def Measure_pos(rho):
    """
    input: density matrix for the composite state
    output: probability distribution of finding the walker in the position space
    """
    p=[]
    for i in range(N):
        projector = tensor(qeye(2),ket2dm(basis(N,i)))
        p.append((rho*projector).tr())
    return p


if __name__ =="__main__":
    r = QW(rho_i,steps)
    y = Measure_pos(r)
    plt.plot(X,y,label=f'$\\theta=$ {th0}')
    plt.legend()
    plt.ylabel('Probability amplitude',fontsize=20)
    plt.xlabel('Position space',fontsize=20)
    plt.title(f' 1-D DTQW for $\\theta =$ {th0} ',fontsize=20)
    print(sum(y)) # Used to check if the probabilities are conserved (should print 1)

    
