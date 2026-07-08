from pyscf import __config__ as __config__, lib as lib
from pyscf.lib import logger as logger
from pyscf.pbc.dft import gen_grid as gen_grid, multigrid as multigrid, rks as rks
from pyscf.pbc.scf import khf as khf
from numpy import float64, int64, ndarray
from pyscf.lib.numpy_helper import NPArrayWithTag
from pyscf.pbc.dft.gen_grid import UniformGrids
from pyscf.pbc.dft.kgks import KGKS
from pyscf.pbc.dft.krks_ksymm import KsymAdaptedKRKS
from pyscf.pbc.dft.krkspu import KRKSpU
from pyscf.pbc.dft.kuks import KUKS
from pyscf.pbc.dft.kuks_ksymm import KsymAdaptedKUKS
from pyscf.pbc.dft.rks import KohnShamDFT
from pyscf.pbc.grad.krks import Gradients
from pyscf.pbc.gto.cell import Cell
from pyscf.pbc.lib.kpts import KPoints
from pyscf.pbc.scf.khf import KRHF
from typing import Callable, Optional, Tuple, Union

def get_veff(ks: Union[KRKS, KRKSpU], cell: Optional[Cell]=None, dm: Optional[Union[NPArrayWithTag, ndarray]]=None, dm_last: Union[ndarray, int, NPArrayWithTag] = 0, vhf_last: Union[int, NPArrayWithTag] = 0, hermi: int = 1, kpts: Optional[ndarray]=None, kpts_band: Optional[ndarray]=None) -> NPArrayWithTag: ...
def get_rho(mf: Union[KRKS, KsymAdaptedKUKS, KsymAdaptedKRKS, KUKS], dm: Optional[NPArrayWithTag]=None, grids: Optional[UniformGrids]=None, kpts: None=None) -> ndarray: ...
def energy_elec(mf: Union[KRKS, KGKS], dm_kpts: Optional[Union[ndarray, NPArrayWithTag]]=None, h1e_kpts: Optional[ndarray]=None, vhf: Optional[NPArrayWithTag]=None) -> Tuple[float64, float64]: ...
def gen_response(mf: "KRKS", mo_coeff: Optional[ndarray]=None, mo_occ: Optional[ndarray]=None, singlet: Optional[bool]=None, hermi: int = 0, max_memory: Optional[float]=None, with_nlc: bool = True) -> Callable: ...

class KRKS(rks.KohnShamDFT, khf.KRHF):
    get_veff = get_veff
    energy_elec = energy_elec
    get_rho = get_rho
    gen_response = gen_response
    def __init__(self, cell: Cell, kpts: Optional[ndarray]=None, xc: str = 'LDA,VWN', exxdiv: str=...) -> None: ...
    def dump_flags(self, verbose: None=None) -> Union[KRKS, KRKSpU]: ...
    def Gradients(self) -> Gradients: ...
    def to_hf(self) -> KRHF: ...
    def multigrid_numint(self, mesh: None=None) -> Union[KRKS, KsymAdaptedKUKS, KsymAdaptedKRKS, KUKS]: ...
    to_gpu = lib.to_gpu
