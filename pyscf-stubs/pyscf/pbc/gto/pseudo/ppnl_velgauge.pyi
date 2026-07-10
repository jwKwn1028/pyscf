from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.lib import logger as logger
from pyscf.pbc.df.ft_ao import ExtendedMole as ExtendedMole, estimate_rcut as estimate_rcut
from pyscf.pbc.gto.pseudo.pp_int import fake_cell_vnl as fake_cell_vnl
from pyscf.pbc.tools import k2gamma as k2gamma

RCUT_THRESHOLD: Incomplete
KECUT_THRESHOLD: Incomplete
libpbc: Incomplete

def get_gth_pp_nl_velgauge(cell, q, kpts=None, vgppnl_helper=None): ...
def get_gth_pp_nl_velgauge_commutator(cell, q, kpts=None, vgppnl_helper=None): ...

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
    def __init__(self, cell, kpts=None, intors=None, hl_max: int = 3, origin=(0.0, 0.0, 0.0)) -> None: ...
    def build(self) -> None: ...
    def int_vnl_ft(self, Gv, q=..., rc: bool = False): ...

def prepare_ppnl_ft_data(cell, fakecell, hl_idx, hl_blocks, kpts, intor, origin=(0.0, 0.0, 0.0), comp: int = 1): ...
def ft_aopair_kpts_kern(cell, aosym: str = 's1', kptjs=..., intor: str = 'GTO_ft_ovlp', comp: int = 1, bvk_kmesh=None, origin=(0.0, 0.0, 0.0)): ...
