from pyscf import __config__ as __config__, lib as lib
from pyscf.pbc.df import aft_ao2mo as aft_ao2mo, df_ao2mo as df_ao2mo
from pyscf.pbc.lib import kpts_helper as kpts_helper
from pyscf.pbc.lib.kpts_helper import gamma_point as gamma_point, unique as unique
from numpy import ndarray
from pyscf.pbc.df.mdf import MDF
from typing import Optional, Tuple, Union

def get_eri(mydf: MDF, kpts: Optional[Union[ndarray, Tuple[ndarray, ndarray, ndarray, ndarray]]]=None, compact: bool=...) -> ndarray: ...
def general(mydf: MDF, mo_coeffs: Union[ndarray, Tuple[ndarray, ndarray, ndarray, ndarray]], kpts: Optional[ndarray]=None, compact: bool=...) -> ndarray: ...
def ao2mo_7d(mydf: MDF, mo_coeff_kpts: ndarray, kpts: Optional[ndarray]=None, factor: int = 1, out: None=None) -> ndarray: ...
