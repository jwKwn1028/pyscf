from _typeshed import Incomplete
from pyscf import __config__ as __config__, dft as dft, lib as lib, symm as symm
from pyscf.dft.rks import KohnShamDFT as KohnShamDFT
from pyscf.tdscf import ghf as ghf, rhf as rhf
from numpy import ndarray
from typing import Callable, List, Optional, Tuple

class TDA(ghf.TDA): ...
class TDDFT(ghf.TDHF): ...
RPA = TDDFT
TDGKS = TDDFT

class CasidaTDDFT(TDDFT, TDA):
    get_init_guess: Incomplete
    def gen_vind(self, mf: Optional[Incomplete]=None) -> Tuple[Callable, ndarray]: ...
    nstates: Incomplete
    e: Incomplete
    xy: Incomplete
    def kernel(self, x0: None=None, nstates: Optional[int]=None) -> Tuple[ndarray, List[Tuple[ndarray, ndarray]]]: ...
TDDFTNoHybrid = CasidaTDDFT

def tddft(mf: Incomplete, frozen: None=None) -> TDDFT: ...
