from pyscf import gto as gto, lib as lib
from pyscf.gto.ft_ao import ft_aopair as ft_aopair
from pyscf.lib import logger as logger, zdotCN as zdotCN, zdotNC as zdotNC, zdotNN as zdotNN
from pyscf.pbc.df import ft_ao as ft_ao
from pyscf.pbc.df.incore import libpbc as libpbc
from pyscf.pbc.lib.kpts_helper import group_by_conj_pairs as group_by_conj_pairs, is_zero as is_zero, kk_adapted_iter as kk_adapted_iter
from pyscf.pbc.tools import k2gamma as k2gamma
from numpy import ndarray
from pyscf.lib.numpy_helper import NPArrayWithTag
from pyscf.pbc.df.aft import AFTDF
from pyscf.pbc.df.ft_ao import ExtendedMole
from pyscf.pbc.df.mdf import MDF
from pyscf.pbc.gto.cell import Cell
from typing import Callable, List, Optional, Tuple, Union

def get_j_kpts(mydf: Union[MDF, AFTDF], dm_kpts: Union[ndarray, List[NPArrayWithTag], NPArrayWithTag], hermi: int = 1, kpts: ndarray=..., kpts_band: Optional[ndarray]=None) -> ndarray: ...
def get_j_for_bands(mydf: Union[MDF, AFTDF], dm_kpts: Union[ndarray, NPArrayWithTag], hermi: int = 1, kpts: ndarray=..., kpts_band: Optional[ndarray]=None) -> ndarray: ...
def get_k_kpts(mydf: Union[MDF, AFTDF], dm_kpts: Union[ndarray, List[NPArrayWithTag], NPArrayWithTag], hermi: int = 1, kpts: ndarray=..., kpts_band: Optional[ndarray]=None, exxdiv: Optional[str]=None) -> ndarray: ...
def get_k_for_bands(mydf: Union[MDF, AFTDF], dm_kpts: Union[ndarray, NPArrayWithTag], hermi: int = 1, kpts: ndarray=..., kpts_band: Optional[ndarray]=None, exxdiv: Optional[str]=None) -> ndarray: ...
def get_jk(mydf: Union[MDF, AFTDF], dm: Union[ndarray, NPArrayWithTag], hermi: int = 1, kpt: ndarray=..., kpts_band: Optional[ndarray]=None, with_j: bool = True, with_k: bool = True, exxdiv: Optional[str]=None) -> Union[Tuple[None, ndarray], Tuple[ndarray, ndarray]]: ...
