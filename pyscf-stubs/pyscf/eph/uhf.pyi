from _typeshed import Incomplete
from pyscf import lib as lib
from pyscf.data.nist import MP_ME as MP_ME
from pyscf.eph import rhf as rhf_eph
from pyscf.hessian import uhf as uhf_hess

CUTOFF_FREQUENCY: Incomplete
KEEP_IMAG_FREQUENCY: Incomplete

def uhf_deriv_generator(mf, mo_coeff, mo_occ): ...
def get_eph(ephobj, mo1, omega, vec, mo_rep): ...

class EPH(uhf_hess.Hessian):
    cutoff_frequency: Incomplete
    keep_imag_frequency: Incomplete
    def __init__(self, scf_method, cutoff_frequency=..., keep_imag_frequency=...) -> None: ...
    get_mode = rhf_eph.get_mode
    get_eph = get_eph
    vnuc_generator = rhf_eph.vnuc_generator
    kernel = rhf_eph.kernel
