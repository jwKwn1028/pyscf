from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.lib import logger as logger, zdotCN as zdotCN, zdotNC as zdotNC, zdotNN as zdotNN
from pyscf.pbc import tools as tools
from pyscf.pbc.lib.kpts_helper import gamma_point as gamma_point, get_kconserv_ria as get_kconserv_ria, is_zero as is_zero, member as member
from numpy import float64, int64, ndarray
from pyscf.lib.numpy_helper import NPArrayWithTag
from pyscf.pbc.df.df import GDF
from pyscf.pbc.df.mdf import MDF
from pyscf.pbc.df.rsdf import RSGDF
from pyscf.pbc.gto.cell import Cell
from pyscf.pbc.scf.hf import SCF
from typing import Dict, List, Optional, Tuple, Union

DM2MO_PREC: Incomplete

def density_fit(mf: SCF, auxbasis: Optional[Union[List[List[Union[int, Tuple[float, float]]]], Dict[str, List[List[Union[int, List[Union[float64, int]]]]]], str]]=None, mesh: Optional[Tuple[int, int, int]]=None, with_df: Optional[GDF]=None) -> SCF: ...
def get_j_kpts(mydf: Union[GDF, MDF, RSGDF], dm_kpts: Union[ndarray, NPArrayWithTag], hermi: int = 1, kpts: ndarray=..., kpts_band: Optional[ndarray]=None) -> ndarray: ...
def get_j_kpts_kshift(mydf: RSGDF, dm_kpts: ndarray, kshift: Union[int64, int], hermi: int = 0, kpts: ndarray=..., kpts_band: None=None) -> ndarray: ...
def get_k_kpts(mydf: Union[GDF, MDF, RSGDF], dm_kpts: Union[NPArrayWithTag, ndarray], hermi: int = 1, kpts: ndarray=..., kpts_band: Optional[ndarray]=None, exxdiv: Optional[str]=None) -> ndarray: ...
def get_k_kpts_kshift(mydf: RSGDF, dm_kpts: ndarray, kshift: Union[int64, int], hermi: int = 0, kpts: ndarray=..., kpts_band: None=None, exxdiv: None=None) -> ndarray: ...
def get_jk(mydf: Union[GDF, MDF, RSGDF], dm: Union[ndarray, NPArrayWithTag], hermi: int = 1, kpt: ndarray=..., kpts_band: Optional[ndarray]=None, with_j: bool = True, with_k: bool = True, exxdiv: Optional[str]=None) -> Union[Tuple[None, ndarray], Tuple[ndarray, ndarray]]: ...
