from _typeshed import Incomplete
from pyscf import __config__ as __config__, gto as gto, lib as lib, scf as scf
from pyscf.lib import logger as logger
from numpy import int64, ndarray
from pyscf.scf.rohf import ROHF
from pyscf.scf.uhf import UHF
from typing import Tuple, Union

THRESHOLD: Incomplete
MINAO: Incomplete
WITH_IAO: Incomplete
OPENSHELL_OPTION: Incomplete
CANONICALIZE: Incomplete

def kernel(mf: Union[UHF, ROHF], aolabels: str, threshold: float=..., minao: str=..., with_iao: bool=..., openshell_option: int=..., canonicalize: bool=..., ncore: int = 0, verbose: None=None) -> Tuple[int, int64, ndarray]: ...
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
    def __init__(self, mf: Union[UHF, ROHF], aolabels: str, threshold: float=..., minao: str=..., with_iao: bool=..., openshell_option: int=..., canonicalize: bool=..., ncore: int = 0, verbose: None=None) -> None: ...
    def dump_flags(self, verbose: None=None) -> "AVAS": ...
    def kernel(self) -> Tuple[int, int64, ndarray]: ...
