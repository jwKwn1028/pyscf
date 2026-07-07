from _typeshed import Incomplete
from pyscf import __config__ as __config__, dft as dft, lib as lib, symm as symm
from pyscf.dft.rks import KohnShamDFT as KohnShamDFT
from pyscf.tdscf import ghf as ghf, rhf as rhf

class TDA(ghf.TDA): ...
class TDDFT(ghf.TDHF): ...
RPA = TDDFT
TDGKS = TDDFT

class CasidaTDDFT(TDDFT, TDA):
    get_init_guess: Incomplete
    def gen_vind(self, mf=None): ...
    nstates: Incomplete
    e: Incomplete
    xy: Incomplete
    def kernel(self, x0=None, nstates=None): ...
TDDFTNoHybrid = CasidaTDDFT

def tddft(mf, frozen=None): ...
