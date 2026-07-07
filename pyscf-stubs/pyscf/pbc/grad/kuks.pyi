from _typeshed import Incomplete
from pyscf import lib as lib
from pyscf.dft import numint as numint
from pyscf.lib import logger as logger
from pyscf.pbc import gto as gto
from pyscf.pbc.grad import kuhf as uhf_grad

def get_veff(ks_grad, dm=None, kpts=None): ...
def get_vxc(ni, cell, grids, xc_code, dms, kpts, kpts_band=None, relativity: int = 0, hermi: int = 1, max_memory: int = 2000, verbose=None): ...

class Gradients(uhf_grad.Gradients):
    grids: Incomplete
    grid_response: bool
    def __init__(self, mf) -> None: ...
    get_veff = get_veff
    def get_stress(self): ...
