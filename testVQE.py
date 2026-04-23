import numpy as np
from qiskit.circuit.library import EfficientSU2
from qiskit.quantum_info import SparsePauliOp
from qiskit_algorithms import VQE
from qiskit_algorithms.optimizers import SLSQP
from qiskit.primitives import StatevectorEstimator


hamiltonian = SparsePauliOp.from_list([("ZZ", 1.0)])

ansatz = EfficientSU2(num_qubits=2, reps=1, entanglement='linear')

estimator = StatevectorEstimator()
optimizer = SLSQP(maxiter=100)

vqe = VQE(estimator, ansatz, optimizer)
result = vqe.compute_minimum_eigenvalue(operator=hamiltonian)

print(f"VQE Eigenvalue: {result.eigenvalue.real:.5f}")
print(f"Optimal Parameters: {result.optimal_point}")
