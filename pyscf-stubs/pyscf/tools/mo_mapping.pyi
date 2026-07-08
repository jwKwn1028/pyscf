from _typeshed import Incomplete
from pyscf import __config__ as __config__, gto as gto, lib as lib, lo as lo
from pyscf.lib import logger as logger
from numpy import int64, ndarray
from pyscf.gto.mole import Mole
from typing import Any, List, Tuple

BASE: Incomplete
MAP_TOL: Incomplete
ORTH_METHOD: Incomplete

def mo_map(mol1: Mole, mo1: ndarray, mol2: Mole, mo2: ndarray, base: int=..., tol: float = 0.5) -> Tuple[ndarray, ndarray]: ...
def mo_1to1map(s: ndarray) -> List[int64]: ...
def mo_comps(aolabels_or_baslst: List[Any], mol: Mole, mo_coeff: ndarray, cart: bool = False, orth_method: str=...) -> ndarray: ...
