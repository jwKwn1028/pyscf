from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.pbc.dft import kuks as kuks, rks as rks
from pyscf.pbc.dft.kuks import energy_elec as energy_elec
from pyscf.pbc.scf import krohf as krohf
from numpy import ndarray
from pyscf.lib.numpy_helper import NPArrayWithTag
from pyscf.pbc.gto.cell import Cell
from pyscf.pbc.scf.krohf import KROHF
from typing import Optional

def get_veff(ks: "KROKS", cell: Optional[Cell]=None, dm: Optional[NPArrayWithTag]=None, dm_last: int = 0, vhf_last: int = 0, hermi: int = 1, kpts: Optional[ndarray]=None, kpts_band: None=None) -> NPArrayWithTag: ...

class KROKS(rks.KohnShamDFT, krohf.KROHF):
    get_veff = get_veff
    energy_elec = energy_elec
    get_rho = kuks.get_rho
    def __init__(self, cell: Cell, kpts: Optional[ndarray]=None, xc: str = 'LDA,VWN', exxdiv: str=...) -> None: ...
    def dump_flags(self, verbose=None): ...
    def to_hf(self) -> KROHF: ...
    multigrid_numint: Incomplete
    to_gpu = lib.to_gpu
