from pyscf import lib as lib
from pyscf.dft import gks as gks, rks as rks
from pyscf.dft.numint2c import NumInt2C as NumInt2C
from pyscf.lib import logger as logger
from pyscf.scf import ghf_symm as ghf_symm

class GKS(rks.KohnShamDFT, ghf_symm.GHF):
    def __init__(self, mol, xc: str = 'LDA,VWN') -> None: ...
    def dump_flags(self, verbose=None): ...
    get_veff = gks.get_veff
    energy_elec = rks.energy_elec
    @property
    def collinear(self): ...
    @collinear.setter
    def collinear(self, val) -> None: ...
    def nuc_grad_method(self) -> None: ...
    to_gpu = lib.to_gpu
