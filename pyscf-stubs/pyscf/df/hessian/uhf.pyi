from pyscf import ao2mo as ao2mo, df as df, lib as lib
from pyscf.df.grad.rhf import LINEAR_DEP_THRESHOLD as LINEAR_DEP_THRESHOLD
from pyscf.hessian import uhf as uhf_hess
from pyscf.lib import logger as logger
from numpy import ndarray
from pyscf.df.hessian.uks import Hessian
from pyscf.lib.logger import Logger
from typing import Iterator, List, Optional, Tuple, Union

def partial_hess_elec(hessobj: "Hessian", mo_energy: Optional[ndarray]=None, mo_coeff: Optional[ndarray]=None, mo_occ: Optional[ndarray]=None, atmlst: Optional[range]=None, max_memory: int = 4000, verbose: Optional[Logger]=None) -> ndarray: ...
def make_h1(hessobj: "Hessian", mo_coeff: ndarray, mo_occ: ndarray, chkfile: None=None, atmlst: Optional[range]=None, verbose: Optional[Logger]=None) -> Tuple[List[ndarray], List[ndarray]]: ...

class Hessian(uhf_hess.Hessian):
    def __init__(self, mf) -> None: ...
    auxbasis_response: int
    partial_hess_elec = partial_hess_elec
    make_h1 = make_h1
