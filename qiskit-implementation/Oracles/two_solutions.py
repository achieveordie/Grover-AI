"""
For Three-qubit oracles, cases where two solution is possible 0,0 to 7,7 giving (8x7)/2 = 28 oracles.
These oracles are pre-written which just showcases how it turns ugly-long really quick. Via this we also find
motivation to write an implementation for general case (NSFW - Not So Fun Way) which uses an algorithmic approach by
creating matrices rather than complete circuits. NSFW isn't fun, so we finally create a ML-model to do the same.
"""
from abc import ABC, abstractmethod
from qiskit import QuantumCircuit


class ThreeQubitsOracles(ABC):
    def __init__(self):
        self.n_qubits = 3
        self.oracle = QuantumCircuit(self.n_qubits)

    @abstractmethod
    def getOracle(self):
        pass


class Oracle01(ThreeQubitsOracles):
    def __init__(self):
        super(Oracle01, self).__init__()
        self.search_int1 = 0
        self.search_int2 = 1

    def getOracle(self):
        for qubit in range(self.n_qubits-1):
            self.oracle.z(qubit)
        self.oracle.cz(control_qubit=0, target_qubit=1)

        oracle_gate = self.oracle.to_gate()
        oracle_gate.name = f"0({self.n_qubits}-{self.search_int1}&{self.search_int2})"
        return oracle_gate


class Oracle02(ThreeQubitsOracles):
    def __init__(self):
        super(Oracle02, self).__init__()
        self.search_int1 = 0
        self.search_int2 = 2

    def getOracle(self):
        self.oracle.z(0)
        self.oracle.z(2)
        self.oracle.cz(control_qubit=0, target_qubit=2)

        oracle_gate = self.oracle.to_gate()
        oracle_gate.name = f"0({self.n_qubits}-{self.search_int1}&{self.search_int2})"
        return oracle_gate


class Oracle03(ThreeQubitsOracles):
    def __init__(self):
        super(Oracle03, self).__init__()
        self.search_int1 = 0
        self.search_int2 = 1

    def getOracle(self):
        for qubit in range(self.n_qubits):
            self.oracle.z(qubit)
        self.oracle.cz(control_qubit=0, target_qubit=1)
        self.oracle.cz(control_qubit=0, target_qubit=2)

        oracle_gate = self.oracle.to_gate()
        oracle_gate.name = f"0({self.n_qubits}-{self.search_int1}&{self.search_int2})"
        return oracle_gate


class Oracle04(ThreeQubitsOracles):
    def __init__(self):
        super(Oracle04, self).__init__()
        self.search_int1 = 0
        self.search_int2 = 1

    def getOracle(self):
        self.oracle.z(1)
        self.oracle.z(2)
        self.oracle.cz(1, 2)

        oracle_gate = self.oracle.to_gate()
        oracle_gate.name = f"0({self.n_qubits}-{self.search_int1}&{self.search_int2})"
        return oracle_gate


class Oracle05(ThreeQubitsOracles):
    def __init__(self):
        super(Oracle05, self).__init__()
        self.search_int1 = 0
        self.search_int2 = 1

    def getOracle(self):
        for qubit in range(self.n_qubits):
            self.oracle.z(qubit)
        self.oracle.cz(control_qubit=0, target_qubit=1)
        self.oracle.cz(control_qubit=1, target_qubit=2)

        oracle_gate = self.oracle.to_gate()
        oracle_gate.name = f"0({self.n_qubits}-{self.search_int1}&{self.search_int2})"
        return oracle_gate


class Oracle06(ThreeQubitsOracles):
    def __init__(self):
        super(Oracle06, self).__init__()
        self.search_int1 = 0
        self.search_int2 = 1

    def getOracle(self):
        for qubit in range(self.n_qubits):
            self.oracle.z(qubit)
        self.oracle.cz(control_qubit=0, target_qubit=2)
        self.oracle.cz(control_qubit=1, target_qubit=2)

        oracle_gate = self.oracle.to_gate()
        oracle_gate.name = f"0({self.n_qubits}-{self.search_int1}&{self.search_int2})"
        return oracle_gate


class Oracle07(ThreeQubitsOracles):
    def __init__(self):
        super(Oracle07, self).__init__()
        self.search_int1 = 0
        self.search_int2 = 1

    def getOracle(self):
        for qubit in range(self.n_qubits):
            self.oracle.z(qubit)
        self.oracle.cz(control_qubit=0, target_qubit=1)
        self.oracle.cz(control_qubit=0, target_qubit=2)
        self.oracle.cz(control_qubit=1, target_qubit=2)

        oracle_gate = self.oracle.to_gate()
        oracle_gate.name = f"0({self.n_qubits}-{self.search_int1}&{self.search_int2})"
        return oracle_gate


class Oracle12(ThreeQubitsOracles):
    def __init__(self):
        super(Oracle12, self).__init__()
        self.search_int1 = 1
        self.search_int2 = 2

    def getOracle(self):
        self.oracle.z(1)
        self.oracle.z(2)
        self.oracle.cz(control_qubit=0, target_qubit=1)
        self.oracle.cz(control_qubit=0, target_qubit=2)

        oracle_gate = self.oracle.to_gate()
        oracle_gate.name = f"0({self.n_qubits}-{self.search_int1}&{self.search_int2})"
        return oracle_gate


class Oracle13(ThreeQubitsOracles):
    def __init__(self):
        super(Oracle13, self).__init__()
        self.search_int1 = 1
        self.search_int2 = 3

    def getOracle(self):
        self.oracle.z(2)
        self.oracle.cz(control_qubit=0, target_qubit=2)

        oracle_gate = self.oracle.to_gate()
        oracle_gate.name = f"0({self.n_qubits}-{self.search_int1}&{self.search_int2})"
        return oracle_gate


class Oracle14(ThreeQubitsOracles):
    def __init__(self):
        super(Oracle14, self).__init__()
        self.search_int1 = 1
        self.search_int2 = 4

    def getOracle(self):
        self.oracle.z(0)
        self.oracle.z(2)
        self.oracle.cz(control_qubit=0, target_qubit=1)
        self.oracle.cz(control_qubit=1, target_qubit=2)

        oracle_gate = self.oracle.to_gate()
        oracle_gate.name = f"0({self.n_qubits}-{self.search_int1}&{self.search_int2})"
        return oracle_gate


class Oracle15(ThreeQubitsOracles):
    def __init__(self):
        super(Oracle15, self).__init__()
        self.search_int1 = 1
        self.search_int2 = 5

    def getOracle(self):
        self.oracle.z(2)
        self.oracle.cz(control_qubit=1, target_qubit=2)

        oracle_gate = self.oracle.to_gate()
        oracle_gate.name = f"0({self.n_qubits}-{self.search_int1}&{self.search_int2})"
        return oracle_gate


class Oracle16(ThreeQubitsOracles):
    def __init__(self):
        super(Oracle16, self).__init__()
        self.search_int1 = 1
        self.search_int2 = 6

    def getOracle(self):
        self.oracle.z(2)
        self.oracle.barrier()
        self.oracle.cz(control_qubit=0, target_qubit=1)
        self.oracle.cz(control_qubit=0, target_qubit=2)
        self.oracle.cz(control_qubit=1, target_qubit=2)

        oracle_gate = self.oracle.to_gate()
        oracle_gate.name = f"0({self.n_qubits}-{self.search_int1}&{self.search_int2})"
        return oracle_gate


class Oracle17(ThreeQubitsOracles):
    def __init__(self):
        super(Oracle17, self).__init__()
        self.search_int1 = 1
        self.search_int2 = 7

    def getOracle(self):
        self.oracle.z(2)
        self.oracle.cz(control_qubit=0, target_qubit=2)
        self.oracle.cz(control_qubit=1, target_qubit=2)

        oracle_gate = self.oracle.to_gate()
        oracle_gate.name = f"0({self.n_qubits}-{self.search_int1}&{self.search_int2})"
        return oracle_gate


class Oracle23(ThreeQubitsOracles):
    def __init__(self):
        super(Oracle23, self).__init__()
        self.search_int1 = 2
        self.search_int2 = 3

    def getOracle(self):
        self.oracle.z(1)
        self.oracle.cz(control_qubit=0, target_qubit=1)

        oracle_gate = self.oracle.to_gate()
        oracle_gate.name = f"0({self.n_qubits}-{self.search_int1}&{self.search_int2})"
        return oracle_gate


class Oracle24(ThreeQubitsOracles):
    def __init__(self):
        super(Oracle24, self).__init__()
        self.search_int1 = 2
        self.search_int2 = 4

    def getOracle(self):
        self.oracle.z(0)
        self.oracle.z(1)
        self.oracle.cz(control_qubit=0, target_qubit=2)
        self.oracle.cz(control_qubit=1, target_qubit=2)

        oracle_gate = self.oracle.to_gate()
        oracle_gate.name = f"0({self.n_qubits}-{self.search_int1}&{self.search_int2})"
        return oracle_gate


class Oracle25(ThreeQubitsOracles):
    def __init__(self):
        super(Oracle25, self).__init__()
        self.search_int1 = 2
        self.search_int2 = 5

    def getOracle(self):
        self.oracle.z(1)
        self.oracle.cz(control_qubit=0, target_qubit=1)
        self.oracle.cz(control_qubit=0, target_qubit=2)
        self.oracle.cz(control_qubit=1, target_qubit=2)

        oracle_gate = self.oracle.to_gate()
        oracle_gate.name = f"0({self.n_qubits}-{self.search_int1}&{self.search_int2})"
        return oracle_gate


class Oracle26(ThreeQubitsOracles):
    def __init__(self):
        super(Oracle26, self).__init__()
        self.search_int1 = 2
        self.search_int2 = 6

    def getOracle(self):
        self.oracle.z(1)
        self.oracle.cz(control_qubit=1, target_qubit=2)

        oracle_gate = self.oracle.to_gate()
        oracle_gate.name = f"0({self.n_qubits}-{self.search_int1}&{self.search_int2})"
        return oracle_gate


class Oracle27(ThreeQubitsOracles):
    def __init__(self):
        super(Oracle27, self).__init__()
        self.search_int1 = 2
        self.search_int2 = 7

    def getOracle(self):
        self.oracle.z(1)
        self.oracle.cz(control_qubit=0, target_qubit=1)
        self.oracle.cz(control_qubit=1, target_qubit=2)

        oracle_gate = self.oracle.to_gate()
        oracle_gate.name = f"0({self.n_qubits}-{self.search_int1}&{self.search_int2})"
        return oracle_gate


class Oracle34(ThreeQubitsOracles):
    def __init__(self):
        super(Oracle34, self).__init__()
        self.search_int1 = 3
        self.search_int2 = 4

    def getOracle(self):
        self.oracle.z(0)
        self.oracle.cz(control_qubit=0, target_qubit=1)
        self.oracle.cz(control_qubit=0, target_qubit=2)
        self.oracle.cz(control_qubit=1, target_qubit=2)

        oracle_gate = self.oracle.to_gate()
        oracle_gate.name = f"0({self.n_qubits}-{self.search_int1}&{self.search_int2})"
        return oracle_gate


class Oracle35(ThreeQubitsOracles):
    def __init__(self):
        super(Oracle35, self).__init__()
        self.search_int1 = 3
        self.search_int2 = 5

    def getOracle(self):
        self.oracle.cz(control_qubit=0, target_qubit=2)
        self.oracle.cz(control_qubit=1, target_qubit=2)

        oracle_gate = self.oracle.to_gate()
        oracle_gate.name = f"0({self.n_qubits}-{self.search_int1}&{self.search_int2})"
        return oracle_gate


class Oracle36(ThreeQubitsOracles):
    def __init__(self):
        super(Oracle36, self).__init__()
        self.search_int1 = 3
        self.search_int2 = 6

    def getOracle(self):
        self.oracle.cz(control_qubit=0, target_qubit=1)
        self.oracle.cz(control_qubit=1, target_qubit=2)

        oracle_gate = self.oracle.to_gate()
        oracle_gate.name = f"0({self.n_qubits}-{self.search_int1}&{self.search_int2})"
        return oracle_gate


class Oracle37(ThreeQubitsOracles):
    def __init__(self):
        super(Oracle37, self).__init__()
        self.search_int1 = 3
        self.search_int2 = 7

    def getOracle(self):
        self.oracle.cz(control_qubit=1, target_qubit=2)

        oracle_gate = self.oracle.to_gate()
        oracle_gate.name = f"0({self.n_qubits}-{self.search_int1}&{self.search_int2})"
        return oracle_gate


class Oracle45(ThreeQubitsOracles):
    def __init__(self):
        super(Oracle45, self).__init__()
        self.search_int1 = 4
        self.search_int2 = 5

    def getOracle(self):
        self.oracle.z(1)
        self.oracle.cz(control_qubit=0, target_qubit=1)

        oracle_gate = self.oracle.to_gate()
        oracle_gate.name = f"0({self.n_qubits}-{self.search_int1}&{self.search_int2})"
        return oracle_gate


class Oracle46(ThreeQubitsOracles):
    def __init__(self):
        super(Oracle46, self).__init__()
        self.search_int1 = 4
        self.search_int2 = 6

    def getOracle(self):
        self.oracle.z(1)
        self.oracle.cz(control_qubit=0, target_qubit=2)

        oracle_gate = self.oracle.to_gate()
        oracle_gate.name = f"0({self.n_qubits}-{self.search_int1}&{self.search_int2})"
        return oracle_gate


class Oracle47(ThreeQubitsOracles):
    def __init__(self):
        super(Oracle47, self).__init__()
        self.search_int1 = 4
        self.search_int2 = 7

    def getOracle(self):
        self.oracle.z(1)
        self.oracle.cz(control_qubit=0, target_qubit=1)
        self.oracle.cz(control_qubit=0, target_qubit=2)

        oracle_gate = self.oracle.to_gate()
        oracle_gate.name = f"0({self.n_qubits}-{self.search_int1}&{self.search_int2})"
        return oracle_gate


class Oracle56(ThreeQubitsOracles):
    def __init__(self):
        super(Oracle56, self).__init__()
        self.search_int1 = 5
        self.search_int2 = 6

    def getOracle(self):
        self.oracle.cz(control_qubit=0, target_qubit=1)
        self.oracle.cz(control_qubit=0, target_qubit=2)

        oracle_gate = self.oracle.to_gate()
        oracle_gate.name = f"0({self.n_qubits}-{self.search_int1}&{self.search_int2})"
        return oracle_gate


class Oracle57(ThreeQubitsOracles):
    def __init__(self):
        super(Oracle57, self).__init__()
        self.search_int1 = 5
        self.search_int2 = 7

    def getOracle(self):
        self.oracle.cz(control_qubit=0, target_qubit=2)

        oracle_gate = self.oracle.to_gate()
        oracle_gate.name = f"0({self.n_qubits}-{self.search_int1}&{self.search_int2})"
        return oracle_gate


class Oracle67(ThreeQubitsOracles):
    def __init__(self):
        super(Oracle67, self).__init__()
        self.search_int1 = 6
        self.search_int2 = 7

    def getOracle(self):
        self.oracle.cz(control_qubit=0, target_qubit=1)

        oracle_gate = self.oracle.to_gate()
        oracle_gate.name = f"0({self.n_qubits}-{self.search_int1}&{self.search_int2})"
        return oracle_gate
