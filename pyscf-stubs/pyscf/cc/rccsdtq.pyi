from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.cc import ccsd as ccsd, rccsdt as rccsdt
from pyscf.cc.rccsdt import compute_r1r2 as compute_r1r2, format_size as format_size, intermediates_t1t2 as intermediates_t1t2, intermediates_t3 as intermediates_t3, kernel as kernel, purify_tamps_tri_ as purify_tamps_tri_, r1r2_divide_e_ as r1r2_divide_e_, symmetrize_tamps_tri_ as symmetrize_tamps_tri_, t3_spin_summation_inplace_ as t3_spin_summation_inplace_, update_t1_fock_eris as update_t1_fock_eris
from pyscf.cc.rccsdt_highm import compute_r3 as compute_r3, intermediates_t3_add_t3 as intermediates_t3_add_t3, purify_tamps_ as purify_tamps_, r1r2_add_t3_ as r1r2_add_t3_, r3_divide_e_ as r3_divide_e_, t3_perm_symmetrize_inplace_ as t3_perm_symmetrize_inplace_, t3_spin_summation as t3_spin_summation
from pyscf.lib import logger as logger
from pyscf.mp.mp2 import get_e_hf as get_e_hf, get_frozen_mask as get_frozen_mask, get_nmo as get_nmo, get_nocc as get_nocc

def t4_spin_summation_inplace_(A, nocc4, nvir, pattern, alpha: float = 1.0, beta: float = 0.0): ...
def t4_add_(t4, r4, nocc4, nvir): ...
def unpack_t4_tri2block_(t4, t4_blk, map_, mask, i0, i1, j0, j1, k0, k1, l0, l1, nocc, nvir, blk_i, blk_j, blk_k, blk_l): ...
def accumulate_t4_block2tri_(t4, t4_blk, map_, i0, i1, j0, j1, k0, k1, l0, l1, nocc, nvir, blk_i, blk_j, blk_k, blk_l, alpha, beta): ...
def r2_add_t4_tri_(mycc, imds, r2, t4): ...
def r3_add_t4_tri_(mycc, imds, r3, t4): ...
def intermediates_t4_tri(mycc, imds, t2, t3, t4): ...
def compute_r4_tri(mycc, imds, t2, t3, t4): ...
def r4_tri_divide_e_(mycc, r4, mo_energy): ...
def update_amps_rccsdtq_tri_(mycc, tamps, eris): ...
def memory_estimate_log_rccsdtq(mycc): ...
def dump_chk(mycc, tamps=None, frozen=None, mo_coeff=None, mo_occ=None): ...

class RCCSDTQ(rccsdt.RCCSDT):
    __doc__: Incomplete
    conv_tol: Incomplete
    conv_tol_normt: Incomplete
    cc_order: int
    do_diis_max_t: Incomplete
    blksize: Incomplete
    @property
    def t4(self): ...
    @t4.setter
    def t4(self, val) -> None: ...
    tamps: Incomplete
    def __init__(self, mf, frozen=None, mo_coeff=None, mo_occ=None) -> None: ...
    do_tri_max_t: Incomplete
    memory_estimate_log = memory_estimate_log_rccsdtq
    update_amps_ = update_amps_rccsdtq_tri_
    dump_chk = dump_chk
    def kernel(self, tamps=None, eris=None): ...
    e_hf: Incomplete
    unique_tamps_map: Incomplete
    def ccsdtq(self, tamps=None, eris=None): ...

class _IMDS:
    t1_fock: Incomplete
    t1_eris: Incomplete
    F_oo: Incomplete
    F_vv: Incomplete
    W_oooo: Incomplete
    W_ovvo: Incomplete
    W_ovov: Incomplete
    W_vooo: Incomplete
    W_vvvo: Incomplete
    W_vvvv: Incomplete
    W_ovvvoo: Incomplete
    W_ovvovo: Incomplete
    W_vooooo: Incomplete
    W_vvoooo: Incomplete
    W_vvvvoo: Incomplete
    def __init__(self) -> None: ...
