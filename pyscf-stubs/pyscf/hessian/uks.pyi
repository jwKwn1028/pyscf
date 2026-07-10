from _typeshed import Incomplete
from pyscf import dft as dft, lib as lib
from pyscf.dft import numint as numint
from pyscf.hessian import rhf as rhf_hess, uhf as uhf_hess
from pyscf.lib import logger as logger
from numpy import ndarray
from pyscf.dft.uks import UKS
from pyscf.lib.logger import Logger
from typing import List, Optional, Tuple, Union

def partial_hess_elec(hessobj: "Hessian", mo_energy: Optional[ndarray]=None, mo_coeff: Optional[ndarray]=None, mo_occ: Optional[ndarray]=None, atmlst: Optional[Union[range, List[int]]]=None, max_memory: int = 4000, verbose: Optional[Logger]=None) -> ndarray: ...
def make_h1(hessobj: "Hessian", mo_coeff: ndarray, mo_occ: ndarray, chkfile: None=None, atmlst: Optional[Union[range, List[int]]]=None, verbose: Optional[Logger]=None) -> Tuple[ndarray, ndarray]: ...

XX: Incomplete
XY: Incomplete
XZ: Incomplete
YX: Incomplete
YY: Incomplete
YZ: Incomplete
ZX: Incomplete
ZY: Incomplete
ZZ: Incomplete
XXX: Incomplete
XXY: Incomplete
XXZ: Incomplete
XYY: Incomplete
XYZ: Incomplete
XZZ: Incomplete
YYY: Incomplete
YYZ: Incomplete
YZZ: Incomplete
ZZZ: Incomplete

class Hessian(rhf_hess.HessianBase):
    grids: Incomplete
    grid_response: bool
    def __init__(self, mf: UKS) -> None: ...
    hess_elec = uhf_hess.hess_elec
    gen_hop = uhf_hess.gen_hop
    solve_mo1: Incomplete
    partial_hess_elec = partial_hess_elec
    make_h1 = make_h1
