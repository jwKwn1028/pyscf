import pyscf.dft
from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.lib import logger as logger
from pyscf.pbc.dft import gen_grid as gen_grid, multigrid as multigrid, rks as rks
from pyscf.pbc.scf import uhf as pbcuhf
from numpy import ndarray
from pyscf.lib.numpy_helper import NPArrayWithTag
from pyscf.pbc.dft.kuks import KUKS
from pyscf.pbc.dft.kuks_ksymm import KsymAdaptedKUKS
from pyscf.pbc.dft.kukspu import KUKSpU
from pyscf.pbc.dft.kukspu_ksymm import KsymAdaptedKUKSpU
from pyscf.pbc.dft.roks import ROKS
from pyscf.pbc.gto.cell import Cell
from pyscf.pbc.lib.kpts import KPoints
from typing import Callable, Optional, Tuple, Union

get_rho = rks.get_rho

def get_veff(ks: Union[UKS, ROKS], cell: Optional[Cell]=None, dm: Optional[Union[ndarray, Tuple[ndarray, ndarray], NPArrayWithTag]]=None, dm_last: Union[ndarray, int, NPArrayWithTag] = 0, vhf_last: Union[int, NPArrayWithTag] = 0, hermi: int = 1, kpt: None=None, kpts_band: None=None) -> NPArrayWithTag: ...
def gen_response(mf: "UKS", mo_coeff: Optional[Union[ndarray, Tuple[ndarray, ndarray]]]=None, mo_occ: Optional[Union[ndarray, Tuple[ndarray, ndarray]]]=None, with_j: bool = True, hermi: int = 0, max_memory: Optional[float]=None, with_nlc: bool = True) -> Callable: ...

class UKS(rks.KohnShamDFT, pbcuhf.UHF):
    get_rho = get_rho
    get_vsap: Incomplete
    init_guess_by_vsap: Incomplete
    get_veff = get_veff
    energy_elec = pyscf.dft.uks.energy_elec
    gen_response = gen_response
    def __init__(self, cell: Cell, kpt: Optional[ndarray]=None, xc: str = 'LDA,VWN', exxdiv: str=...) -> None: ...
    def dump_flags(self, verbose: None=None) -> "UKS": ...
    def initialize_grids(self, cell: Cell, dm: Union[ndarray, NPArrayWithTag], kpts: Union[ndarray, KPoints], ground_state: bool = True) -> Union[UKS, KUKS, KUKSpU, KsymAdaptedKUKSpU, KsymAdaptedKUKS]: ...
    def to_hf(self): ...
    def Gradients(self): ...
    multigrid_numint: Incomplete
    to_gpu = lib.to_gpu
