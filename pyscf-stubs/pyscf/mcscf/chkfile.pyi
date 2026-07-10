from pyscf.lib import H5FileWrap as H5FileWrap
from pyscf.lib.chkfile import dump as dump, load as load, load_mol as load_mol
from pyscf.mcscf.addons import StateAverageMixFCISolver as StateAverageMixFCISolver
from numpy import float64, int64, ndarray
from pyscf.lib.numpy_helper import NPArrayWithTag
from typing import Any, Optional, Tuple, Union

def load_mcscf(chkfile): ...
def dump_mcscf(mc: Any, chkfile: Optional[str]=None, key: str = 'mcscf', e_tot: Optional[float64]=None, mo_coeff: Optional[Union[ndarray, Tuple[ndarray, ndarray], NPArrayWithTag]]=None, ncore: Optional[int64]=None, ncas: Optional[int64]=None, nelecas: Optional[ndarray]=None, mo_occ: Optional[ndarray]=None, mo_energy: Optional[ndarray]=None, e_cas: Optional[float64]=None, ci_vector: None=None, casdm1: Optional[Union[ndarray, Tuple[ndarray, ndarray]]]=None, overwrite_mol: bool = True) -> None: ...
