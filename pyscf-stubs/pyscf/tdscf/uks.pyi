from _typeshed import Incomplete
from pyscf import __config__ as __config__, dft as dft, lib as lib, symm as symm
from pyscf.dft.rks import KohnShamDFT as KohnShamDFT
from pyscf.lib import logger as logger
from pyscf.tdscf import rhf as rhf, uhf as uhf

class TDA(uhf.TDA):
    def Gradients(self): ...

class TDDFT(uhf.TDHF):
    Gradients: Incomplete
RPA = TDDFT
TDUKS = TDDFT

class CasidaTDDFT(TDDFT, TDA):
    get_init_guess: Incomplete
    get_precond: Incomplete
    def gen_vind(self, mf=None): ...
    nstates: Incomplete
    e: Incomplete
    xy: Incomplete
    def kernel(self, x0=None, nstates=None): ...
TDDFTNoHybrid = CasidaTDDFT

class dRPA(TDDFTNoHybrid):
    def __init__(self, mf, frozen=None) -> None: ...
TDH = dRPA

class dTDA(TDA):
    def __init__(self, mf, frozen=None) -> None: ...

def tddft(mf, frozen=None): ...
