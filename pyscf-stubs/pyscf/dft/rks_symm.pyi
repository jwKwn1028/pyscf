from pyscf import lib as lib
from pyscf.dft import rks as rks, uks as uks
from pyscf.scf import hf_symm as hf_symm

class SymAdaptedRKS(rks.KohnShamDFT, hf_symm.SymAdaptedRHF):
    def __init__(self, mol, xc: str = 'LDA,VWN') -> None: ...
    def dump_flags(self, verbose=None): ...
    get_veff = rks.get_veff
    get_vsap = rks.get_vsap
    energy_elec = rks.energy_elec
    init_guess_by_vsap = rks.init_guess_by_vsap
    def nuc_grad_method(self): ...
    to_gpu = lib.to_gpu
RKS = SymAdaptedRKS

class SymAdaptedROKS(rks.KohnShamDFT, hf_symm.SymAdaptedROHF):
    def __init__(self, mol=None, xc: str = 'LDA,VWN') -> None: ...
    def dump_flags(self, verbose=None): ...
    get_veff = uks.get_veff
    get_vsap = rks.get_vsap
    energy_elec = uks.energy_elec
    init_guess_by_vsap = rks.init_guess_by_vsap
    def nuc_grad_method(self): ...
    to_gpu = lib.to_gpu
ROKS = SymAdaptedROKS
