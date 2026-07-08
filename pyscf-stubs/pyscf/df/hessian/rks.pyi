from pyscf import lib as lib
from pyscf.hessian import rks as rks_hess
from pyscf.lib import logger as logger
from numpy import ndarray
from pyscf.lib.logger import Logger
from typing import Optional

def partial_hess_elec(hessobj: "Hessian", mo_energy: Optional[ndarray]=None, mo_coeff: Optional[ndarray]=None, mo_occ: Optional[ndarray]=None, atmlst: Optional[range]=None, max_memory: int = 4000, verbose: Optional[Logger]=None) -> ndarray: ...
def make_h1(hessobj: "Hessian", mo_coeff: ndarray, mo_occ: ndarray, chkfile: None=None, atmlst: Optional[range]=None, verbose: Optional[Logger]=None) -> ndarray: ...

class Hessian(rks_hess.Hessian):
    def __init__(self, mf) -> None: ...
    auxbasis_response: int
    partial_hess_elec = partial_hess_elec
    make_h1 = make_h1
