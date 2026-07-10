from pyscf import lib as lib
from pyscf.dft import rks as rks, uks as uks
from pyscf.dft.uks import energy_elec as energy_elec
from pyscf.scf import rohf as rohf

def get_veff(ks, mol=None, dm=None, dm_last: int = 0, vhf_last: int = 0, hermi: int = 1): ...

class ROKS(rks.KohnShamDFT, rohf.ROHF):
    def __init__(self, mol, xc: str = 'LDA,VWN') -> None: ...
    def dump_flags(self, verbose=None): ...
    get_veff = get_veff
    get_vsap = rks.get_vsap
    energy_elec = energy_elec
    init_guess_by_vsap = rks.init_guess_by_vsap
    def nuc_grad_method(self): ...
    def to_hf(self): ...
    to_gpu = lib.to_gpu
