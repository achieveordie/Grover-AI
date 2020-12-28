from pprint import pprint

from qiskit import IBMQ, Aer, QuantumCircuit, ClassicalRegister, QuantumRegister, execute
import qiskit
from Oracles import single_solution

n = 3
# grover_circuit = QuantumCircuit(n)
# grover_circuit = initialize_s(grover_circuit, [0, 1, 2])
# grover_circuit.append(oracle_ex3, [0, 1, 2])
# grover_circuit.append(diffuser(n), [0, 1, 2])
# grover_circuit.measure_all()
#
# backend = Aer.get_backend('qasm_simulator')
# counts = execute(grover_circuit, backend=backend, shots=1024).result().get_counts()
# pprint(counts, indent=4)


class Grover:
    def __init__(self, nqubits, oracle, backend=Aer.get_backend('qasm_simulator'), shots=1024):
        self.n_qubits = nqubits
        self.oracle = oracle
        self.backend = backend
        self.shots = shots
        self._circuit = qiskit.QuantumCircuit(self.n_qubits)

    def getOracle(self):
        self._circuit.append(self.oracle, [i for i in range(self.n_qubits)])

    def getAmplifier(self):
        qc = QuantumCircuit(self.n_qubits)
        for qubit in range(self.n_qubits):
            qc.h(qubit)
            qc.x(qubit)
        qc.h(self.n_qubits-1)
        qc.mct(list(range(self.n_qubits-1)), self.n_qubits-1)
        qc.h(self.n_qubits-1)
        for qubit in range(self.n_qubits):
            qc.x(qubit)
            qc.h(qubit)
        amp = qc.to_gate()
        amp.name = "AMP"
        self._circuit.append(amp, [i for i in range(self.n_qubits)])

    def prepareState(self):
        for qubit in range(self.n_qubits):
            self._circuit.h(qubit)

    def measureResults(self):
        self._circuit.measure_all()
        return execute(self._circuit, self.backend, shots=self.shots).result().get_counts()

    def drawCircuit(self):
        pass

    def plotResults(self):
        pass
