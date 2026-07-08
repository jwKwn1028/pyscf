from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.lib import logger as logger
from pyscf.pbc.dft import gen_grid as gen_grid, krks as krks, multigrid as multigrid, rks as rks
from pyscf.pbc.dft.numint2c import KNumInt2C as KNumInt2C
from pyscf.pbc.scf import kghf as kghf, khf as khf
from numpy import ndarray
from pyscf.lib.numpy_helper import NPArrayWithTag
from pyscf.pbc.gto.cell import Cell
from pyscf.pbc.scf.kghf import KGHF
from typing import Optional, Union

def get_veff(ks: "KGKS", cell: Optional[Cell]=None, dm: Optional[Union[ndarray, NPArrayWithTag]]=None, dm_last: Union[ndarray, NPArrayWithTag, int] = 0, vhf_last: Union[NPArrayWithTag, int] = 0, hermi: int = 1, kpts: None=None, kpts_band: None=None) -> NPArrayWithTag: ...

class KGKS(rks.KohnShamDFT, kghf.KGHF):
    collinear: Incomplete
    spin_samples: Incomplete
    get_veff = get_veff
    energy_elec = krks.energy_elec
    get_rho = krks.get_rho
    def __init__(self, cell: Cell, kpts: Optional[ndarray]=None, xc: str = 'LDA,VWN', exxdiv: str=...) -> None: ...
    def dump_flags(self, verbose: None=None) -> "KGKS": ...
    def x2c1e(self): ...
    x2c = x2c1e
    def stability(self) -> None: ...
    def nuc_grad_method(self) -> None: ...
    def to_hf(self) -> KGHF: ...
    to_gpu = lib.to_gpu
