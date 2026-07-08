from _typeshed import Incomplete
from pyscf import lib as lib
from pyscf.dft import numint as numint
from pyscf.lib import logger as logger
from pyscf.pbc import gto as gto
from pyscf.pbc.grad import kuhf as uhf_grad
from numpy import ndarray
from pyscf.lib.numpy_helper import NPArrayWithTag
from pyscf.pbc.dft.gen_grid import UniformGrids
from pyscf.pbc.dft.kuks import KUKS
from pyscf.pbc.dft.kukspu import KUKSpU
from pyscf.pbc.dft.numint import KNumInt
from pyscf.pbc.gto.cell import Cell
from typing import Optional, Union

def get_veff(ks_grad, dm=None, kpts=None): ...
def get_vxc(ni: KNumInt, cell: Cell, grids: UniformGrids, xc_code: str, dms: NPArrayWithTag, kpts: ndarray, kpts_band: None=None, relativity: int = 0, hermi: int = 1, max_memory: float = 2000, verbose: Optional[int]=None) -> ndarray: ...

class Gradients(uhf_grad.Gradients):
    grids: Incomplete
    grid_response: bool
    def __init__(self, mf: Union[KUKSpU, KUKS]) -> None: ...
    get_veff = get_veff
    def get_stress(self) -> ndarray: ...
