from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.lib import einsum as einsum, logger as logger
from pyscf.lib.parameters import LARGE_DENOM as LARGE_DENOM
from pyscf.mp import mp2 as mp2
from pyscf.pbc import scf as scf
from pyscf.pbc.df import df as df
from pyscf.pbc.lib import kpts_helper as kpts_helper

WITH_T2: Incomplete

def kernel(mp, mo_energy, mo_coeff, verbose=..., with_t2=...): ...
def padding_k_idx(mp, kind: str = 'split'): ...
def padded_mo_energy(mp, mo_energy): ...
def padded_mo_coeff(mp, mo_coeff): ...
def get_nocc(mp, per_kpoint: bool = False): ...
def get_nmo(mp, per_kpoint: bool = False): ...
def get_frozen_mask(mp): ...
def make_rdm1(mp, t2=None, kind: str = 'compact'): ...
def make_rdm2(mp, t2=None, kind: str = 'compact'): ...

class KMP2(mp2.MP2):
    mol: Incomplete
    verbose: Incomplete
    stdout: Incomplete
    max_memory: Incomplete
    frozen: Incomplete
    with_df_ints: bool
    kpts: Incomplete
    nkpts: Incomplete
    khelper: Incomplete
    mo_energy: Incomplete
    mo_coeff: Incomplete
    mo_occ: Incomplete
    e_hf: Incomplete
    e_corr: Incomplete
    e_corr_ss: Incomplete
    e_corr_os: Incomplete
    t2: Incomplete
    def __init__(self, mf, frozen=None, mo_coeff=None, mo_occ=None) -> None: ...
    get_nocc = get_nocc
    get_nmo = get_nmo
    get_frozen_mask = get_frozen_mask
    make_rdm1 = make_rdm1
    make_rdm2 = make_rdm2
    def dump_flags(self): ...
    def kernel(self, mo_energy=None, mo_coeff=None, with_t2=...): ...
    to_gpu = lib.to_gpu
KRMP2 = KMP2
