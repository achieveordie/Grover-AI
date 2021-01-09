"""
This is the N(ot) S(o) F(un) W(ay) to create oracle. We have been creating circuits whose matrix essentially attaches
a factor of -1 corresponding to the solution while others remain 1, after all that was the whole essence of having an
oracle which flips the phase of the searched element in the superposition.
"""
from qiskit.circuit.library import Diagonal


class OracleNSFW:
    def __init__(self, search):
        self.n_qubits = 1
        if type(search) == int:
            self.search_int = search
            while 2**self.n_qubits < search:
                self.n_qubits += 1
        elif type(search) in (list, tuple):
            self.search_int = tuple(search)
            max_int = max(self.search_int)
            while 2**self.n_qubits < max_int:
                self.n_qubits += 1
        self.elements = [1 for _ in range(2 ** self.n_qubits)]

    def getOracle(self):
        if type(self.search_int) == int:
            self.elements[self.search_int-1] = -1
            oracle_gate = Diagonal(self.elements)
            oracle_gate.name = f"O({self.n_qubits}-{self.search_int})"
            return oracle_gate
        elif type(self.search_int) == tuple:
            for element in self.search_int:
                self.elements[element-1] = -1
            oracle_gate = Diagonal(self.elements)
            oracle_gate.name = f"O({self.n_qubits}-MUL)"
            return oracle_gate
