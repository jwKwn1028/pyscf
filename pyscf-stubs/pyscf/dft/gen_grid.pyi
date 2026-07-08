from _typeshed import Incomplete
from pyscf import __config__ as __config__, gto as gto, lib as lib
from pyscf.dft import radi as radi
from pyscf.dft.LebedevGrid import LEBEDEV_NGRID as LEBEDEV_NGRID, LEBEDEV_ORDER as LEBEDEV_ORDER, MakeAngularGrid as MakeAngularGrid
from pyscf.gto.eval_gto import BLKSIZE as BLKSIZE, CUTOFF as CUTOFF, NBINS as NBINS, make_screen_index as make_screen_index
from pyscf.lib import logger as logger
from numpy import int64, ndarray
from pyscf.gto.mole import Mole
from pyscf.lib.logger import Logger
from pyscf.pbc.dft.gen_grid import BeckeGrids
from pyscf.pbc.gto.cell import Cell
from typing import Any, Callable, Dict, Optional, Tuple, Union

libdft: Incomplete
GROUP_BOX_SIZE: float
GROUP_BOUNDARY_PENALTY: float
ALIGNMENT_UNIT: int
NELEC_ERROR_TOL: Incomplete

def sg1_prune(nuc: int, rads: ndarray, n_ang: int, radii: ndarray=...) -> ndarray: ...
def nwchem_prune(nuc: int, rads: ndarray, n_ang: int, radii: ndarray=...) -> ndarray: ...
def treutler_prune(nuc: int, rads: ndarray, n_ang: int, radii: None=None) -> ndarray: ...

SGX_ANG_MAPPING: Incomplete

def sgx_prune(nuc, rads, n_ang, radii=...): ...
def stratmann(g: ndarray) -> ndarray: ...
def original_becke(g) -> None: ...
def becke_lko(g) -> None: ...
def gen_atomic_grids(mol: Union[Cell, Mole], atom_grid: Union[Dict[str, Tuple[int, int]], Tuple[int, int]]={}, radi_method: Callable=..., level: int = 3, prune: Optional[Callable]=..., **kwargs) -> Dict[str, Tuple[ndarray, ndarray]]: ...
def get_partition(mol: Union[Cell, Mole], atom_grids_tab: Dict[str, Tuple[ndarray, ndarray]], radii_adjust: Optional[Callable]=None, atomic_radii: ndarray=..., becke_scheme: Callable=..., concat: bool = True) -> Tuple[ndarray, ndarray]: ...
gen_partition = get_partition

def make_mask(mol: Union[Cell, Mole], coords: ndarray, relativity: int = 0, shls_slice: None=None, cutoff: float=..., verbose: None=None) -> ndarray: ...
def arg_group_grids(mol: Union[Cell, Mole], coords: ndarray, box_size: float=...) -> ndarray: ...

class Grids(lib.StreamObject):
    atomic_radii: Incomplete
    radii_adjust: Incomplete
    radi_method: Incomplete
    becke_scheme: Incomplete
    prune: Incomplete
    level: Incomplete
    alignment = ALIGNMENT_UNIT
    cutoff = CUTOFF
    mol: Incomplete
    stdout: Incomplete
    verbose: Incomplete
    symmetry: Incomplete
    atom_grid: Incomplete
    non0tab: Incomplete
    screen_index: Incomplete
    coords: Incomplete
    weights: Incomplete
    atm_idx: Incomplete
    quadrature_weights: Incomplete
    def __init__(self, mol: Union[Cell, Mole]) -> None: ...
    @property
    def size(self) -> int: ...
    def __setattr__(self, key: str, val: Any) -> None: ...
    def dump_flags(self, verbose: Optional[Logger]=None) -> Union[BeckeGrids, Grids]: ...
    def build(self, mol: None=None, with_non0tab: bool = False, sort_grids: bool = True, **kwargs) -> "Grids": ...
    def kernel(self, mol: None=None, with_non0tab: bool = False) -> "Grids": ...
    def reset(self, mol: Optional[Mole]=None) -> Union[BeckeGrids, Grids]: ...
    gen_atomic_grids: Incomplete
    def get_partition(self, mol: Union[Cell, Mole], atom_grids_tab: Optional[Dict[str, Tuple[ndarray, ndarray]]]=None, radii_adjust: Optional[Callable]=None, atomic_radii: ndarray=..., becke_scheme: Callable=..., concat: bool = True) -> Tuple[ndarray, ndarray]: ...
    gen_partition = get_partition
    make_mask: Incomplete
    def prune_by_density_(self, rho: ndarray, threshold: float = 0) -> "Grids": ...
    to_gpu = lib.to_gpu

RAD_GRIDS: Incomplete
ANG_ORDER: Incomplete
