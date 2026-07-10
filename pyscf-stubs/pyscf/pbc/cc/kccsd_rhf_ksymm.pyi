from _typeshed import Incomplete
from pyscf import lib as lib
from pyscf.lib import logger as logger
from pyscf.pbc.cc.kccsd_rhf import RCCSD as RCCSD
from pyscf.pbc.df import GDF as GDF, RSGDF as RSGDF
from pyscf.pbc.lib import ktensor as ktensor
from pyscf.pbc.lib.kpts import KQuartets as KQuartets, MORotationMatrix as MORotationMatrix
from pyscf.pbc.mp.kmp2 import get_nocc as get_nocc, padded_mo_coeff as padded_mo_coeff, padding_k_idx as padding_k_idx

einsum = lib.einsum

def update_amps(cc, t1, t2, eris): ...
def add_vvvv_(cc, Ht2, t1, t2, eris): ...
def energy(cc, t1, t2, eris): ...

class KsymAdaptedRCCSD(RCCSD):
    kqrts: Incomplete
    rmat: Incomplete
    ktensor_direct: bool
    eris_outcore: bool
    def __init__(self, mf, frozen=None, mo_coeff=None, mo_occ=None) -> None: ...
    def ao2mo(self, mo_coeff=None): ...
    emp2: Incomplete
    def init_amps(self, eris): ...
    def amplitudes_to_vector(self, t1, t2): ...
    def vector_to_amplitudes(self, vec): ...
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
    def __init__(self, cell=None) -> None: ...
