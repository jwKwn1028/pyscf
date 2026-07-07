from _typeshed import Incomplete
from pyscf import __config__ as __config__, df as df, lib as lib
from pyscf.adc import radc_amplitudes as radc_amplitudes, radc_ao2mo as radc_ao2mo
from pyscf.data.nist import HARTREE2EV as HARTREE2EV
from pyscf.lib import logger as logger
from pyscf.mp import mp2 as mp2

def kernel(adc, nroots: int = 1, guess=None, eris=None, verbose=None): ...
def make_ref_rdm1(adc, with_frozen: bool = True, ao_repr: bool = False): ...
def get_frozen_mask(adc): ...

class RADC(lib.StreamObject):
    incore_complete: Incomplete
    async_io: Incomplete
    blkmin: Incomplete
    memorymin: Incomplete
    mol: Incomplete
    verbose: Incomplete
    stdout: Incomplete
    max_memory: Incomplete
    max_space: Incomplete
    max_cycle: Incomplete
    conv_tol: Incomplete
    tol_residual: Incomplete
    scf_energy: Incomplete
    frozen: Incomplete
    mo_occ: Incomplete
    e_corr: Incomplete
    t1: Incomplete
    t2: Incomplete
    imds: Incomplete
    mo_coeff: Incomplete
    mo_coeff_hf: Incomplete
    mo_energy: Incomplete
    if_heri_eris: bool
    chkfile: Incomplete
    method: str
    method_type: str
    with_df: Incomplete
    compute_properties: bool
    approx_trans_moments: bool
    evec_print_tol: float
    spec_factor_print_tol: float
    ncvs: Incomplete
    E: Incomplete
    U: Incomplete
    P: Incomplete
    X: Incomplete
    dip_mom: Incomplete
    dip_mom_nuc: Incomplete
    def __init__(self, mf, frozen=None, mo_coeff=None, mo_occ=None) -> None: ...
    compute_amplitudes = radc_amplitudes.compute_amplitudes
    compute_energy = radc_amplitudes.compute_energy
    transform_integrals = radc_ao2mo.transform_integrals_incore
    make_ref_rdm1 = make_ref_rdm1
    get_frozen_mask = get_frozen_mask
    def dump_flags(self, verbose=None): ...
    def dump_flags_gs(self, verbose=None): ...
    def kernel_gs(self): ...
    def kernel(self, nroots: int = 1, guess=None, eris=None): ...
    def ea_adc(self, nroots: int = 1, guess=None, eris=None): ...
    def ee_adc(self, nroots: int = 1, guess=None, eris=None): ...
    def ip_adc(self, nroots: int = 1, guess=None, eris=None): ...
    def ip_cvs_adc(self, nroots: int = 1, guess=None, eris=None): ...
    def density_fit(self, auxbasis=None, with_df=None): ...
    def analyze(self) -> None: ...
    def compute_dyson_mo(self): ...
    def make_rdm1(self, with_frozen: bool = True, ao_repr: bool = False): ...
