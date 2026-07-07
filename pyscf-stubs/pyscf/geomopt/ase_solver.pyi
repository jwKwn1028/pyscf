from _typeshed import Incomplete
from pyscf import lib as lib
from pyscf.lib import logger as logger
from pyscf.pbc import gto as gto
from pyscf.pbc.tools.pyscf_ase import PySCF as PySCF, pyscf_to_ase_atoms as pyscf_to_ase_atoms

def kernel(method, target=None, logfile=None, fmax: float = 0.05, max_steps: int = 100): ...

class GeometryOptimizer(lib.StreamObject):
    method: Incomplete
    converged: bool
    max_steps: int
    fmax: float
    target: Incomplete
    logfile: Incomplete
    def __init__(self, method) -> None: ...
    @property
    def max_cycle(self): ...
    @property
    def cell(self): ...
    @cell.setter
    def cell(self, x) -> None: ...
    @property
    def mol(self): ...
    @mol.setter
    def mol(self, x) -> None: ...
    def kernel(self): ...
    optimize = kernel
