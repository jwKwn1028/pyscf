from pyscf import lib as lib
from pyscf.ci import cisd as cisd, gcisd as gcisd, ucisd as ucisd
from pyscf.pbc import mp as mp, scf as scf
from _typeshed import Incomplete
from numpy import ndarray
from pyscf.cc.gccsd import _PhysicistsERIs
from pyscf.lib.numpy_helper import NPArrayWithTag
from pyscf.pbc.scf.ghf import GHF
from pyscf.pbc.scf.hf import RHF
from pyscf.pbc.scf.uhf import UHF
from typing import Optional

class RCISD(cisd.RCISD):
    def __init__(self, mf: RHF, frozen: None=None, mo_coeff: None=None, mo_occ: None=None) -> None: ...
    def ao2mo(self, mo_coeff: Optional[ndarray]=None) -> Incomplete: ...

class UCISD(ucisd.UCISD):
    def __init__(self, mf: UHF, frozen: None=None, mo_coeff: None=None, mo_occ: None=None) -> None: ...
    def ao2mo(self, mo_coeff: Optional[ndarray]=None) -> Incomplete: ...

class GCISD(gcisd.GCISD):
    def __init__(self, mf: GHF, frozen: None=None, mo_coeff: None=None, mo_occ: None=None) -> None: ...
    def ao2mo(self, mo_coeff: Optional[NPArrayWithTag]=None) -> _PhysicistsERIs: ...
