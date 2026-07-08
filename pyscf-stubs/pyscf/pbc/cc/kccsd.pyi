from _typeshed import Incomplete
from pyscf import lib as lib
from pyscf.cc import ccsd as ccsd, gccsd as gccsd
from pyscf.lib import logger as logger
from pyscf.lib.parameters import LARGE_DENOM as LARGE_DENOM, LOOSE_ZERO_TOL as LOOSE_ZERO_TOL
from pyscf.pbc import scf as scf
from pyscf.pbc.cc import kintermediates as imdk
from pyscf.pbc.lib import kpts_helper as kpts_helper
from pyscf.pbc.mp.kmp2 import get_frozen_mask as get_frozen_mask, get_nmo as get_nmo, get_nocc as get_nocc, padded_mo_coeff as padded_mo_coeff, padding_k_idx as padding_k_idx
from numpy import float64, ndarray
from pyscf.cc.gccsd import _PhysicistsERIs
from pyscf.lib.numpy_helper import NPArrayWithTag
from pyscf.pbc.scf.kghf import KGHF
from pyscf.pbc.scf.khf import KRHF
from typing import Any, List, Optional, Tuple, Union

DEBUG: bool
einsum = lib.einsum

def energy(cc: "GCCSD", t1: Union[ndarray, NPArrayWithTag], t2: Union[ndarray, NPArrayWithTag], eris: _PhysicistsERIs) -> float64: ...
def update_amps(cc: "GCCSD", t1: Union[ndarray, NPArrayWithTag], t2: Union[ndarray, NPArrayWithTag], eris: _PhysicistsERIs) -> Tuple[ndarray, ndarray]: ...
def spatial2spin(tx: Union[Tuple[ndarray, ndarray], Tuple[ndarray, ndarray, ndarray], ndarray], orbspin: Union[ndarray, List[ndarray]], kconserv: ndarray) -> NPArrayWithTag: ...
def spin2spatial(tx: NPArrayWithTag, orbspin: ndarray, kconserv: ndarray) -> Union[Tuple[ndarray, ndarray], Tuple[ndarray, ndarray, ndarray]]: ...

class GCCSD(gccsd.GCCSD):
    kpts: Incomplete
    khelper: Incomplete
    def __init__(self, mf: Union[KRHF, KGHF], frozen: Optional[Union[int, List[List[int]], List[int], List[List[Union[int, Any]]]]]=None, mo_coeff: None=None, mo_occ: None=None) -> None: ...
    @property
    def nkpts(self) -> int: ...
    get_nocc = get_nocc
    get_nmo = get_nmo
    get_frozen_mask = get_frozen_mask
    def dump_flags(self, verbose: None=None) -> "GCCSD": ...
    emp2: int
    def init_amps(self, eris: _PhysicistsERIs) -> Tuple[float64, ndarray, ndarray]: ...
    t1: Incomplete
    t2: Incomplete
    def ccsd(self, t1: None=None, t2: None=None, eris: Optional[_PhysicistsERIs]=None, **kwargs) -> Tuple[float64, NPArrayWithTag, NPArrayWithTag]: ...
    update_amps = update_amps
    energy = energy
    def ao2mo(self, mo_coeff: Optional[Union[ndarray, List[NPArrayWithTag]]]=None) -> _PhysicistsERIs: ...
    def ccsd_t(self, t1: None=None, t2: None=None, eris: Optional[_PhysicistsERIs]=None) -> float64: ...
    def amplitudes_to_vector(self, t1: ndarray, t2: ndarray) -> ndarray: ...
    def vector_to_amplitudes(self, vec: ndarray, nmo: None=None, nocc: None=None) -> Tuple[ndarray, ndarray]: ...
    def spatial2spin(self, tx: Union[ndarray, Tuple[ndarray, ndarray], Tuple[ndarray, ndarray, ndarray]], orbspin: None=None, kconserv: None=None) -> NPArrayWithTag: ...
    def spin2spatial(self, tx, orbspin=None, kconserv=None): ...
    def from_uccsd(self, t1, t2, orbspin=None): ...
    def to_uccsd(self, t1, t2, orbspin=None): ...
    to_gpu = lib.to_gpu
CCSD = GCCSD
KCCSD = GCCSD
KGCCSD = GCCSD

def check_antisymm_3412(cc, kpts, integrals): ...
def check_antisymm_12(cc, kpts, integrals) -> None: ...
def check_antisymm_34(cc, kpts, integrals) -> None: ...
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
