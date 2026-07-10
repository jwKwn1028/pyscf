from _typeshed import Incomplete
from pyscf import __config__ as __config__, dft as dft, lib as lib, symm as symm
from pyscf.dft.rks import KohnShamDFT as KohnShamDFT
from pyscf.lib import logger as logger
from pyscf.tdscf import rhf as rhf, uhf as uhf
from numpy import ndarray
from pyscf.dft.uks import UKS
from pyscf.dft.uks_symm import SymAdaptedUKS
from pyscf.scf.uhf import UHF
from typing import Callable, List, Optional, Tuple, Union

class TDA(uhf.TDA):
    def Gradients(self): ...

class TDDFT(uhf.TDHF):
    Gradients: Incomplete
RPA = TDDFT
TDUKS = TDDFT

class CasidaTDDFT(TDDFT, TDA):
    get_init_guess: Incomplete
    get_precond: Incomplete
    def gen_vind(self, mf: Optional[Union[SymAdaptedUKS, UKS]]=None) -> Tuple[Callable, ndarray]: ...
    nstates: Incomplete
    e: Incomplete
    xy: Incomplete
    def kernel(self, x0: None=None, nstates: Optional[int]=None) -> Tuple[ndarray, List[Tuple[Tuple[ndarray, ndarray], Tuple[ndarray, ndarray]]]]: ...
TDDFTNoHybrid = CasidaTDDFT

class dRPA(TDDFTNoHybrid):
    def __init__(self, mf: Union[UKS, UHF], frozen: None=None) -> None: ...
TDH = dRPA

class dTDA(TDA):
    def __init__(self, mf: Union[UKS, UHF], frozen: None=None) -> None: ...

def tddft(mf: UKS, frozen: None=None) -> Union[TDDFT, CasidaTDDFT]: ...
