from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.lib import einsum as einsum, logger as logger
from pyscf.lib.parameters import LARGE_DENOM as LARGE_DENOM
from pyscf.pbc import scf as scf
from pyscf.pbc.mp import kmp2 as kmp2
from numpy import ndarray
from pyscf.lib.numpy_helper import NPArrayWithTag
from typing import List, Tuple

WITH_T2: Incomplete

def kernel(mp: "KsymAdaptedKMP2", mo_energy: List[ndarray], mo_coeff: List[ndarray], verbose: int=..., with_t2: bool=...) -> Tuple[NPArrayWithTag, None]: ...
def kernel_with_t2(mp, mo_energy, mo_coeff, verbose=..., with_t2=...): ...
def make_rdm1(mp: "KsymAdaptedKMP2", t2: None=None, kind: str = 'compact') -> List[ndarray]: ...
def make_t2_for_rdm1(mp: "KsymAdaptedKMP2") -> ndarray: ...

class KsymAdaptedKMP2(kmp2.KMP2):
    e_hf: Incomplete
    e_corr_ss: Incomplete
    e_corr_os: Incomplete
    e_corr: Incomplete
    def kernel(self, mo_energy: None=None, mo_coeff: None=None, with_t2: bool=...) -> Tuple[float, None]: ...
    make_rdm1 = make_rdm1
    def make_rdm2(self) -> None: ...
KRMP2 = KsymAdaptedKMP2
KMP2 = KsymAdaptedKMP2
