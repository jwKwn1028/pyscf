from _typeshed import Incomplete
from functools import reduce as reduce
from pyscf import __config__ as __config__, df as df, lib as lib, scf as scf
from pyscf.lib import logger as logger
from pyscf.mp import dfmp2 as dfmp2, ump2 as ump2
from pyscf.mp.ump2 import make_rdm1 as make_rdm1, make_rdm2 as make_rdm2

WITH_T2: Incomplete
THRESH_LINDEP: Incomplete
libmp: Incomplete

def kernel(mp, mo_energy=None, mo_coeff=None, eris=None, with_t2=..., verbose=None): ...

class DFUMP2(ump2.UMP2):
    __init__: Incomplete
    get_nocc = ump2.get_nocc
    get_nmo = ump2.get_nmo
    get_frozen_mask = ump2.get_frozen_mask
    kernel: Incomplete
    make_fno = ump2.make_fno
    make_rdm1 = make_rdm1
    make_rdm2 = make_rdm2
    reset: Incomplete
    def split_mo_coeff(self, mo_coeff=None): ...
    def split_mo_energy(self, mo_energy=None): ...
    def split_mo_occ(self, mo_occ=None): ...
    def ao2mo(self, mo_coeff=None, ovL=None, ovL_to_save=None): ...
    def nuc_grad_method(self) -> None: ...
    def update_amps(self, t2, eris) -> None: ...
    def init_amps(self, mo_energy=None, mo_coeff=None, eris=None, with_t2=...): ...
    Gradients = NotImplemented
MP2 = DFUMP2
UMP2 = DFUMP2

class _DFINCOREERIS:
    with_df: Incomplete
    occ_coeff: Incomplete
    vir_coeff: Incomplete
    max_memory: Incomplete
    verbose: Incomplete
    stdout: Incomplete
    dtype: Incomplete
    dsize: int
    ovL: Incomplete
    def __init__(self, with_df, occ_coeff, vir_coeff, max_memory, ovL=None, verbose=None, stdout=None) -> None: ...
    @property
    def nocc(self): ...
    @property
    def nvir(self): ...
    @property
    def naux(self): ...
    def build(self) -> None: ...
    def get_occ_blk(self, s, i0, i1): ...
    def get_ov_blk(self, s, ia0, ia1): ...

class _DFOUTCOREERIS(_DFINCOREERIS):
    def __init__(self, with_df, occ_coeff, vir_coeff, max_memory, ovL=None, ovL_to_save=None, verbose=None, stdout=None) -> None: ...
    feri: Incomplete
    ovL: Incomplete
    def build(self) -> None: ...
