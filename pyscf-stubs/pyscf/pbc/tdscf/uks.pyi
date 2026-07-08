from _typeshed import Incomplete
from pyscf import lib as lib
from pyscf.pbc import dft as dft
from pyscf.pbc.tdscf.uhf import TDHF, TDA as TDA, TDHF as TDDFT
from pyscf.tdscf import uks as uks
from pyscf.pbc.dft.uks import UKS
from typing import Union

RPA = TDDFT
TDUKS = TDDFT

class CasidaTDDFT(TDDFT):
    get_init_guess: Incomplete
    gen_vind: Incomplete
    kernel: Incomplete
TDDFTNoHybrid = CasidaTDDFT

def tddft(mf: UKS, frozen: None=None) -> Union[CasidaTDDFT, TDHF]: ...
