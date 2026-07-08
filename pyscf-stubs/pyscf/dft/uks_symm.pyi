from pyscf import lib as lib
from pyscf.dft import rks as rks, uks as uks
from pyscf.lib import logger as logger
from pyscf.scf import uhf_symm as uhf_symm
from pyscf.gto.mole import Mole

class SymAdaptedUKS(rks.KohnShamDFT, uhf_symm.UHF):
    def __init__(self, mol: Mole, xc: str = 'LDA,VWN') -> None: ...
    def dump_flags(self, verbose: None=None) -> "SymAdaptedUKS": ...
    get_veff = uks.get_veff
    get_vsap = uks.get_vsap
    energy_elec = uks.energy_elec
    init_guess_by_vsap = rks.init_guess_by_vsap
    def nuc_grad_method(self): ...
    to_gpu = lib.to_gpu
UKS = SymAdaptedUKS
