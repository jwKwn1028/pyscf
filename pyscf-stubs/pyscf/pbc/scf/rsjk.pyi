from _typeshed import Incomplete
from pyscf import __config__ as __config__, gto as gto, lib as lib
from pyscf.lib import logger as logger
from pyscf.pbc.df import aft as aft, aft_jk as aft_jk, ft_ao as ft_ao, rsdf_builder as rsdf_builder
from pyscf.pbc.df.df_jk import zdotCN as zdotCN, zdotNC as zdotNC, zdotNN as zdotNN
from pyscf.pbc.df.incore import LOG_ADJUST as LOG_ADJUST, libpbc as libpbc, verify_cint_backend as verify_cint_backend
from pyscf.pbc.lib.kpts_helper import group_by_conj_pairs as group_by_conj_pairs, intersection as intersection, is_zero as is_zero, kk_adapted_iter as kk_adapted_iter
from pyscf.pbc.scf import addons as addons
from pyscf.pbc.tools import k2gamma as k2gamma
from numpy import bool, float64, ndarray
from pyscf.lib.numpy_helper import NPArrayWithTag
from pyscf.pbc.df.ft_ao import _RangeSeparatedCell
from pyscf.pbc.gto.cell import Cell
from typing import Optional, Tuple, Union

RCUT_THRESHOLD: Incomplete
OMEGA_MIN: Incomplete
INDEX_MIN: Incomplete

class RangeSeparatedJKBuilder(lib.StreamObject):
    cell: Incomplete
    stdout: Incomplete
    verbose: Incomplete
    max_memory: Incomplete
    mesh: Incomplete
    kpts: Incomplete
    purify: bool
    omega: Incomplete
    rs_cell: Incomplete
    cell_d: Incomplete
    bvk_kmesh: Incomplete
    supmol_sr: Incomplete
    supmol_ft: Incomplete
    supmol_d: Incomplete
    cell0_basis_mask: Incomplete
    ke_cutoff: Incomplete
    direct_scf_tol: Incomplete
    time_reversal_symmetry: bool
    exclude_dd_block: bool
    allow_drv_nodddd: bool
    approx_vk_lr_missing_mo: bool
    def __init__(self, cell: Cell, kpts: ndarray=...) -> None: ...
    def has_long_range(self) -> bool: ...
    def dump_flags(self, verbose=None): ...
    def reset(self, cell: None=None) -> "RangeSeparatedJKBuilder": ...
    def build(self, omega: None=None, intor: str = 'int2e') -> "RangeSeparatedJKBuilder": ...
    @property
    def qindex(self): ...
    @qindex.setter
    def qindex(self, x) -> None: ...
    def get_jk(self, dm_kpts: Union[ndarray, NPArrayWithTag], hermi: int = 1, kpts: Optional[ndarray]=None, kpts_band: None=None, with_j: bool = True, with_k: bool = True, omega: None=None, exxdiv: Optional[str]=None) -> Union[Tuple[ndarray, ndarray], Tuple[ndarray, None], Tuple[None, ndarray]]: ...
    weighted_coulG = aft.weighted_coulG
    def weighted_coulG_LR(self, kpt=..., exx: bool = False, mesh=None): ...
    def weighted_coulG_SR(self, kpt: ndarray=..., exx: bool = False, mesh: Optional[ndarray]=None) -> ndarray: ...
    to_gpu = lib.to_gpu
RangeSeparationJKBuilder = RangeSeparatedJKBuilder

def estimate_rcut(rs_cell: _RangeSeparatedCell, omega: float64, precision: None=None, exclude_dd_block: bool = True) -> ndarray: ...
def estimate_ke_cutoff_for_omega(cell: Cell, omega: Union[float, float64], precision: None=None) -> float64: ...
def estimate_omega_for_ke_cutoff(cell: Cell, ke_cutoff: float64, precision: Optional[float]=None) -> float64: ...
