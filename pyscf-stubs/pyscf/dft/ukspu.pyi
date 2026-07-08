from _typeshed import Incomplete
from pyscf import lib as lib
from pyscf.data.nist import HARTREE2EV as HARTREE2EV
from pyscf.dft import uks as uks
from pyscf.lib import logger as logger
from pyscf.lo.iao import reference_mol as reference_mol
from numpy import float64, ndarray
from pyscf.gto.mole import Mole
from pyscf.lib.numpy_helper import NPArrayWithTag
from typing import List, Optional, Tuple, Union

def get_veff(ks: "UKSpU", mol: Optional[Mole]=None, dm: Optional[Union[ndarray, NPArrayWithTag]]=None, dm_last: Union[ndarray, int, NPArrayWithTag] = 0, vhf_last: Union[int, NPArrayWithTag] = 0, hermi: int = 1) -> NPArrayWithTag: ...
def energy_elec(mf: "UKSpU", dm: Optional[Union[ndarray, NPArrayWithTag]]=None, h1e: Optional[ndarray]=None, vhf: Optional[NPArrayWithTag]=None) -> Tuple[float64, float64]: ...

class UKSpU(uks.UKS):
    get_veff = get_veff
    energy_elec = energy_elec
    to_hf: Incomplete
    U_idx: Incomplete
    U_val: Incomplete
    C_ao_lo: Incomplete
    minao_ref: Incomplete
    alpha: Incomplete
    def __init__(self, mol: Mole, xc: str = 'LDA,VWN', U_idx: List[str]=[], U_val: List[float]=[], C_ao_lo: None=None, minao_ref: str = 'MINAO') -> None: ...
    def dump_flags(self, verbose: None=None) -> "UKSpU": ...
    def Gradients(self): ...
    def nuc_grad_method(self): ...

def linear_response_u(mf_plus_u: UKSpU, alphalist: Tuple[float, float, float]=(0.02, 0.05, 0.08)) -> float64: ...
