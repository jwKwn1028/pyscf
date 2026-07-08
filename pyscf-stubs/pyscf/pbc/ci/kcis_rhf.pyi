from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.lib import logger as logger
from pyscf.pbc import scf as scf, tools as tools
from pyscf.pbc.df import df as df
from pyscf.pbc.lib import kpts_helper as kpts_helper
from pyscf.pbc.mp.kmp2 import get_frozen_mask as get_frozen_mask, get_nmo as get_nmo, get_nocc as get_nocc, padded_mo_coeff as padded_mo_coeff, padding_k_idx as padding_k_idx
from numpy import int64, ndarray
from pyscf.pbc.scf.khf import KRHF
from typing import Callable, List, Optional, Tuple

einsum = lib.einsum
direct_sum = lib.direct_sum

def kernel(cis: "KCIS", nroots: int = 1, eris: Optional[_CIS_ERIS]=None, kptlist: Optional[List[int]]=None, **kargs) -> Tuple[List[ndarray], List[List[ndarray]]]: ...
def cis_matvec_singlet(cis: "KCIS", vector: ndarray, kshift: int, eris: Optional[_CIS_ERIS]=None) -> ndarray: ...
def cis_H(cis: "KCIS", kshift: int, eris: Optional[_CIS_ERIS]=None) -> ndarray: ...
def cis_diag(cis: "KCIS", kshift: int, eris: Optional[_CIS_ERIS]=None) -> ndarray: ...

class KCIS(lib.StreamObject):
    kpts: Incomplete
    verbose: Incomplete
    max_memory: Incomplete
    max_space: Incomplete
    max_cycle: Incomplete
    conv_tol: Incomplete
    keep_exxdiv: bool
    direct: bool
    build_full_H: bool
    davidson: bool
    khelper: Incomplete
    mo_coeff: Incomplete
    mo_occ: Incomplete
    frozen: Incomplete
    voov: Incomplete
    ovov: Incomplete
    def __init__(self, mf: KRHF, frozen: None=None, mo_coeff: None=None, mo_occ: None=None) -> None: ...
    def dump_flags(self, verbose: None=None) -> "KCIS": ...
    @property
    def nkpts(self) -> int: ...
    @property
    def nocc(self) -> int64: ...
    @property
    def nmo(self) -> int64: ...
    get_nocc = get_nocc
    get_nmo = get_nmo
    get_frozen_mask = get_frozen_mask
    get_diag = cis_diag
    matvec = cis_matvec_singlet
    kernel = kernel
    def vector_size(self) -> int64: ...
    def vector_to_amplitudes(self, vector: ndarray, nkpts: None=None, nmo: None=None, nocc: None=None) -> ndarray: ...
    def amplitudes_to_vector(self, r: ndarray) -> ndarray: ...
    def ao2mo(self, mo_coeff: None=None) -> "_CIS_ERIS": ...
    def gen_matvec(self, kshift: int, eris: Optional[_CIS_ERIS]=None, **kwargs) -> Tuple[Callable, ndarray]: ...
    def get_init_guess(self, nroots: int = 1, diag: Optional[ndarray]=None) -> List[ndarray]: ...
    def get_kconserv_r(self, kshift: int) -> ndarray: ...

class _CIS_ERIS:
    fock: Incomplete
    mo_energy: Incomplete
    ovov: Incomplete
    voov: Incomplete
    dtype: Incomplete
    feri1: Incomplete
    def __init__(self, cis: KCIS, mo_coeff: None=None, method: str = 'incore') -> None: ...
