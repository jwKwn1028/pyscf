from pyscf import lib as lib
from pyscf.dft import rks as rks
from pyscf.dft.numint2c import NumInt2C as NumInt2C
from pyscf.lib import logger as logger
from pyscf.scf import ghf as ghf
from _typeshed import Incomplete
from numpy import ndarray
from pyscf.dft.dks import DKS
from pyscf.gto.mole import Mole
from pyscf.lib.numpy_helper import NPArrayWithTag
from pyscf.scf.ghf import GHF
from pyscf.x2c.dft import UKS
from typing import Optional, Union

def get_veff(ks: Union[DKS, Incomplete, Incomplete, UKS], mol: Optional[Mole]=None, dm: Optional[Union[NPArrayWithTag, ndarray]]=None, dm_last: Union[ndarray, int, NPArrayWithTag] = 0, vhf_last: Union[NPArrayWithTag, int] = 0, hermi: int = 1) -> NPArrayWithTag: ...
energy_elec = rks.energy_elec

class GKS(rks.KohnShamDFT, ghf.GHF):
    get_veff = get_veff
    energy_elec = energy_elec
    def __init__(self, mol: Mole, xc: str = 'LDA,VWN') -> None: ...
    def dump_flags(self, verbose: None=None) -> Incomplete: ...
    @property
    def collinear(self): ...
    @collinear.setter
    def collinear(self, val) -> None: ...
    @property
    def spin_samples(self): ...
    @spin_samples.setter
    def spin_samples(self, val) -> None: ...
    def nuc_grad_method(self) -> None: ...
    def to_hf(self) -> GHF: ...
    to_gpu = lib.to_gpu
