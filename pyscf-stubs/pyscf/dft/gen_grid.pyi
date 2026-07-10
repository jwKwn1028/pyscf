from _typeshed import Incomplete
from pyscf import __config__ as __config__, gto as gto, lib as lib
from pyscf.dft import radi as radi
from pyscf.dft.LebedevGrid import LEBEDEV_NGRID as LEBEDEV_NGRID, LEBEDEV_ORDER as LEBEDEV_ORDER, MakeAngularGrid as MakeAngularGrid
from pyscf.gto.eval_gto import BLKSIZE as BLKSIZE, CUTOFF as CUTOFF, NBINS as NBINS, make_screen_index as make_screen_index
from pyscf.lib import logger as logger

libdft: Incomplete
GROUP_BOX_SIZE: float
GROUP_BOUNDARY_PENALTY: float
ALIGNMENT_UNIT: int
NELEC_ERROR_TOL: Incomplete

def sg1_prune(nuc, rads, n_ang, radii=...): ...
def nwchem_prune(nuc, rads, n_ang, radii=...): ...
def treutler_prune(nuc, rads, n_ang, radii=None): ...

SGX_ANG_MAPPING: Incomplete

def sgx_prune(nuc, rads, n_ang, radii=...): ...
def stratmann(g): ...
def original_becke(g) -> None: ...
def becke_lko(g) -> None: ...
def gen_atomic_grids(mol, atom_grid={}, radi_method=..., level: int = 3, prune=..., **kwargs): ...
def get_partition(mol, atom_grids_tab, radii_adjust=None, atomic_radii=..., becke_scheme=..., concat: bool = True): ...
gen_partition = get_partition

def make_mask(mol, coords, relativity: int = 0, shls_slice=None, cutoff=..., verbose=None): ...
def arg_group_grids(mol, coords, box_size=...): ...

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
    def __init__(self, mol) -> None: ...
    @property
    def size(self): ...
    def __setattr__(self, key, val) -> None: ...
    def dump_flags(self, verbose=None): ...
    def build(self, mol=None, with_non0tab: bool = False, sort_grids: bool = True, **kwargs): ...
    def kernel(self, mol=None, with_non0tab: bool = False): ...
    def reset(self, mol=None): ...
    gen_atomic_grids: Incomplete
    def get_partition(self, mol, atom_grids_tab=None, radii_adjust=None, atomic_radii=..., becke_scheme=..., concat: bool = True): ...
    gen_partition = get_partition
    make_mask: Incomplete
    def prune_by_density_(self, rho, threshold: int = 0): ...
    to_gpu = lib.to_gpu

RAD_GRIDS: Incomplete
ANG_ORDER: Incomplete
