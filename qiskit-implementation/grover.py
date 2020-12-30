import math
import tkinter
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (NavigationToolbar2Tk, FigureCanvasTkAgg)

from qiskit import Aer, QuantumCircuit, execute
from qiskit.visualization import circuit_drawer, plot_histogram

from Oracles import single_solution


class Grover:
    def __init__(self, nqubits, oracle, backend=Aer.get_backend('qasm_simulator'), shots=1024):
        self.n_qubits = nqubits
        self.oracle = oracle
        self.backend = backend
        self.shots = shots
        self._circuit = QuantumCircuit(self.n_qubits)

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
        root = tkinter.Tk()
        root.title(f"Grover Solver with oracle:{self.oracle.name}")
        root.geometry("500x500")

        fig = Figure(figsize=(5, 5), dpi=90)
        axes = fig.add_subplot(111)
        circuit_drawer(circuit=self._circuit, output='mpl', ax=axes)

        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack(expand=1)

        toolbar = NavigationToolbar2Tk(canvas, root)
        toolbar.update()

        root.mainloop()


def plotResults(count_dict):
    root = tkinter.Tk()
    root.title("Plotting the results of measurement.")
    root.geometry("500x500")
    fig = Figure(figsize=(5, 5), dpi=90)
    axes = fig.add_subplot(111)

    plot_histogram(data=count_dict, sort='desc', bar_labels=True, ax=axes)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(expand=1)

    root.mainloop()


def solve(search_number):
    oracle = None
    if search_number == 0:
        oracle = single_solution.Oracle0().getOracle()
    elif search_number == 1:
        oracle = single_solution.Oracle1().getOracle()

    g_circuit = Grover(nqubits=3, oracle=oracle)
    g_circuit.prepareState()
    g_circuit.getOracle()
    g_circuit.getAmplifier()

    for i in range(int(math.sqrt(search_number))):
        g_circuit.getOracle()
        g_circuit.getAmplifier()

    g_circuit.drawCircuit()
    plotResults(g_circuit.measureResults())


if __name__ == '__main__':
    solve(0)
