import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint

from qiskit import IBMQ, Aer, QuantumCircuit, ClassicalRegister, QuantumRegister, execute
from qiskit.providers.ibmq import least_busy
import qiskit
from qiskit.visualization import plot_histogram

qc = QuantumCircuit(3)
qc.cz(0, 2)
qc.cz(1, 2)
oracle_ex3 = qc.to_gate()
oracle_ex3.name = "U$_\omega$"


def initialize_s(qc, qubits):
    for q in qubits:
        qc.h(q)
    return qc


def diffuser(nqubits):
    qc = QuantumCircuit(nqubits)
    for qubit in range(nqubits):
        qc.h(qubit)
    for qubit in range(nqubits):
        qc.x(qubit)
    qc.h(nqubits-1)
    qc.mct(list(range(nqubits-1)), nqubits-1)
    qc.h(nqubits-1)
    for qubit in range(nqubits):
        qc.x(qubit)
    for qubit in range(nqubits):
        qc.h(qubit)
    U_s = qc.to_gate()
    U_s.name = "U$_s$"
    return U_s


n = 3
grover_circuit = QuantumCircuit(n)
grover_circuit = initialize_s(grover_circuit, [0, 1, 2])
grover_circuit.append(oracle_ex3, [0, 1, 2])
grover_circuit.append(diffuser(n), [0, 1, 2])
grover_circuit.measure_all()

backend = Aer.get_backend('qasm_simulator')
counts = execute(grover_circuit, backend=backend, shots=1024).result().get_counts()
pprint(counts, indent=4)


class Grover:
    def __init__(self, nqubits):
        self._circuit = qiskit.QuantumCircuit(nqubits)

    def getOracle(self, oracle):
        pass

    def getAmplifier(self):
        pass

    def prepareState(self):
        pass

    def measureResults(self):
        pass

    def drawCircuit(self):
        pass

    def plotResults(self):
        pass
