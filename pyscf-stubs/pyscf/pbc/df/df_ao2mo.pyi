from pyscf import __config__ as __config__, ao2mo as ao2mo, lib as lib
from pyscf.ao2mo.incore import iden_coeffs as iden_coeffs
from pyscf.pbc.df.df_jk import zdotNC as zdotNC, zdotNN as zdotNN
from pyscf.pbc.lib import kpts_helper as kpts_helper
from pyscf.pbc.lib.kpts_helper import gamma_point as gamma_point, is_zero as is_zero, unique as unique
from h5py._hl.dataset import Dataset
from numpy import bool, ndarray
from pyscf.lib.misc import StreamObject
from pyscf.pbc.df.df import GDF
from pyscf.pbc.df.mdf import MDF
from pyscf.pbc.df.rsdf import RSGDF
from typing import List, Optional, Tuple, Union

def get_eri(mydf: Union[MDF, RSGDF, GDF], kpts: Optional[Union[Tuple[ndarray, ndarray, ndarray, ndarray], ndarray]]=None, compact: bool=...) -> ndarray: ...
def general(mydf: Union[MDF, RSGDF, GDF], mo_coeffs: Union[ndarray, Tuple[ndarray, ndarray, ndarray, ndarray], List[ndarray]], kpts: Optional[Union[ndarray, Tuple[ndarray, ndarray, ndarray, ndarray]]]=None, compact: bool=...) -> ndarray: ...
def ao2mo_7d(mydf: Union[RSGDF, GDF], mo_coeff_kpts: Union[ndarray, List[ndarray]], kpts: Optional[ndarray]=None, factor: Union[float, int] = 1, out: Optional[Dataset]=None) -> Union[ndarray, Dataset]: ...

class PBC2DIntegralsWarning(RuntimeWarning): ...

def warn_pbc2d_eri(mydf: StreamObject) -> None: ...
