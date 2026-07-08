from _typeshed import Incomplete
from pyscf import gto as mol_gto, lib as lib
from pyscf.lib import logger as logger
from pyscf.lib.parameters import BOHR as BOHR
from pyscf.pbc.df.incore import libpbc as libpbc, make_auxcell as make_auxcell
from pyscf.pbc.lib.kpts_helper import KPT_DIFF_TOL as KPT_DIFF_TOL, gamma_point as gamma_point, is_zero as is_zero, unique as unique
from pyscf.pbc.tools import k2gamma as k2gamma
from numpy import float64, int64, ndarray
from pyscf.lib.misc import H5TmpFile
from pyscf.pbc.gto.cell import Cell
from typing import Callable, Dict, List, Optional, Tuple, Union

class MoleNoBasSort(mol_gto.mole.Mole):
    atom: Incomplete
    basis: Incomplete
    def build(self, **kwargs) -> "MoleNoBasSort": ...

def remove_exp_basis(basis: Dict[str, Union[List[List[Union[int, List[Union[float, int]]]]], List[List[Union[int, List[float]]]]]], amin: Optional[float]=None, amax: None=None) -> Dict[str, Union[List[List[Union[int, List[Union[float, int]]]]], List[List[Union[int, List[float]]]]]]: ...
def estimate_omega_for_npw(cell: Cell, npw_max: int, precision: Optional[float]=None, kmax: float64 = 0, round2odd: bool = True) -> Tuple[float64, float64, ndarray]: ...
def estimate_mesh_for_omega(cell: Cell, omega: float, precision: Optional[float]=None, kmax: Union[int, float64] = 0, round2odd: bool = True) -> Tuple[float64, ndarray]: ...
def intor_j2c(cell: Cell, omega: float, precision: None=None, kpts: Optional[ndarray]=None, hermi: int = 1, shls_slice: None=None, no_screening: bool = False) -> List[ndarray]: ...
def wrap_int3c_nospltbas(cell: Cell, auxcell: Cell, omega: Union[float, float64], shlpr_mask: ndarray, prescreening_data: Tuple[ndarray, ndarray, int, ndarray, ndarray, float, ndarray, ndarray, ndarray], intor: str = 'int3c2e', aosym: str = 's1', comp: int = 1, kptij_lst: ndarray=..., cintopt: None=None, bvk_kmesh: Optional[ndarray]=None) -> Callable: ...
