from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.lib import logger as logger
from pyscf.pbc.scf import kghf as kghf, khf_ksymm as khf_ksymm
from numpy import ndarray
from pyscf.lib.numpy_helper import NPArrayWithTag
from pyscf.pbc.gto.cell import Cell
from pyscf.pbc.lib.kpts import KPoints
from typing import List, Optional, Tuple, Union

def get_jk(mf: "KsymAdaptedKGHF", cell: Optional[Cell]=None, dm_kpts: Optional[Union[ndarray, NPArrayWithTag]]=None, hermi: int = 0, kpts: None=None, kpts_band: None=None, with_j: bool = True, with_k: bool = True, **kwargs) -> Tuple[ndarray, ndarray]: ...
def get_occ(mf: "KsymAdaptedKGHF", mo_energy_kpts: Optional[ndarray]=None, mo_coeff_kpts: Optional[ndarray]=None) -> List[ndarray]: ...
def eig(kmf, h_kpts, s_kpts, overwrite: bool = False, x=None): ...

class KsymAdaptedKGHF(khf_ksymm.KsymAdaptedKSCF, kghf.KGHF):
    get_jk = get_jk
    get_occ = get_occ
    energy_elec: Incomplete
    get_init_guess: Incomplete
    init_guess_by_minao: Incomplete
    init_guess_by_atom: Incomplete
    init_guess_by_chkfile: Incomplete
    to_ks: Incomplete
    convert_from_: Incomplete
    def __init__(self, cell: Cell, kpts: KPoints=..., exxdiv: str=..., use_ao_symmetry: bool = True) -> None: ...
    def get_hcore(self, cell: Optional[Cell]=None, kpts: None=None) -> ndarray: ...
    def get_ovlp(self, cell: Optional[Cell]=None, kpts: None=None) -> ndarray: ...
    def eig(self, h_kpts: ndarray, s_kpts: ndarray, overwrite: bool = False, x: Optional[List[ndarray]]=None) -> Tuple[ndarray, ndarray]: ...
    def get_orbsym(self, mo_coeff=None, s=None): ...
    orbsym: Incomplete
KGHF = KsymAdaptedKGHF
