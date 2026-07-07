from _typeshed import Incomplete
from pyscf import lib as lib, symm as symm
from pyscf.adc import dfadc as dfadc, radc_ao2mo as radc_ao2mo, uadc as uadc, uadc_ao2mo as uadc_ao2mo
from pyscf.data.nist import HARTREE2EV as HARTREE2EV
from pyscf.lib import logger as logger

def get_imds(adc, eris=None): ...
def get_diag(adc, M_ij=None, eris=None): ...
def matvec(adc, M_ij=None, eris=None): ...
def get_trans_moments(adc): ...
def get_trans_moments_orbital(adc, orb, spin: str = 'alpha'): ...
def analyze_eigenvector(adc) -> None: ...
def analyze_spec_factor(adc) -> None: ...
def get_properties(adc, nroots: int = 1): ...
def analyze(myadc) -> None: ...
def compute_dyson_mo(myadc): ...
def make_rdm1(adc): ...
def make_rdm1_eigenvectors(adc, L, R): ...

class UADCIPCVS(uadc.UADC):
    verbose: Incomplete
    stdout: Incomplete
    max_memory: Incomplete
    max_space: Incomplete
    max_cycle: Incomplete
    conv_tol: Incomplete
    tol_residual: Incomplete
    t1: Incomplete
    t2: Incomplete
    imds: Incomplete
    e_corr: Incomplete
    method: Incomplete
    method_type: Incomplete
    nocc_a: Incomplete
    nocc_b: Incomplete
    nvir_a: Incomplete
    nvir_b: Incomplete
    mo_coeff: Incomplete
    mo_coeff_hf: Incomplete
    mo_energy_a: Incomplete
    mo_energy_b: Incomplete
    nmo_a: Incomplete
    nmo_b: Incomplete
    mol: Incomplete
    transform_integrals: Incomplete
    with_df: Incomplete
    spec_factor_print_tol: Incomplete
    evec_print_tol: Incomplete
    ncvs: Incomplete
    frozen: Incomplete
    mo_occ: Incomplete
    compute_properties: Incomplete
    approx_trans_moments: Incomplete
    compute_spin_square: bool
    E: Incomplete
    U: Incomplete
    P: Incomplete
    X: Incomplete
    def __init__(self, adc) -> None: ...
    kernel = uadc.kernel
    get_imds = get_imds
    get_diag = get_diag
    matvec = matvec
    get_trans_moments = get_trans_moments
    get_properties = get_properties
    analyze_spec_factor = analyze_spec_factor
    analyze_eigenvector = analyze_eigenvector
    analyze = analyze
    compute_dyson_mo = compute_dyson_mo
    def get_init_guess(self, nroots: int = 1, diag=None, ascending: bool = True, type=None, ini=None): ...
    def gen_matvec(self, imds=None, eris=None): ...
