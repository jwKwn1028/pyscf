from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.lib import logger as logger
from pyscf.pbc.dft import gen_grid as gen_grid, krks as krks, multigrid as multigrid, rks as rks, uks as uks
from pyscf.pbc.dft.krks import get_rho as get_rho
from pyscf.pbc.scf import khf as khf, kuhf as kuhf
from numpy import float64, ndarray
from pyscf.lib.numpy_helper import NPArrayWithTag
from pyscf.pbc.dft.kroks import KROKS
from pyscf.pbc.dft.kukspu import KUKSpU
from pyscf.pbc.grad.kuks import Gradients
from pyscf.pbc.gto.cell import Cell
from pyscf.pbc.scf.kuhf import KUHF
from typing import Callable, Optional, Tuple, Union

def get_veff(ks: Union[KROKS, KUKS, KUKSpU], cell: Optional[Cell]=None, dm: Optional[Union[Tuple[ndarray, ndarray], NPArrayWithTag, ndarray]]=None, dm_last: Union[ndarray, NPArrayWithTag, int] = 0, vhf_last: Union[NPArrayWithTag, int] = 0, hermi: int = 1, kpts: Optional[ndarray]=None, kpts_band: None=None) -> NPArrayWithTag: ...
def energy_elec(mf: "KUKS", dm_kpts: Optional[Union[ndarray, NPArrayWithTag]]=None, h1e_kpts: Optional[ndarray]=None, vhf: Optional[NPArrayWithTag]=None) -> Tuple[float64, float64]: ...
def gen_response(mf: "KUKS", mo_coeff: None=None, mo_occ: None=None, with_j: bool = True, hermi: int = 0, max_memory: Optional[float]=None, with_nlc: bool = True) -> Callable: ...

class KUKS(rks.KohnShamDFT, kuhf.KUHF):
    get_veff = get_veff
    energy_elec = energy_elec
    get_rho = get_rho
    gen_response = gen_response
    initialize_grids: Incomplete
    def __init__(self, cell: Cell, kpts: Optional[ndarray]=None, xc: str = 'LDA,VWN', exxdiv: str=...) -> None: ...
    def dump_flags(self, verbose: None=None) -> Union[KUKS, KUKSpU]: ...
    def Gradients(self) -> Gradients: ...
    def to_hf(self) -> KUHF: ...
    multigrid_numint: Incomplete
    to_gpu = lib.to_gpu
