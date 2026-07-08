from _typeshed import Incomplete
from pyscf import lib as lib
from pyscf.lib import logger as logger
from pyscf.pbc.cc.kccsd_rhf import RCCSD as RCCSD
from pyscf.pbc.df import GDF as GDF, RSGDF as RSGDF
from pyscf.pbc.lib import ktensor as ktensor
from pyscf.pbc.lib.kpts import KQuartets as KQuartets, MORotationMatrix as MORotationMatrix
from pyscf.pbc.mp.kmp2 import get_nocc as get_nocc, padded_mo_coeff as padded_mo_coeff, padding_k_idx as padding_k_idx
from numpy import float64, int64, ndarray
from pyscf.pbc.lib.ktensor import KsymmArray
from pyscf.pbc.scf.khf_ksymm import KsymAdaptedKRHF
from typing import Callable, List, Optional, Tuple

einsum = lib.einsum

def update_amps(cc: "KsymAdaptedRCCSD", t1: KsymmArray, t2: KsymmArray, eris: "_PhysicistsERIs") -> Tuple[KsymmArray, KsymmArray]: ...
def add_vvvv_(cc: "KsymAdaptedRCCSD", Ht2: KsymmArray, t1: ndarray, t2: ndarray, eris: "_PhysicistsERIs") -> KsymmArray: ...
def energy(cc: "KsymAdaptedRCCSD", t1: KsymmArray, t2: KsymmArray, eris: "_PhysicistsERIs") -> float64: ...

class KsymAdaptedRCCSD(RCCSD):
    kqrts: Incomplete
    rmat: Incomplete
    ktensor_direct: bool
    eris_outcore: bool
    def __init__(self, mf: KsymAdaptedKRHF, frozen: None=None, mo_coeff: None=None, mo_occ: None=None) -> None: ...
    def ao2mo(self, mo_coeff: Optional[List[ndarray]]=None) -> "_PhysicistsERIs": ...
    emp2: Incomplete
    def init_amps(self, eris: "_PhysicistsERIs") -> Tuple[float64, KsymmArray, KsymmArray]: ...
    def amplitudes_to_vector(self, t1: KsymmArray, t2: KsymmArray) -> ndarray: ...
    def vector_to_amplitudes(self, vec: ndarray) -> Tuple[KsymmArray, KsymmArray]: ...
    energy = energy
    update_amps = update_amps

class _PhysicistsERIs:
    cell: Incomplete
    kpts: Incomplete
    mo_coeff: Incomplete
    nocc: Incomplete
    nmo: Incomplete
    nvir: Incomplete
    fock: Incomplete
    dtype: Incomplete
    oooo: Incomplete
    ooov: Incomplete
    oovv: Incomplete
    ovov: Incomplete
    voov: Incomplete
    vovv: Incomplete
    vvvv: Incomplete
    Lpv: Incomplete
    def __init__(self, cell: None=None) -> None: ...
