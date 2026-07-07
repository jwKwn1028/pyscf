from _typeshed import Incomplete
from pyscf import __config__ as __config__, ao2mo as ao2mo, dft as dft, lib as lib
from pyscf.lib import logger as logger
from pyscf.mp.mp2 import get_frozen_mask as get_frozen_mask, get_nmo as get_nmo, get_nocc as get_nocc

einsum = lib.einsum
BLKMIN: Incomplete
MEMORYMIN: Incomplete

def kernel(gw, mo_energy, mo_coeff, td_e, td_xy, eris=None, orbs=None, verbose=...): ...
def get_sigma_element(gw, omega, tdm_p, tdm_q, td_e, eta=None, vir_sgn: int = 1): ...
def get_sigma_deriv_element(gw, omega, tdm_p, tdm_q, td_e, eta=None, vir_sgn: int = 1): ...
def get_g(omega, mo_energy, mo_occ, eta): ...

class GWExact(lib.StreamObject):
    eta: Incomplete
    linearized: Incomplete
    mol: Incomplete
    verbose: Incomplete
    stdout: Incomplete
    max_memory: Incomplete
    frozen: Incomplete
    mo_energy: Incomplete
    mo_coeff: Incomplete
    mo_occ: Incomplete
    def __init__(self, mf, frozen=None, tdmf=None) -> None: ...
    def dump_flags(self, verbose=None): ...
    @property
    def nocc(self): ...
    @nocc.setter
    def nocc(self, n) -> None: ...
    @property
    def nmo(self): ...
    @nmo.setter
    def nmo(self, n) -> None: ...
    get_nocc = get_nocc
    get_nmo = get_nmo
    get_frozen_mask = get_frozen_mask
    def get_g0(self, omega, eta=None): ...
    def get_g(self, omega, eta=None): ...
    def kernel(self, mo_energy=None, mo_coeff=None, td_e=None, td_xy=None, eris=None, orbs=None): ...
    def reset(self, mol=None): ...
    def ao2mo(self, mo_coeff=None): ...

class _ChemistsERIs:
    mol: Incomplete
    mo_coeff: Incomplete
    nocc: Incomplete
    fock: Incomplete
    oooo: Incomplete
    ovoo: Incomplete
    oovv: Incomplete
    ovvo: Incomplete
    ovov: Incomplete
    ovvv: Incomplete
    def __init__(self, mol=None) -> None: ...
