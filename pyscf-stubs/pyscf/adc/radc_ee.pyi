from _typeshed import Incomplete
from pyscf import lib as lib, symm as symm
from pyscf.adc import dfadc as dfadc, radc as radc, radc_amplitudes as radc_amplitudes, radc_ao2mo as radc_ao2mo
from pyscf.data.nist import HARTREE2EV as HARTREE2EV
from pyscf.lib import logger as logger

def get_imds(adc, eris=None): ...
def get_diag(adc, M_ab=None, eris=None): ...
def matvec(adc, M_ab=None, eris=None): ...
def get_trans_moments(adc): ...
def analyze_eigenvector(adc) -> None: ...
def analyze_spec_factor(adc) -> None: ...
def renormalize_eigenvectors(adc, nroots: int = 1): ...
def get_properties(adc, nroots: int = 1): ...
def analyze(myadc) -> None: ...
def make_rdm1(adc): ...
def make_rdm1_eigenvectors(adc, L, R): ...

class RADCEE(radc.RADC):
    mol: Incomplete
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
    mo_coeff: Incomplete
    mo_coeff_hf: Incomplete
    mo_energy: Incomplete
    nmo: Incomplete
    dip_mom: Incomplete
    transform_integrals: Incomplete
    with_df: Incomplete
    compute_properties: Incomplete
    approx_trans_moments: Incomplete
    E: Incomplete
    U: Incomplete
    P: Incomplete
    X: Incomplete
    evec_print_tol: Incomplete
    spec_factor_print_tol: Incomplete
    frozen: Incomplete
    mo_occ: Incomplete
    def __init__(self, adc) -> None: ...
    kernel = radc.kernel
    get_imds = get_imds
    matvec = matvec
    get_diag = get_diag
    get_trans_moments = get_trans_moments
    renormalize_eigenvectors = renormalize_eigenvectors
    analyze = analyze
    analyze_eigenvector = analyze_eigenvector
    analyze_spec_factor = analyze_spec_factor
    get_properties = get_properties
    def get_init_guess(self, nroots: int = 1, diag=None, ascending: bool = True, type=None, eris=None, ini=None): ...
    def gen_matvec(self, imds=None, eris=None): ...
