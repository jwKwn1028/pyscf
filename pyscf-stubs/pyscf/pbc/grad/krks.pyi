from _typeshed import Incomplete
from pyscf import lib as lib
from pyscf.dft import numint as numint
from pyscf.lib import logger as logger
from pyscf.pbc.grad import krhf as rhf_grad
from numpy import ndarray
from pyscf.lib.numpy_helper import NPArrayWithTag
from pyscf.pbc.dft.gen_grid import UniformGrids
from pyscf.pbc.dft.krks import KRKS
from pyscf.pbc.dft.krkspu import KRKSpU
from pyscf.pbc.dft.numint import KNumInt
from pyscf.pbc.gto.cell import Cell
from typing import Optional, Union

def get_veff(ks_grad: "Gradients", dm: Optional[NPArrayWithTag]=None, kpts: Optional[ndarray]=None) -> ndarray: ...
def get_vxc(ni: KNumInt, cell: Cell, grids: UniformGrids, xc_code: str, dms: NPArrayWithTag, kpts: ndarray, kpts_band: None=None, relativity: int = 0, hermi: int = 1, max_memory: float = 2000, verbose: Optional[int]=None) -> ndarray: ...

class Gradients(rhf_grad.Gradients):
    grids: Incomplete
    grid_response: bool
    def __init__(self, mf: Union[KRKS, KRKSpU]) -> None: ...
    def reset(self, cell=None): ...
    def dump_flags(self, verbose=None): ...
    get_veff = get_veff
    def get_stress(self) -> ndarray: ...
