from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib, lo as lo
from pyscf.data.nist import HARTREE2EV as HARTREE2EV
from pyscf.dft.rkspu import reference_mol as reference_mol
from pyscf.lib import logger as logger
from pyscf.pbc.dft import krks as krks
from KRKSpU import Gradients
from numpy import complex128, float64, ndarray
from pyscf.lib.numpy_helper import NPArrayWithTag
from pyscf.pbc.dft.krkspu_ksymm import KsymAdaptedKRKSpU
from pyscf.pbc.grad.krkspu import Gradients
from pyscf.pbc.gto.cell import Cell
from pyscf.pbc.lib.kpts import KPoints
from typing import List, Optional, Tuple, Union

def get_veff(ks: "KRKSpU", cell: Optional[Cell]=None, dm: Optional[Union[NPArrayWithTag, ndarray]]=None, dm_last: Union[ndarray, NPArrayWithTag, int] = 0, vhf_last: Union[NPArrayWithTag, int] = 0, hermi: int = 1, kpts: None=None, kpts_band: None=None) -> NPArrayWithTag: ...
def energy_elec(ks: Union[KsymAdaptedKRKSpU, KRKSpU], dm_kpts: Optional[Union[ndarray, NPArrayWithTag]]=None, h1e_kpts: Optional[ndarray]=None, vhf: Optional[NPArrayWithTag]=None) -> Tuple[float64, complex128]: ...

class KRKSpU(krks.KRKS):
    get_veff = get_veff
    energy_elec = energy_elec
    to_hf: Incomplete
    U_idx: Incomplete
    U_val: Incomplete
    C_ao_lo: Incomplete
    minao_ref: Incomplete
    alpha: Incomplete
    def __init__(self, cell: Cell, kpts: Union[ndarray, KPoints]=..., xc: str = 'LDA,VWN', exxdiv: str=..., U_idx: List[str]=[], U_val: List[Union[float, int]]=[], C_ao_lo: Optional[str]=None, minao_ref: str = 'MINAO', **kwargs) -> None: ...
    def dump_flags(self, verbose: None=None) -> "KRKSpU": ...
    def Gradients(self) -> Gradients: ...
    def nuc_grad_method(self) -> Gradients: ...

def linear_response_u(mf_plus_u: KRKSpU, alphalist: Tuple[float, float]=(0.02, 0.05, 0.08)) -> float64: ...
