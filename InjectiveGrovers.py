#Creating ancillary qubits and using control X,Y,or Z gates allows
#for the sytem to remain in a superposition of possible states
#could have applications in materials science, creating a quantum program
#that finds a material with a specific property, and then using ancillary
#qubits to a distribution of different materials that have similar properties
#   ex. use a qubyte to manage temperature, and then use an ancillary qubit in 
#   superposition to put the temperature into a superposition to find materials
#   that work at a range of temperatures
from qiskit import *
qc = QuantumCircuit(3,2)

qc.h(2)#put the ancillary qubit in a superposition

for i in range(1):
    qc.h(0)
    qc.h(1)

    qc.barrier()
    #insert operator here, can use the third qubit to keep the system in a superposition of possible states
    qc.x(0)
    qc.cx(2,0)

    qc.cz(0,1)
    qc.barrier()

    qc.h(0)
    qc.h(1)
    qc.x(0)
    qc.x(1)

    qc.barrier()
    #insert operator here
    qc.x(0)
    qc.cx(2,0)

    qc.cz(0,1)
    qc.barrier()

    qc.x(0)
    qc.x(1)
    qc.h(0)
    qc.h(1)

qc.measure([0,1],[0,1])

print(qc)
sim_backend = BasicAer.get_backend('qasm_simulator')
job = execute(qc, sim_backend, shots=1000)
result = job.result()
print("results: ", result.get_counts(qc))