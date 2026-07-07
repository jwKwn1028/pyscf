from _typeshed import Incomplete
from pyscf import __config__ as __config__, gto as gto, lib as lib, lo as lo
from pyscf.lib import logger as logger

BASE: Incomplete
MAP_TOL: Incomplete
ORTH_METHOD: Incomplete

def mo_map(mol1, mo1, mol2, mo2, base=..., tol: float = 0.5): ...
def mo_1to1map(s): ...
def mo_comps(aolabels_or_baslst, mol, mo_coeff, cart: bool = False, orth_method=...): ...
