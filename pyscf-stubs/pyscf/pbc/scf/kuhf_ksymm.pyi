from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.lib import logger as logger
from pyscf.pbc.lib.kpts import KPoints, KPoints as KPoints
from pyscf.pbc.scf import khf as khf, khf_ksymm as khf_ksymm, kuhf as kuhf
from numpy import float64, ndarray
from pyscf.lib.numpy_helper import NPArrayWithTag
from pyscf.pbc.dft.kuks_ksymm import KsymAdaptedKUKS
from pyscf.pbc.dft.kukspu_ksymm import KsymAdaptedKUKSpU
from pyscf.pbc.gto.cell import Cell
from typing import List, Optional, Tuple, Union

def get_occ(mf: Union[KsymAdaptedKUKSpU, KsymAdaptedKUHF, KsymAdaptedKUKS], mo_energy_kpts: Optional[ndarray]=None, mo_coeff_kpts: Optional[Tuple[ndarray, ndarray]]=None) -> ndarray: ...
def energy_elec(mf: "KsymAdaptedKUHF", dm_kpts: Optional[Union[ndarray, NPArrayWithTag]]=None, h1e_kpts: Optional[ndarray]=None, vhf_kpts: Optional[ndarray]=None) -> Tuple[float64, float64]: ...
get_rho = khf_ksymm.get_rho

class KsymAdaptedKUHF(khf_ksymm.KsymAdaptedKSCF, kuhf.KUHF):
    get_occ = get_occ
    energy_elec = energy_elec
    get_rho = get_rho
    to_ks: Incomplete
    convert_from_: Incomplete
    def __init__(self, cell: Cell, kpts: KPoints=..., exxdiv: str=..., use_ao_symmetry: bool = True) -> None: ...
    @property
    def nelec(self): ...
    @nelec.setter
    def nelec(self, x) -> None: ...
    def dump_flags(self, verbose: None=None) -> Union[KsymAdaptedKUKSpU, KsymAdaptedKUHF, KsymAdaptedKUKS]: ...
    def get_init_guess(self, cell: Optional[Cell]=None, key: str = 'minao', s1e: Optional[ndarray]=None) -> ndarray: ...
    def eig(self, h_kpts: ndarray, s_kpts: ndarray, overwrite: bool = False, x: Optional[List[ndarray]]=None) -> Tuple[ndarray, Tuple[ndarray, ndarray]]: ...
    def get_orbsym(self, mo_coeff=None, s=None): ...
    orbsym: Incomplete
KUHF = KsymAdaptedKUHF
