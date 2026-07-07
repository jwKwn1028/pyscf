from _typeshed import Incomplete
from pyscf import lib as lib, scf as scf, symm as symm
from pyscf.adc import dfadc as dfadc, radc_ao2mo as radc_ao2mo, uadc as uadc, uadc_amplitudes as uadc_amplitudes, uadc_ao2mo as uadc_ao2mo
from pyscf.data.nist import HARTREE2EV as HARTREE2EV
from pyscf.lib import logger as logger
from pyscf.scf import hf_symm as hf_symm

def get_imds(adc, eris=None): ...
def get_diag(adc, M_ia_jb=None, eris=None): ...
def matvec(adc, M_ia_jb=None, eris=None): ...
def make_rdm1(adc): ...
def make_rdm1_eigenvectors(adc, L, R): ...
def get_spin_square(adc): ...
def get_trans_moments(adc): ...
def analyze_eigenvector(adc) -> None: ...
def analyze_spec_factor(adc) -> None: ...
def get_properties(adc, nroots: int = 1): ...
def analyze(myadc) -> None: ...

class UADCEE(uadc.UADC):
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
    transform_integrals: Incomplete
    with_df: Incomplete
    compute_properties: Incomplete
    approx_trans_moments: Incomplete
    frozen: Incomplete
    mo_occ: Incomplete
    spec_factor_print_tol: Incomplete
    evec_print_tol: Incomplete
    E: Incomplete
    U: Incomplete
    P: Incomplete
    X: Incomplete
    f_ov: Incomplete
    compute_spin_square: Incomplete
    dip_mom: Incomplete
    dip_mom_nuc: Incomplete
    def __init__(self, adc) -> None: ...
    kernel = uadc.kernel
    get_imds = get_imds
    get_diag = get_diag
    matvec = matvec
    get_trans_moments = get_trans_moments
    get_spin_square = get_spin_square
    get_properties = get_properties
    analyze_eigenvector = analyze_eigenvector
    analyze_spec_factor = analyze_spec_factor
    analyze = analyze
    def get_init_guess(self, nroots: int = 1, diag=None, ascending: bool = True, type=None, eris=None, ini=None): ...
    def gen_matvec(self, imds=None, eris=None): ...
