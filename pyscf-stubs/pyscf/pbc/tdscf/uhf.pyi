from _typeshed import Incomplete
from pyscf import lib as lib
from pyscf.pbc import scf as scf
from pyscf.pbc.tdscf.rhf import TDBase as TDBase
from pyscf.tdscf import uhf as uhf

def get_ab(mf): ...

class TDA(TDBase):
    def get_ab(self, mf=None): ...
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
