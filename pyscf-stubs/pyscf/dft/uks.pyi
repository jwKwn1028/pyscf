from pyscf import lib as lib
from pyscf.dft import rks as rks
from pyscf.lib import logger as logger
from pyscf.scf import hf as hf, uhf as uhf
from _typeshed import Incomplete
from numpy import float64, ndarray
from pyscf.dft.rks_symm import SymAdaptedROKS
from pyscf.dft.roks import ROKS
from pyscf.dft.uks_symm import SymAdaptedUKS
from pyscf.dft.ukspu import UKSpU
from pyscf.gto.mole import Mole
from pyscf.lib.numpy_helper import NPArrayWithTag
from pyscf.scf.uhf import UHF
from typing import Optional, Tuple, Union

def get_veff(ks: Union[SymAdaptedUKS, ROKS, SymAdaptedROKS, Incomplete, UKSpU], mol: Optional[Mole]=None, dm: Optional[Union[ndarray, NPArrayWithTag, Tuple[ndarray, ndarray]]]=None, dm_last: Union[ndarray, NPArrayWithTag, int, Tuple[ndarray, ndarray]] = 0, vhf_last: Union[NPArrayWithTag, int] = 0, hermi: int = 1) -> NPArrayWithTag: ...
def get_vsap(ks: SymAdaptedUKS, mol: None=None) -> ndarray: ...
def energy_elec(ks: Union[SymAdaptedUKS, Incomplete, ROKS, SymAdaptedROKS, Incomplete], dm: Optional[Union[ndarray, NPArrayWithTag]]=None, h1e: Optional[ndarray]=None, vhf: Optional[NPArrayWithTag]=None) -> Tuple[float64, float64]: ...

class UKS(rks.KohnShamDFT, uhf.UHF):
    def __init__(self, mol: Mole, xc: str = 'LDA,VWN') -> None: ...
    def dump_flags(self, verbose: None=None) -> Union[Incomplete, UKSpU]: ...
    def initialize_grids(self, mol: Optional[Mole]=None, dm: Optional[ndarray]=None) -> Union[Incomplete, UKSpU]: ...
    get_veff = get_veff
    get_vsap = get_vsap
    energy_elec = energy_elec
    init_guess_by_vsap = rks.init_guess_by_vsap
    def nuc_grad_method(self): ...
    def to_hf(self) -> UHF: ...
    to_gpu = lib.to_gpu
