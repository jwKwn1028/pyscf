import pyscf.cc.ccsd
from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.lib import logger as logger
from pyscf.lib.parameters import LARGE_DENOM as LARGE_DENOM, LOOSE_ZERO_TOL as LOOSE_ZERO_TOL
from pyscf.pbc import scf as scf
from pyscf.pbc.cc import kintermediates_rhf as imdk
from pyscf.pbc.df import GDF as GDF, RSGDF as RSGDF, df as df
from pyscf.pbc.lib import kpts_helper as kpts_helper
from pyscf.pbc.lib.kpts_helper import gamma_point as gamma_point
from pyscf.pbc.mp.kmp2 import get_frozen_mask as get_frozen_mask, get_nmo as get_nmo, get_nocc as get_nocc, padded_mo_coeff as padded_mo_coeff, padding_k_idx as padding_k_idx
from numpy import float64, int64, ndarray
from pyscf.pbc.cc.kccsd_rhf_ksymm import KsymAdaptedRCCSD
from pyscf.pbc.lib.ktensor import KsymmArray
from pyscf.pbc.scf.khf import KRHF
from pyscf.pbc.scf.khf_ksymm import KsymAdaptedKRHF
from typing import Any, List, Optional, Tuple, Union

einsum = lib.einsum
kernel = pyscf.cc.ccsd.kernel

def get_normt_diff(cc, t1, t2, t1new, t2new): ...
def update_amps(cc: "RCCSD", t1: ndarray, t2: ndarray, eris: "_ERIS") -> Tuple[ndarray, ndarray]: ...
def describe_nested(data: Union[ndarray, Tuple[ndarray, ndarray]]) -> Any: ...
def nested_to_vector(data: Union[ndarray, Tuple[ndarray, ndarray]], destination: Optional[ndarray]=None, offset: int = 0) -> Union[Tuple[ndarray, List[Union[Tuple[int, int, int], Tuple[int, int, int, int, int, int, int]]]], Tuple[ndarray, List[Union[Tuple[int], Tuple[int, int, int, int, int]]]], int]: ...
def vector_to_nested(vector: ndarray, struct: Any, copy: bool = True, ensure_size_matches: bool = True) -> Union[List[ndarray], Tuple[ndarray, int64]]: ...
def energy(cc: "RCCSD", t1: ndarray, t2: ndarray, eris: "_ERIS") -> Union[float, float64]: ...
def add_vvvv_(cc: "RCCSD", Ht2: ndarray, t1: ndarray, t2: ndarray, eris: "_ERIS") -> ndarray: ...
def kconserve_pmatrix(nkpts, kconserv): ...

class RCCSD(pyscf.cc.ccsd.CCSD):
    max_space: Incomplete
    kpts: Incomplete
    khelper: Incomplete
    ip_partition: Incomplete
    ea_partition: Incomplete
    direct: bool
    keep_exxdiv: bool
    __imds__: Incomplete
    def __init__(self, mf: Union[KRHF, KsymAdaptedKRHF], frozen: Optional[Union[int, List[List[int]], List[List[Union[int, Any]]], List[int]]]=None, mo_coeff: None=None, mo_occ: None=None) -> None: ...
    @property
    def nkpts(self) -> int: ...
    get_normt_diff = get_normt_diff
    get_nocc = get_nocc
    get_nmo = get_nmo
    get_frozen_mask = get_frozen_mask
    def dump_flags(self, verbose: None=None) -> Union[RCCSD, KsymAdaptedRCCSD]: ...
    @property
    def ccsd_vector_desc(self) -> List[Union[Tuple[int, int64, int64], Tuple[int, int, int, int64, int64, int64, int64]]]: ...
    def amplitudes_to_vector(self, t1: ndarray, t2: ndarray) -> ndarray: ...
    def vector_to_amplitudes(self, vec: ndarray) -> List[ndarray]: ...
    emp2: Incomplete
    def init_amps(self, eris: "_ERIS") -> Tuple[float64, ndarray, ndarray]: ...
    energy = energy
    update_amps = update_amps
    def kernel(self, t1: None=None, t2: None=None, eris: Optional[_ERIS]=None, mbpt2: bool = False) -> Union[Tuple[float, ndarray, ndarray], Tuple[float64, ndarray, ndarray], Tuple[float64, KsymmArray, KsymmArray]]: ...
    e_hf: Incomplete
    eris: Incomplete
    def ccsd(self, t1: None=None, t2: None=None, eris: Optional[_ERIS]=None, mbpt2: bool = False) -> Union[Tuple[float, ndarray, ndarray], Tuple[float64, ndarray, ndarray], Tuple[float64, KsymmArray, KsymmArray]]: ...
    def ccsd_t(self, t1: None=None, t2: None=None, eris: Optional[_ERIS]=None) -> float64: ...
    def ipccsd(self, nroots: int = 1, left: bool = False, koopmans: bool = False, guess: None=None, partition: None=None, eris: None=None, kptlist: Optional[Tuple[int]]=None) -> Tuple[ndarray, ndarray]: ...
    def eaccsd(self, nroots: int = 1, left: bool = False, koopmans: bool = False, guess: None=None, partition: None=None, eris: None=None, kptlist: Optional[Tuple[int]]=None) -> Tuple[ndarray, ndarray]: ...
    def ao2mo(self, mo_coeff: Optional[Union[List[ndarray], ndarray]]=None) -> "_ERIS": ...
    to_gpu = lib.to_gpu
    def ipccsd_matvec(self, vector, kshift): ...
    def ipccsd_diag(self, kshift): ...
    def eaccsd_matvec(self, vector, kshift): ...
    def eaccsd_diag(self, kshift): ...
    @property
    def imds(self): ...
KRCCSD = RCCSD

class _ERIS:
    fock: Incomplete
    mo_energy: Incomplete
    oooo: Incomplete
    ooov: Incomplete
    oovv: Incomplete
    ovov: Incomplete
    voov: Incomplete
    vovv: Incomplete
    vvvv: Incomplete
    dtype: Incomplete
    feri1: Incomplete
    def __init__(self, cc: RCCSD, mo_coeff: Optional[Union[List[ndarray], ndarray]]=None, method: str = 'incore') -> None: ...
imd = imdk

class _IMDS:
    verbose: Incomplete
    stdout: Incomplete
    t1: Incomplete
    t2: Incomplete
    eris: Incomplete
    kconserv: Incomplete
    made_ip_imds: bool
    made_ea_imds: bool
    def __init__(self, cc) -> None: ...
    Woooo: Incomplete
    Wooov: Incomplete
    Wovoo: Incomplete
    def make_ip(self, ip_partition=None) -> None: ...
    Wvovv: Incomplete
    Wvvvo: Incomplete
    Wvvvv: Incomplete
    def make_ea(self, ea_partition=None) -> None: ...
    def make_ee(self) -> None: ...
