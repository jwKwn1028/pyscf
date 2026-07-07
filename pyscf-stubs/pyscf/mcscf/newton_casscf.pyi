from _typeshed import Incomplete
from itertools import product as product
from pyscf import lib as lib, scf as scf
from pyscf.lib import logger as logger
from pyscf.mcscf import addons as addons, casci as casci, mc1step as mc1step
from pyscf.mcscf.casci import canonicalize as canonicalize, cas_natorb as cas_natorb, get_fock as get_fock
from pyscf.soscf import ciah as ciah

def gen_g_hop(casscf, mo, ci0, eris, verbose=None): ...
def extract_rotation(casscf, dr, u, ci0): ...
def update_orb_ci(casscf, mo, ci0, eris, x0_guess=None, conv_tol_grad: float = 0.0001, max_stepsize=None, verbose=None): ...
def kernel(casscf, mo_coeff, tol: float = 1e-07, conv_tol_grad=None, ci0=None, callback=None, verbose=..., dump_chk: bool = True): ...

class CASSCF(mc1step.CASSCF):
    __doc__: Incomplete
    frozen: Incomplete
    max_stepsize: float
    max_cycle_macro: int
    max_cycle_micro: int
    conv_tol: float
    conv_tol_grad: Incomplete
    ah_level_shift: float
    ah_conv_tol: float
    ah_max_cycle: int
    ah_lindep: float
    ah_start_tol: float
    ah_start_cycle: int
    ah_grad_trust_region: float
    kf_trust_region: float
    kf_interval: int
    internal_rotation: bool
    chkfile: Incomplete
    chk_ci: bool
    e_tot: Incomplete
    e_cas: Incomplete
    ci: Incomplete
    mo_coeff: Incomplete
    mo_energy: Incomplete
    converged: bool
    def __init__(self, mf_or_mol, ncas, nelecas, ncore=None, frozen=None) -> None: ...
    def dump_flags(self, verbose=None): ...
    def kernel(self, mo_coeff=None, ci0=None, callback=None): ...
    def casci(self, mo_coeff, ci0=None, eris=None, verbose=None, envs=None): ...
    def update_ao2mo(self, mo) -> None: ...
