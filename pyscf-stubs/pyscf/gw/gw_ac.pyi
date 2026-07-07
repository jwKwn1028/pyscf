from _typeshed import Incomplete
from pyscf import df as df, dft as dft, lib as lib, scf as scf
from pyscf.ao2mo._ao2mo import nr_e2 as nr_e2
from pyscf.gw.utils.ac_grid import PadeAC as PadeAC, TwoPoleAC as TwoPoleAC
from pyscf.gw.utils.gw_np_helper import addto_diagonal as addto_diagonal, get_id_minus_pi_inv as get_id_minus_pi_inv, mkslice as mkslice
from pyscf.lib import einsum as einsum, logger as logger, temporary_env as temporary_env
from pyscf.mp.mp2 import get_frozen_mask as get_frozen_mask, get_nmo as get_nmo, get_nocc as get_nocc

def kernel(gw): ...
def get_rho_response(omega, mo_energy, Lia, out=None): ...
def get_rho_response_metal(omega, mo_energy, mo_occ, Lpq, out=None): ...
def get_sigma(gw, orbs, Lpq, quad_freqs, quad_wts, ef, mo_energy, mo_coeff=None, mo_occ=None, iw_cutoff=None, eval_freqs=None, mo_energy_w=None, fullsigma: bool = False): ...
def get_sigma_outcore(gw, orbs, quad_freqs, quad_wts, ef, mo_energy, mo_coeff, mo_occ=None, iw_cutoff=None, eval_freqs=None, mo_energy_w=None, fullsigma: bool = False): ...
def get_g0(omega, mo_energy, eta): ...
def set_frozen_orbs(gw) -> None: ...

class GWAC(lib.StreamObject):
    mol: Incomplete
    verbose: Incomplete
    stdout: Incomplete
    max_memory: Incomplete
    auxbasis: Incomplete
    frozen: Incomplete
    orbs: Incomplete
    fullsigma: bool
    rdm: bool
    vhf_df: bool
    outcore: bool
    segsize: int
    eta: float
    nw: int
    nw2: Incomplete
    ac: str
    ac_iw_cutoff: float
    ac_pade_npts: int
    ac_pade_step_ratio: Incomplete
    ac_pes_mmax: int
    ac_pes_maxiter: int
    ac_pes_disp: bool
    ac_idx: Incomplete
    qpe_max_iter: int
    qpe_tol: float
    qpe_linearized: bool
    qpe_linearized_range: Incomplete
    writefile: int
    orbs_frz: Incomplete
    mo_energy: Incomplete
    mo_coeff: Incomplete
    mo_occ: Incomplete
    Lpq: Incomplete
    vk: Incomplete
    vxc: Incomplete
    freqs: Incomplete
    wts: Incomplete
    ef: Incomplete
    sigmaI: Incomplete
    acobj: Incomplete
    def __init__(self, mf, frozen=None, auxbasis=None) -> None: ...
    def dump_flags(self) -> None: ...
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
    def kernel(self) -> None: ...
    with_df: Incomplete
    def initialize_df(self, auxbasis=None) -> None: ...
    def ao2mo(self, mo_coeff=None): ...
    def loop_ao2mo(self, mo_coeff=None, ijslice=None, blksize=None): ...
    def get_ef(self, mo_energy=None): ...
    def energy_tot(self): ...
    def make_rdm1(self, ao_repr: bool = False, mode: str = 'linear'): ...
    def make_gf(self, omega, eta: float = 0.0, mode: str = 'dyson'): ...
    def get_sigma_exchange(self, mo_coeff): ...
    def setup_evaluation_grid(self, fallback_freqs=None, fallback_wts=None): ...
