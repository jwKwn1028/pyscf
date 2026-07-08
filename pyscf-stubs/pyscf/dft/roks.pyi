from pyscf import lib as lib
from pyscf.dft import rks as rks, uks as uks
from pyscf.dft.uks import energy_elec as energy_elec
from pyscf.scf import rohf as rohf
from numpy import ndarray
from pyscf.grad.roks import Gradients
from pyscf.gto.mole import Mole
from pyscf.lib.numpy_helper import NPArrayWithTag
from typing import Optional, Union

def get_veff(ks: "ROKS", mol: Optional[Mole]=None, dm: Optional[Union[ndarray, NPArrayWithTag]]=None, dm_last: Union[ndarray, int, NPArrayWithTag] = 0, vhf_last: Union[NPArrayWithTag, int] = 0, hermi: int = 1) -> NPArrayWithTag: ...

class ROKS(rks.KohnShamDFT, rohf.ROHF):
    def __init__(self, mol: Mole, xc: str = 'LDA,VWN') -> None: ...
    def dump_flags(self, verbose: None=None) -> "ROKS": ...
    get_veff = get_veff
    get_vsap = rks.get_vsap
    energy_elec = energy_elec
    init_guess_by_vsap = rks.init_guess_by_vsap
    def nuc_grad_method(self) -> Gradients: ...
    def to_hf(self): ...
    to_gpu = lib.to_gpu
