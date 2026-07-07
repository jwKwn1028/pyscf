from _typeshed import Incomplete
from pyscf import __config__ as __config__, gto as gto, lib as lib, scf as scf
from pyscf.lib import logger as logger

THRESHOLD: Incomplete
MINAO: Incomplete
WITH_IAO: Incomplete
OPENSHELL_OPTION: Incomplete
CANONICALIZE: Incomplete

def kernel(mf, aolabels, threshold=..., minao=..., with_iao=..., openshell_option=..., canonicalize=..., ncore: int = 0, verbose=None): ...
avas = kernel

class AVAS(lib.StreamObject):
    aolabels: Incomplete
    threshold: Incomplete
    minao: Incomplete
    with_iao: Incomplete
    openshell_option: Incomplete
    canonicalize: Incomplete
    ncore: Incomplete
    stdout: Incomplete
    verbose: Incomplete
    ncas: Incomplete
    nelecas: Incomplete
    mo_coeff: Incomplete
    occ_weights: Incomplete
    vir_weights: Incomplete
    def __init__(self, mf, aolabels, threshold=..., minao=..., with_iao=..., openshell_option=..., canonicalize=..., ncore: int = 0, verbose=None) -> None: ...
    def dump_flags(self, verbose=None): ...
    def kernel(self): ...
