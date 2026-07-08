from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.lib import logger as logger
from pyscf.pbc.dft import gen_grid as gen_grid, multigrid as multigrid, rks as rks
from pyscf.pbc.dft.numint2c import NumInt2C as NumInt2C
from pyscf.pbc.scf import ghf as pbcghf
from numpy import ndarray
from pyscf.lib.numpy_helper import NPArrayWithTag
from pyscf.pbc.gto.cell import Cell
from typing import Optional, Union

def get_veff(ks: "GKS", cell: Optional[Cell]=None, dm: Optional[Union[NPArrayWithTag, ndarray]]=None, dm_last: Union[ndarray, int, NPArrayWithTag] = 0, vhf_last: Union[NPArrayWithTag, int] = 0, hermi: int = 1, kpt: None=None, kpts_band: None=None) -> NPArrayWithTag: ...

class GKS(rks.KohnShamDFT, pbcghf.GHF):
    collinear: Incomplete
    spin_samples: Incomplete
    get_veff = get_veff
    energy_elec: Incomplete
    def __init__(self, cell: Cell, kpt: None=None, xc: str = 'LDA,VWN', exxdiv: str=...) -> None: ...
    def dump_flags(self, verbose: None=None) -> "GKS": ...
    def x2c1e(self): ...
    x2c = x2c1e
    def stability(self) -> None: ...
    def nuc_grad_method(self) -> None: ...
    def to_hf(self): ...
    to_gpu = lib.to_gpu
