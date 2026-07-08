from _typeshed import Incomplete
from itertools import product as product
from pyscf import __config__ as __config__, lib as lib
from pyscf.adc import radc_ao2mo as radc_ao2mo
from pyscf.lib import logger as logger
from pyscf.lib.parameters import LARGE_DENOM as LARGE_DENOM, LOOSE_ZERO_TOL as LOOSE_ZERO_TOL
from pyscf.pbc import df as df, mp as mp, scf as scf, tools as tools
from pyscf.pbc.adc import dfadc as dfadc, kadc_ao2mo as kadc_ao2mo, kadc_rhf as kadc_rhf
from pyscf.pbc.lib import kpts_helper as kpts_helper
from pyscf.pbc.mp.kmp2 import get_frozen_mask as get_frozen_mask, get_nmo as get_nmo, get_nocc as get_nocc, padded_mo_coeff as padded_mo_coeff, padding_k_idx as padding_k_idx
from numpy import int64, ndarray
from pyscf.pbc.adc.kadc_rhf import RADC
from typing import Callable, List, Optional, Tuple

def vector_size(adc: "RADCEA") -> int64: ...
def get_imds(adc: "RADCEA", eris: Optional[Callable]=None) -> ndarray: ...
def get_diag(adc: "RADCEA", kshift: int, M_ab: Optional[ndarray]=None, eris: Optional[Callable]=None) -> ndarray: ...
def matvec(adc: "RADCEA", kshift: int, M_ab: Optional[ndarray]=None, eris: Optional[Callable]=None) -> Callable: ...
def get_trans_moments(adc: "RADCEA", kshift: int) -> ndarray: ...
def get_trans_moments_orbital(adc: "RADCEA", orb: int, kshift: int) -> ndarray: ...
def renormalize_eigenvectors(adc: "RADCEA", kshift: int, U: ndarray, nroots: int = 1) -> ndarray: ...
def get_properties(adc: "RADCEA", kshift: int, U: ndarray, nroots: int = 1) -> Tuple[ndarray, ndarray]: ...

class RADCEA(kadc_rhf.RADC):
    verbose: Incomplete
    stdout: Incomplete
    max_memory: Incomplete
    max_space: Incomplete
    max_cycle: Incomplete
    conv_tol: Incomplete
    tol_residual: Incomplete
    t1: Incomplete
    t2: Incomplete
    method: Incomplete
    method_type: Incomplete
    compute_properties: Incomplete
    approx_trans_moments: Incomplete
    kpts: Incomplete
    exxdiv: Incomplete
    khelper: Incomplete
    cell: Incomplete
    mo_coeff: Incomplete
    mo_occ: Incomplete
    frozen: Incomplete
    nkop_chk: Incomplete
    kop_npick: Incomplete
    e_corr: Incomplete
    mo_energy: Incomplete
    imds: Incomplete
    chnk_size: Incomplete
    def __init__(self, adc: RADC) -> None: ...
    kernel = kadc_rhf.kernel
    get_imds = get_imds
    get_diag = get_diag
    matvec = matvec
    vector_size = vector_size
    get_trans_moments = get_trans_moments
    renormalize_eigenvectors = renormalize_eigenvectors
    get_properties = get_properties
    def get_init_guess(self, nroots: int = 1, diag: Optional[ndarray]=None, ascending: bool = True) -> List[ndarray]: ...
    def gen_matvec(self, kshift: int, imds: Optional[ndarray]=None, eris: Optional[Callable]=None) -> Tuple[Callable, ndarray]: ...

def ea_contract_r_vvvv(adc: RADCEA, r2: ndarray, vvvv: ndarray, ka: int, kb: int, kc: int64) -> ndarray: ...
