from _typeshed import Incomplete
from pyscf import __config__ as __config__
from pyscf.data.nist import HARTREE2WAVENUMBER as HARTREE2WAVENUMBER, MP_ME as MP_ME
from pyscf.hessian import rhf as rhf
from pyscf.lib import logger as logger

CUTOFF_FREQUENCY: Incomplete
KEEP_IMAG_FREQUENCY: Incomplete
IMAG_CUTOFF_FREQUENCY: Incomplete

def kernel(ephobj, mo_energy=None, mo_coeff=None, mo_occ=None, mo_rep: bool = False): ...
def solve_hmat(mol, hmat, cutoff_frequency=..., keep_imag_frequency=...): ...
def get_mode(ephobj, mol=None, de=None): ...
def rhf_deriv_generator(mf, mo_coeff, mo_occ): ...
def vnuc_generator(ephobj, mol): ...
def get_eph(ephobj, mo1, omega, vec, mo_rep): ...

class EPH(rhf.Hessian):
    cutoff_frequency: Incomplete
    keep_imag_frequency: Incomplete
    def __init__(self, scf_method, cutoff_frequency=..., keep_imag_frequency=...) -> None: ...
    get_mode = get_mode
    get_eph = get_eph
    vnuc_generator = vnuc_generator
    kernel = kernel
