from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.cc import uccsd as uccsd
from pyscf.lib import logger as logger
from pyscf.lib.parameters import LARGE_DENOM as LARGE_DENOM, LOOSE_ZERO_TOL as LOOSE_ZERO_TOL
from pyscf.pbc import scf as scf
from pyscf.pbc.cc import kintermediates_uhf as kintermediates_uhf
from pyscf.pbc.lib import kpts_helper as kpts_helper
from pyscf.pbc.lib.kpts_helper import gamma_point as gamma_point
from pyscf.pbc.mp.kump2 import get_frozen_mask as get_frozen_mask, get_nmo as get_nmo, get_nocc as get_nocc, padded_mo_coeff as padded_mo_coeff, padding_k_idx as padding_k_idx
from numpy import complex128, float64, int64, ndarray
from pyscf.cc.uccsd import _ChemistsERIs
from pyscf.lib.misc import H5TmpFile
from pyscf.pbc.scf.kuhf import KUHF
from typing import List, Optional, Tuple, Union

einsum = lib.einsum

def mo_c_list_to_array(mo_coeff): ...
def convert_mo_coeff(mo_coeff: ndarray) -> ndarray: ...
def update_amps(cc: "KUCCSD", t1: Tuple[ndarray, ndarray], t2: Tuple[ndarray, ndarray, ndarray], eris: _ChemistsERIs) -> Tuple[Tuple[ndarray, ndarray], Tuple[ndarray, ndarray, ndarray]]: ...
def get_normt_diff(cc, t1, t2, t1new, t2new): ...
def energy(cc: "KUCCSD", t1: Tuple[ndarray, ndarray], t2: Tuple[ndarray, ndarray, ndarray], eris: _ChemistsERIs) -> float64: ...
def amplitudes_to_vector(t1: Tuple[ndarray, ndarray], t2: Tuple[ndarray, ndarray, ndarray]) -> ndarray: ...
def vector_to_amplitudes(vec: ndarray, nmo: Union[Tuple[int, int], Tuple[int64, int64]], nocc: Union[Tuple[int, int], Tuple[int64, int64]], nkpts: int = 1) -> Tuple[Tuple[ndarray, ndarray], Tuple[ndarray, ndarray, ndarray]]: ...
def add_vvvv_(cc: "KUCCSD", Ht2: Tuple[ndarray, ndarray, ndarray], t1: Tuple[ndarray, ndarray], t2: Tuple[ndarray, ndarray, ndarray], eris: _ChemistsERIs) -> Tuple[ndarray, ndarray, ndarray]: ...

class KUCCSD(uccsd.UCCSD):
    max_space: Incomplete
    kpts: Incomplete
    mo_energy: Incomplete
    khelper: Incomplete
    direct: bool
    def __init__(self, mf: KUHF, frozen: Optional[Tuple[List[List[int]], List[List[int]]]]=None, mo_coeff: None=None, mo_occ: None=None) -> None: ...
    @property
    def nkpts(self) -> int: ...
    get_normt_diff = get_normt_diff
    get_nocc = get_nocc
    get_nmo = get_nmo
    get_frozen_mask = get_frozen_mask
    update_amps = update_amps
    energy = energy
    def dump_flags(self, verbose: None=None) -> "KUCCSD": ...
    def ao2mo(self, mo_coeff: Optional[ndarray]=None) -> _ChemistsERIs: ...
    emp2: Incomplete
    def init_amps(self, eris: _ChemistsERIs) -> Tuple[complex128, Tuple[ndarray, ndarray], Tuple[ndarray, ndarray, ndarray]]: ...
    def amplitudes_to_vector(self, t1: Tuple[ndarray, ndarray], t2: Tuple[ndarray, ndarray, ndarray]) -> ndarray: ...
    def vector_to_amplitudes(self, vec: ndarray, nmo: None=None, nocc: None=None, nkpts: None=None) -> Tuple[Tuple[ndarray, ndarray], Tuple[ndarray, ndarray, ndarray]]: ...
    to_gpu = lib.to_gpu
UCCSD = KUCCSD
