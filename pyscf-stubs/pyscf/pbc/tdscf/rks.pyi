from _typeshed import Incomplete
from pyscf import lib as lib
from pyscf.pbc import dft as dft
from pyscf.pbc.lib.kpts_helper import gamma_point as gamma_point
from pyscf.pbc.tdscf import rhf as rhf
from pyscf.tdscf import rks as rks
from pyscf.pbc.dft.rks import RKS
from pyscf.pbc.tdscf.rhf import TDHF
from typing import Union

class TDA(rhf.TDA): ...
RPA = rhf.TDHF
TDRKS = rhf.TDHF
TDDFT = rhf.TDHF

class CasidaTDDFT(TDDFT):
    get_init_guess: Incomplete
    gen_vind: Incomplete
    kernel: Incomplete
TDDFTNoHybrid = CasidaTDDFT

def tddft(mf: RKS, frozen: None=None) -> Union[CasidaTDDFT, TDHF]: ...
