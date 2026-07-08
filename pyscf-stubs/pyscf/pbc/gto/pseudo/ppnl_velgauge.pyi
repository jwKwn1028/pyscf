from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.lib import logger as logger
from pyscf.pbc.df.ft_ao import ExtendedMole as ExtendedMole, estimate_rcut as estimate_rcut
from pyscf.pbc.gto.pseudo.pp_int import fake_cell_vnl as fake_cell_vnl
from pyscf.pbc.tools import k2gamma as k2gamma
from numpy import ndarray
from pyscf.pbc.gto.cell import Cell
from typing import Callable, List, Optional, Tuple

RCUT_THRESHOLD: Incomplete
KECUT_THRESHOLD: Incomplete
libpbc: Incomplete

def get_gth_pp_nl_velgauge(cell: Cell, q: ndarray, kpts: Optional[ndarray]=None, vgppnl_helper: None=None) -> ndarray: ...
def get_gth_pp_nl_velgauge_commutator(cell: Cell, q: ndarray, kpts: Optional[ndarray]=None, vgppnl_helper: None=None) -> ndarray: ...

class VelGaugePPNLHelper:
    kpts: Incomplete
    nkpts: Incomplete
    cell: Incomplete
    origin: Incomplete
    fakecell: Incomplete
    hl_blocks: Incomplete
    intors: Incomplete
    comm_intors: Incomplete
    ft_data: Incomplete
    hl_max: Incomplete
    hl_dims: Incomplete
    def __init__(self, cell: Cell, kpts: Optional[ndarray]=None, intors: None=None, hl_max: int = 3, origin: Tuple[float, float, float]=(0.0, 0.0, 0.0)) -> None: ...
    def build(self) -> None: ...
    def int_vnl_ft(self, Gv: ndarray, q: ndarray=..., rc: bool = False) -> Tuple[ndarray, ndarray, ndarray]: ...

def prepare_ppnl_ft_data(cell: Cell, fakecell: Cell, hl_idx: int, hl_blocks: List[ndarray], kpts: ndarray, intor: str, origin: Tuple[float, float, float]=(0.0, 0.0, 0.0), comp: int = 1) -> Tuple[Tuple[int, int, int, int], Callable, Cell]: ...
def ft_aopair_kpts_kern(cell: Cell, aosym: str = 's1', kptjs: ndarray=..., intor: str = 'GTO_ft_ovlp', comp: int = 1, bvk_kmesh: None=None, origin: Tuple[float, float, float]=(0.0, 0.0, 0.0)) -> Callable: ...
