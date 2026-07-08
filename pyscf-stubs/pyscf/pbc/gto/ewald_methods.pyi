from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.gto import mole as mole
from pyscf.lib import logger as logger
from pyscf.pbc import tools as tools
from numpy import float64, int64, ndarray
from pyscf.pbc.gto.cell import Cell
from typing import List, Optional, Tuple, Union

libpbc: Incomplete
INTERPOLATION_ORDER: Incomplete

def bspline(u: ndarray, ng: int64, n: int = 4, deriv: int = 0) -> Union[Tuple[ndarray, ndarray, List[ndarray]], Tuple[List[ndarray], ndarray, List[ndarray]]]: ...
def particle_mesh_ewald(cell: Cell, ew_eta: None=None, ew_cut: None=None, order: int=...) -> float64: ...
def particle_mesh_ewald_nuc_grad(cell: Cell, ew_eta: Optional[float64]=None, ew_cut: Optional[float64]=None, order: int=...) -> ndarray: ...
def ewald_nuc_grad(cell: Cell, ew_eta: None=None, ew_cut: None=None) -> ndarray: ...
