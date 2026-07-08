import pyscf.dft
from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.pbc.dft import rks as rks, uks as uks
from pyscf.pbc.scf import rohf as rohf
from pyscf.lib.numpy_helper import NPArrayWithTag
from pyscf.pbc.gto.cell import Cell
from typing import Optional

def get_veff(ks: "ROKS", cell: Optional[Cell]=None, dm: Optional[NPArrayWithTag]=None, dm_last: int = 0, vhf_last: int = 0, hermi: int = 1, kpt: None=None, kpts_band: None=None) -> NPArrayWithTag: ...

class ROKS(rks.KohnShamDFT, rohf.ROHF):
    get_vsap: Incomplete
    init_guess_by_vsap: Incomplete
    get_veff = get_veff
    energy_elec = pyscf.dft.uks.energy_elec
    def __init__(self, cell: Cell, kpt: None=None, xc: str = 'LDA,VWN', exxdiv: str=...) -> None: ...
    def dump_flags(self, verbose=None): ...
    def to_hf(self): ...
    multigrid_numint: Incomplete
    to_gpu = lib.to_gpu
