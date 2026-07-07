from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.lib import einsum as einsum, logger as logger
from pyscf.lib.parameters import LARGE_DENOM as LARGE_DENOM
from pyscf.pbc import scf as scf
from pyscf.pbc.mp import kmp2 as kmp2

WITH_T2: Incomplete

def kernel(mp, mo_energy, mo_coeff, verbose=..., with_t2=...): ...
def kernel_with_t2(mp, mo_energy, mo_coeff, verbose=..., with_t2=...): ...
def make_rdm1(mp, t2=None, kind: str = 'compact'): ...
def make_t2_for_rdm1(mp): ...

class KsymAdaptedKMP2(kmp2.KMP2):
    e_hf: Incomplete
    e_corr_ss: Incomplete
    e_corr_os: Incomplete
    e_corr: Incomplete
    def kernel(self, mo_energy=None, mo_coeff=None, with_t2=...): ...
    make_rdm1 = make_rdm1
    def make_rdm2(self) -> None: ...
KRMP2 = KsymAdaptedKMP2
KMP2 = KsymAdaptedKMP2
