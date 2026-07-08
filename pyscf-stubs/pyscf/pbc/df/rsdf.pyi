from _typeshed import Incomplete
from pyscf import lib as lib
from pyscf.df.addons import make_auxmol as make_auxmol
from pyscf.lib import logger as logger, zdotCN as zdotCN
from pyscf.pbc.df import aft as aft, aft_jk as aft_jk, ft_ao as ft_ao, gdf_builder as gdf_builder, rsdf_builder as rsdf_builder, rsdf_helper as rsdf_helper
from pyscf.pbc.df.df import GDF as GDF
from pyscf.pbc.df.incore import Int3cBuilder as Int3cBuilder
from pyscf.pbc.lib.kpts_helper import is_zero as is_zero, member as member, members_with_wrap_around as members_with_wrap_around, unique as unique
from pyscf.pbc.tools import k2gamma as k2gamma
from numpy import ndarray
from pyscf.lib.misc import H5TmpFile
from pyscf.pbc.gto.cell import Cell
from typing import Callable, List, Optional, Tuple, Union

def get_aux_chg(auxcell: Cell) -> ndarray: ...

class RSGDF(GDF):
    def weighted_coulG(self, kpt=..., exx: bool = False, mesh=None, omega=None): ...
    use_bvk: bool
    precision_R: Incomplete
    precision_G: Incomplete
    npw_max: int
    omega: Incomplete
    ke_cutoff: Incomplete
    mesh_compact: Incomplete
    omega_j2c: float
    mesh_j2c: Incomplete
    precision_j2c: float
    j2c_eig_always: bool
    kpts: Incomplete
    def __init__(self, cell: Cell, kpts: Union[ndarray, List[ndarray]]=...) -> None: ...
    def dump_flags(self, verbose: None=None) -> "RSGDF": ...
    def build(self, j_only: Optional[bool]=None, with_j3c: bool = True, kpts_band: None=None) -> "RSGDF": ...
RSDF = RSGDF

class _RSGDFBuilder(rsdf_builder._RSGDFBuilder):
    eta: Incomplete
    mesh: Incomplete
    omega: Incomplete
    ke_cutoff: Incomplete
    bvk_kmesh: Incomplete
    supmol_ft: Incomplete
    j2c_eig_always: bool
    linear_dep_threshold: Incomplete
    def __init__(self, cell: Cell, auxcell: Cell, kpts: ndarray=...) -> None: ...
    rs_cell: Incomplete
    def build(self, omega: None=None) -> "_RSGDFBuilder": ...
    def get_2c2e(self, uniq_kpts: ndarray) -> List[ndarray]: ...
    def outcore_auxe2(self, cderi_file: str, intor: str = 'int3c2e', aosym: str = 's2', comp: None=None, kptij_lst: Optional[ndarray]=None, j_only: bool = False, dataname: str = 'j3c-junk', shls_slice: None=None) -> H5TmpFile: ...
    def weighted_ft_ao(self, kpt: ndarray) -> Tuple[ndarray, ndarray]: ...
    def gen_j3c_loader(self, h5group: H5TmpFile, kpt: ndarray, kpt_ij_idx: ndarray, ijlst_mapping: ndarray, aosym: str) -> Callable: ...
    def make_j3c(self, cderi_file: str, intor: str = 'int3c2e', aosym: str = 's2', comp: None=None, j_only: bool = False, dataname: str = 'j3c', shls_slice: None=None, kptij_lst: None=None) -> "_RSGDFBuilder": ...
