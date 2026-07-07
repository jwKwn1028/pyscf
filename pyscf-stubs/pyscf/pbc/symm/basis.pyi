from pyscf.pbc.symm import symmetry as symmetry
from pyscf.pbc.symm.group import PGElement as PGElement, PointGroup as PointGroup

def symm_adapted_basis(cell, kpts, tol: float = 1e-09): ...
