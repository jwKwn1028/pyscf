from _typeshed import Incomplete
from pyscf import dft as dft, lib as lib
from pyscf.dft import numint as numint
from pyscf.hessian import rhf as rhf_hess, uhf as uhf_hess
from pyscf.lib import logger as logger

def partial_hess_elec(hessobj, mo_energy=None, mo_coeff=None, mo_occ=None, atmlst=None, max_memory: int = 4000, verbose=None): ...
def make_h1(hessobj, mo_coeff, mo_occ, chkfile=None, atmlst=None, verbose=None): ...

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
    def __init__(self, mf) -> None: ...
    hess_elec = uhf_hess.hess_elec
    gen_hop = uhf_hess.gen_hop
    solve_mo1: Incomplete
    partial_hess_elec = partial_hess_elec
    make_h1 = make_h1
