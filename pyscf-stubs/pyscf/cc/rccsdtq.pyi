from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.cc import ccsd as ccsd, rccsdt as rccsdt
from pyscf.cc.rccsdt import _PhysicistsERIs, compute_r1r2 as compute_r1r2, format_size as format_size, intermediates_t1t2 as intermediates_t1t2, intermediates_t3 as intermediates_t3, kernel as kernel, purify_tamps_tri_ as purify_tamps_tri_, r1r2_divide_e_ as r1r2_divide_e_, symmetrize_tamps_tri_ as symmetrize_tamps_tri_, t3_spin_summation_inplace_ as t3_spin_summation_inplace_, update_t1_fock_eris as update_t1_fock_eris
from pyscf.cc.rccsdt_highm import compute_r3 as compute_r3, intermediates_t3_add_t3 as intermediates_t3_add_t3, purify_tamps_ as purify_tamps_, r1r2_add_t3_ as r1r2_add_t3_, r3_divide_e_ as r3_divide_e_, t3_perm_symmetrize_inplace_ as t3_perm_symmetrize_inplace_, t3_spin_summation as t3_spin_summation
from pyscf.lib import logger as logger
from pyscf.mp.mp2 import get_e_hf as get_e_hf, get_frozen_mask as get_frozen_mask, get_nmo as get_nmo, get_nocc as get_nocc
from numpy import float64, ndarray
from pyscf.cc.rccsdtq_highm import RCCSDTQ
from pyscf.lib.numpy_helper import NPArrayWithTag
from pyscf.scf.hf import RHF
from typing import List, Optional, Tuple, Union

def t4_spin_summation_inplace_(A: ndarray, nocc4: int, nvir: int, pattern: str, alpha: float = 1.0, beta: float = 0.0) -> ndarray: ...
def t4_add_(t4: ndarray, r4: ndarray, nocc4: int, nvir: int) -> ndarray: ...
def unpack_t4_tri2block_(t4: ndarray, t4_blk: ndarray, map_: ndarray, mask: ndarray, i0: int, i1: int, j0: int, j1: int, k0: int, k1: int, l0: int, l1: int, nocc: int, nvir: int, blk_i: int, blk_j: int, blk_k: int, blk_l: int) -> ndarray: ...
def accumulate_t4_block2tri_(t4: ndarray, t4_blk: ndarray, map_: ndarray, i0: int, i1: int, j0: int, j1: int, k0: int, k1: int, l0: int, l1: int, nocc: int, nvir: int, blk_i: int, blk_j: int, blk_k: int, blk_l: int, alpha: float, beta: float) -> ndarray: ...
def r2_add_t4_tri_(mycc: "RCCSDTQ", imds: "_IMDS", r2: ndarray, t4: ndarray) -> ndarray: ...
def r3_add_t4_tri_(mycc: "RCCSDTQ", imds: "_IMDS", r3: ndarray, t4: ndarray) -> ndarray: ...
def intermediates_t4_tri(mycc: "RCCSDTQ", imds: "_IMDS", t2: ndarray, t3: ndarray, t4: ndarray) -> "_IMDS": ...
def compute_r4_tri(mycc: "RCCSDTQ", imds: "_IMDS", t2: ndarray, t3: ndarray, t4: ndarray) -> ndarray: ...
def r4_tri_divide_e_(mycc: "RCCSDTQ", r4: ndarray, mo_energy: ndarray) -> ndarray: ...
def update_amps_rccsdtq_tri_(mycc: "RCCSDTQ", tamps: List[ndarray], eris: _PhysicistsERIs) -> List[float64]: ...
def memory_estimate_log_rccsdtq(mycc: Union[RCCSDTQ, RCCSDTQ]) -> Union[RCCSDTQ, RCCSDTQ]: ...
def dump_chk(mycc: Union[RCCSDTQ, RCCSDTQ], tamps: None=None, frozen: None=None, mo_coeff: None=None, mo_occ: None=None): ...

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
    def __init__(self, mf: RHF, frozen: Optional[int]=None, mo_coeff: None=None, mo_occ: None=None) -> None: ...
    do_tri_max_t: Incomplete
    memory_estimate_log = memory_estimate_log_rccsdtq
    update_amps_ = update_amps_rccsdtq_tri_
    dump_chk = dump_chk
    def kernel(self, tamps: Optional[List[ndarray]]=None, eris: Optional[_PhysicistsERIs]=None) -> Tuple[NPArrayWithTag, List[ndarray]]: ...
    e_hf: Incomplete
    unique_tamps_map: Incomplete
    def ccsdtq(self, tamps: Optional[List[ndarray]]=None, eris: Optional[_PhysicistsERIs]=None) -> Tuple[NPArrayWithTag, List[ndarray]]: ...

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
