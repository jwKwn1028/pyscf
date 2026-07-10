import pyscf.dft
from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.pbc.dft import rks as rks, uks as uks
from pyscf.pbc.scf import rohf as rohf

def get_veff(ks, cell=None, dm=None, dm_last: int = 0, vhf_last: int = 0, hermi: int = 1, kpt=None, kpts_band=None): ...

class ROKS(rks.KohnShamDFT, rohf.ROHF):
    get_vsap: Incomplete
    init_guess_by_vsap: Incomplete
    get_veff = get_veff
    energy_elec = pyscf.dft.uks.energy_elec
    def __init__(self, cell, kpt=None, xc: str = 'LDA,VWN', exxdiv=...) -> None: ...
    def dump_flags(self, verbose=None): ...
    def to_hf(self): ...
    multigrid_numint: Incomplete
    to_gpu = lib.to_gpu
