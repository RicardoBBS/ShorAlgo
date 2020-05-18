<img src="https://raw.githubusercontent.com/Aurelien-Pelissier/IBMQ-Quantum-Computing/master/img/qiskit-heading.gif" width=300>


# Shor's Algorithm
I worked through the code from

https://github.com/Aurelien-Pelissier/IBMQ-Quantum-Programming

to understand the algorithm fully and refactored the code so it works with the updated Qiskit library (and also for readability).


The code avoids the complexity of a general controlled modular exponentiation by implementing the particular case where N = 15 and a = 7 and avoids using the inverse QFT circuit by using a period finding subroutine.


 I got as far as applying the Inverse Quantum Fourier Transform to a circuit with known phase, as I found the code written and explained in:

https://qiskit.org/textbook/ch-algorithms/quantum-phase-estimation.html

But was unable to apply the inverse QFT to the Particular modular exponentiation circuit of N=15 and a=7 that I had refactored.

## Usage
The main file is Shor.py, to change N edit the file (line 14). Run:
```
$ python Shor.py
```
The code should output to the terminal the results of the period finding subroutine and open windows with the schematics of the modular exponentiation circuit as it evolves in the routine.