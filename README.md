# Simulating 1-dimensional discrete time quantum walks
In this repository, you will find the code to run simulations of discrete-time quantum walks(DTQW) in Python. The software used to construct the quantum walk operators and states is QuTiP (version 4.6.2). Learn more about qutip by clicking [here](https://qutip.org/index.html). 

The concept of discrete time quantum walk is defined by incorporating the superposition principle in quantum mechanics in the idea of classical random walk. Consider a quantum walker who has a coin and is allowed to travel on a 1-D space lattice and the movement on this lattice is dependent on a coin toss that is performed iteratively. 

Mathematically, the state of the quantum walker is described by a vector belonging to a direct product Hilbert space, composed of a 2-dimensional Hilbert space(coin space), used to describe the state of the coin, and of a N-dimensional Hilbert space(position space) used for the discrete postion space which has N sites. The coin operation is carried out with a 2x2 rotation matrix defined on the coin space. After the "coin toss", a shift operation, defined on the composite Hilbert space, is performed on the state of the walker. 
If the state of the coin is 'head', then the walker shifts 1 step right on the lattice and if the coin state is 'tail', the walker shifts 1 step left. The 'head' and 'tail' states are taken to be the basis states of the 2-dimensional coin space. 

<p class='aligncenter'>
<img src='/Hadamard_walk.png' width = '50%' />
</p>

Since the coin state can always be in a superposition of the basis states, consequently, the position of the walker on the lattice evolves as a superposition of different sites on the 1-D lattice. This feature of the quantum walk results in a distribution muh different from that of the classical random walk. 

