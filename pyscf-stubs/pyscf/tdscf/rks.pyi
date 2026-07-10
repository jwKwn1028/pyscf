from _typeshed import Incomplete
from pyscf import __config__ as __config__, dft as dft, lib as lib, symm as symm
from pyscf.dft.rks import RKS, KohnShamDFT as KohnShamDFT
from pyscf.lib import logger as logger
from pyscf.tdscf import rhf as rhf
from numpy import ndarray
from pyscf.dft.rks_symm import SymAdaptedRKS
from pyscf.scf.hf import RHF
from typing import Callable, List, Optional, Tuple, Union

class TDA(rhf.TDA):
    def Gradients(self): ...

class TDDFT(rhf.TDHF):
    Gradients: Incomplete
RPA = TDDFT
TDRKS = TDDFT

class CasidaTDDFT(TDDFT, TDA):
    get_init_guess: Incomplete
    get_precond: Incomplete
    def gen_vind(self, mf: Optional[Union[RKS, SymAdaptedRKS]]=None) -> Tuple[Callable, ndarray]: ...
    nstates: Incomplete
    e: Incomplete
    xy: Incomplete
    def kernel(self, x0: None=None, nstates: Optional[int]=None) -> Tuple[ndarray, List[Tuple[ndarray, ndarray]]]: ...
TDDFTNoHybrid = CasidaTDDFT

class dRPA(TDDFTNoHybrid):
    def __init__(self, mf: Union[RHF, RKS], frozen: None=None) -> None: ...
TDH = dRPA

class dTDA(TDA):
    def __init__(self, mf: Union[RHF, RKS], frozen: None=None) -> None: ...

def tddft(mf: RKS, frozen: None=None) -> Union[CasidaTDDFT, TDDFT]: ...
