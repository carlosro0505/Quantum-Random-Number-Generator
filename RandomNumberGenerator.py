#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from qiskit import *
from qiskit import BasicAer, execute
from collections import Counter

n = input("Enter a number to calculate a random number between 0 and 2^(input)-1 \n(keep in mind that the highest digit you can enter is 24): ")
res = str(2 ** int(n) - 1)
print("Random number range: 0 to ", res)
q = QuantumRegister(int(n))
c = ClassicalRegister(int(n))
# used to generate an equally weighted superposition of 0 and 1 to get a random bit using hadamard
circ = QuantumCircuit(q, c)

for j in range(int(n)):
    circ.h(q[j])
    
circ.measure(q,c)

job = execute(circ, BasicAer.get_backend('qasm_simulator'), shots=8192)

bit_counts = job.result().get_counts()
int_counts = {}
# converts them into integers
for bitstring in bit_counts:
    int_counts[int(bitstring,2)] = bit_counts[bitstring]
    
def most_common_element(arr):
    # use Counter to count occurrences of each element in the array
    counter = Counter(arr)
    
    # find the most common element and its count
    most_common, count = counter.most_common(1)[0]

    return most_common

result = most_common_element(int_counts)
print("Random number: ", result)




# In[4]:





# In[ ]:




