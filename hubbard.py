import numpy as np
from scipy.sparse.linalg import eigsh
import openfermion as of

# parameters
nsites = 4 # per line
nqubits = 2 * nsites # each site has two spins
U = 2.0
J = -1.0 # negative by convention? 
mu = 0.5 * U

hubbard = of.fermi_hubbard(1, nsites, tunneling = -J, coulomb = U, chemical_potential = mu, periodic = False) # change to x = 2 from 1 for 2D
# Given particle_hole_symmetry = False, chemical_potential > U/2 indicates past half fill, where infinity is full.

H = of.get_sparse_operator(hubbard, nqubits)

# Lowest few eigenvalues
eval, evec = eigsh(H, k = 1, which = 'SA')
print(eval)
print(evec)







"""
## Trotterization

# One-body (hopping) terms
one_body_terms = []
for i in range(nqubits - 2):
    op = of.FermionOperator(((i, 1), (i + 2, 0)), coefficient = J)
    one_body_terms.append(op + of.hermitian_conjugated(op))

# Two-body (charge-charge) terms
two_body_terms = []
for i in range(0, nqubits, 2):
    term = of.FermionOperator(((i, 1), (i, 0), (i + 1, 1), (i + 1, 0)), coefficient = U)
    two_body_terms.append(term)

# Chemical potential (doping) terms
chem_terms = []
for i in range(nqubits):
    term = of.FermionOperator(((i, 1), (i, 0)), coefficient = -mu)
    chem_terms.append(term)

# Verify this produces the same Hamiltonian from OpenFermion.
assert sum(one_body_terms) + sum(two_body_terms) == hubbard 
"""