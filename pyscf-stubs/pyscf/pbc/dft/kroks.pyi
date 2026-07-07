from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.pbc.dft import kuks as kuks, rks as rks
from pyscf.pbc.dft.kuks import energy_elec as energy_elec
from pyscf.pbc.scf import krohf as krohf

def get_veff(ks, cell=None, dm=None, dm_last: int = 0, vhf_last: int = 0, hermi: int = 1, kpts=None, kpts_band=None): ...

class KROKS(rks.KohnShamDFT, krohf.KROHF):
    get_veff = get_veff
    energy_elec = energy_elec
    get_rho = kuks.get_rho
    def __init__(self, cell, kpts=None, xc: str = 'LDA,VWN', exxdiv=...) -> None: ...
    def dump_flags(self, verbose=None): ...
    def to_hf(self): ...
    multigrid_numint: Incomplete
    to_gpu = lib.to_gpu
