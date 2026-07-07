from _typeshed import Incomplete
from collections.abc import Generator
from pyscf import __config__ as __config__, lib as lib, scf as scf
from pyscf.lib import logger as logger
from pyscf.mp import dfmp2 as dfmp2, gmp2 as gmp2
from pyscf.mp.gmp2 import make_rdm1 as make_rdm1, make_rdm2 as make_rdm2

WITH_T2: Incomplete

def kernel(mp, mo_energy=None, mo_coeff=None, eris=None, with_t2=..., verbose=...): ...

class DFGMP2(gmp2.GMP2):
    __init__: Incomplete
    kernel: Incomplete
    split_mo_energy: Incomplete
    split_mo_coeff: Incomplete
    split_mo_occ: Incomplete
    reset: Incomplete
    def loop_ao2mo(self, mo_coeff, nocc, orbspin) -> Generator[Incomplete]: ...
    def ao2mo(self, mo_coeff=None): ...
    def make_rdm1(self, t2=None, ao_repr: bool = False, with_frozen: bool = True): ...
    def make_rdm2(self, t2=None, ao_repr: bool = False): ...
    def nuc_grad_method(self) -> None: ...
    def update_amps(self, t2, eris) -> None: ...
    def init_amps(self, mo_energy=None, mo_coeff=None, eris=None, with_t2=...): ...
    Gradients = NotImplemented
MP2 = DFGMP2
DFMP2 = DFGMP2
