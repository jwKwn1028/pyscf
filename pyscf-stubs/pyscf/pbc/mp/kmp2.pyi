from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.lib import einsum as einsum, logger as logger
from pyscf.lib.parameters import LARGE_DENOM as LARGE_DENOM
from pyscf.mp import mp2 as mp2
from pyscf.pbc import scf as scf
from pyscf.pbc.df import df as df
from pyscf.pbc.lib import kpts_helper as kpts_helper
from numpy import int64, ndarray
from pyscf.lib.misc import StreamObject
from pyscf.lib.numpy_helper import NPArrayWithTag
from pyscf.pbc.mp.kmp2_stagger import KMP2_stagger
from pyscf.pbc.scf.khf import KRHF
from pyscf.pbc.scf.khf_ksymm import KsymAdaptedKRHF
from typing import Any, List, Optional, Tuple, Union

WITH_T2: Incomplete

def kernel(mp: "KMP2", mo_energy: ndarray, mo_coeff: Union[ndarray, List[ndarray]], verbose: int=..., with_t2: bool=...) -> Tuple[NPArrayWithTag, ndarray]: ...
def padding_k_idx(mp: StreamObject, kind: str = 'split') -> Union[List[ndarray], Tuple[List[ndarray], List[ndarray]]]: ...
def padded_mo_energy(mp: Union[KMP2, KMP2_stagger], mo_energy: ndarray) -> ndarray: ...
def padded_mo_coeff(mp: StreamObject, mo_coeff: Union[ndarray, List[ndarray]]) -> ndarray: ...
def get_nocc(mp: StreamObject, per_kpoint: bool = False) -> Union[int64, List[int64], List[int]]: ...
def get_nmo(mp: StreamObject, per_kpoint: bool = False) -> Union[int64, List[int]]: ...
def get_frozen_mask(mp: StreamObject) -> List[ndarray]: ...
def make_rdm1(mp: "KMP2", t2: Optional[ndarray]=None, kind: str = 'compact') -> List[ndarray]: ...
def make_rdm2(mp: "KMP2", t2: None=None, kind: str = 'compact') -> List[ndarray]: ...

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
    def __init__(self, mf: Union[KsymAdaptedKRHF, KRHF], frozen: Optional[Union[List[List[Union[int, Any]]], List[int]]]=None, mo_coeff: None=None, mo_occ: None=None) -> None: ...
    get_nocc = get_nocc
    get_nmo = get_nmo
    get_frozen_mask = get_frozen_mask
    make_rdm1 = make_rdm1
    make_rdm2 = make_rdm2
    def dump_flags(self) -> "KMP2": ...
    def kernel(self, mo_energy: None=None, mo_coeff: None=None, with_t2: bool=...) -> Tuple[float, ndarray]: ...
    to_gpu = lib.to_gpu
KRMP2 = KMP2
