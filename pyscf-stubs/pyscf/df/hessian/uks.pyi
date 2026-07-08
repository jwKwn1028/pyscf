from pyscf import lib as lib
from pyscf.hessian import uks as uks_hess
from pyscf.lib import logger as logger

def partial_hess_elec(hessobj, mo_energy=None, mo_coeff=None, mo_occ=None, atmlst=None, max_memory: int = 4000, verbose=None): ...
def make_h1(hessobj, mo_coeff, mo_occ, chkfile=None, atmlst=None, verbose=None): ...

class Hessian(uks_hess.Hessian):
    def __init__(self, mf) -> None: ...
    auxbasis_response: int
    partial_hess_elec = partial_hess_elec
    make_h1 = make_h1
