from pyscf import ao2mo as ao2mo, df as df, lib as lib
from pyscf.df.grad.rhf import LINEAR_DEP_THRESHOLD as LINEAR_DEP_THRESHOLD
from pyscf.hessian import rhf as rhf_hess
from pyscf.lib import logger as logger

def partial_hess_elec(hessobj, mo_energy=None, mo_coeff=None, mo_occ=None, atmlst=None, max_memory: int = 4000, verbose=None): ...
def make_h1(hessobj, mo_coeff, mo_occ, chkfile=None, atmlst=None, verbose=None): ...

class Hessian(rhf_hess.Hessian):
    def __init__(self, mf) -> None: ...
    auxbasis_response: int
    partial_hess_elec = partial_hess_elec
    make_h1 = make_h1
