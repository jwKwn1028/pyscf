from pyscf.pbc.symm import symmetry as symmetry
from pyscf.pbc.symm.group import PointGroup, PGElement as PGElement, PointGroup as PointGroup
from numpy import ndarray
from pyscf.pbc.gto.cell import Cell
from pyscf.pbc.lib.kpts import KPoints
from pyscf.pbc.symm.space_group import SPGElement
from typing import List, Tuple

def symm_adapted_basis(cell: Cell, kpts: KPoints, tol: float = 1e-09) -> Tuple[List[List[ndarray]], List[List[int]]]: ...
