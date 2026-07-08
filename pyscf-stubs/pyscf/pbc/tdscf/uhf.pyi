from _typeshed import Incomplete
from pyscf import lib as lib
from pyscf.pbc import scf as scf
from pyscf.pbc.tdscf.rhf import TDBase as TDBase
from pyscf.tdscf import uhf as uhf
from numpy import ndarray
from pyscf.pbc.dft.uks import UKS
from typing import Tuple

def get_ab(mf: UKS) -> Tuple[Tuple[ndarray, ndarray, ndarray], Tuple[ndarray, ndarray, ndarray]]: ...

class TDA(TDBase):
    def get_ab(self, mf: None=None) -> Tuple[Tuple[ndarray, ndarray, ndarray], Tuple[ndarray, ndarray, ndarray]]: ...
    singlet: Incomplete
    get_init_guess: Incomplete
    kernel: Incomplete
    gen_vind: Incomplete
    get_frozen_mask: Incomplete
CIS = TDA

class TDHF(TDBase):
    get_ab: Incomplete
    singlet: Incomplete
    get_init_guess: Incomplete
    kernel: Incomplete
    gen_vind: Incomplete
    get_frozen_mask: Incomplete
RPA = TDHF
TDUHF = TDHF
