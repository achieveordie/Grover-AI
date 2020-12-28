# To have all single-solution oracle circuits.
from abc import ABC, abstractmethod
from qiskit import QuantumCircuit


class ThreeQubitsOracles(ABC):
    def __init__(self):
        self.n_qubits = 3
        self.oracle = QuantumCircuit(self.n_qubits)

    @abstractmethod
    def getOracle(self):
        pass


class Oracle0(ThreeQubitsOracles):
    def __init__(self):
        super(Oracle0, self).__init__()
        self.search_int = 0

    def getOracle(self):
        for qubit in range(self.n_qubits):
            self.oracle.x(qubit)
        self.oracle.h(self.n_qubits-1)
        self.oracle.ccx(0, 1, target_qubit=self.n_qubits-1)
        self.oracle.h(self.n_qubits-1)
        for qubit in range(self.n_qubits):
            self.oracle.x(qubit)

        oracle_gate = self.oracle.to_gate()
        oracle_gate.name = f"O({self.n_qubits})-{self.search_int}"
        return oracle_gate


class Oracle1(ThreeQubitsOracles):
    def __init__(self):
        super(Oracle1, self).__init__()
        self.search_int = 1

    def getOracle(self):
        for qubit in range(self.n_qubits-1):
            self.oracle.x(qubit)
        self.oracle.h(self.n_qubits-1)
        self.oracle.ccx([i for i in range(self.n_qubits-1)], self.n_qubits-1)
        self.oracle.h(self.n_qubits-1)
        for qubit in range(self.n_qubits-1):
            self.oracle.x(qubit)

        oracle_gate = self.oracle.to_gate()
        oracle_gate.name = f"O({self.n_qubits})-{self.search_int}"
        return oracle_gate


# grover_circuit.measure_all()
#
# backend = Aer.get_backend('qasm_simulator')
# counts = execute(grover_circuit, backend=backend, shots=1024).result().get_counts()
# pprint(counts, indent=4)
