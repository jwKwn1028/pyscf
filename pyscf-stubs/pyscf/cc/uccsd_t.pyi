from pyscf import lib as lib
from pyscf.lib import logger as logger
from h5py._hl.dataset import Dataset
from numpy import float64, ndarray
from pyscf.cc.uccsd import UCCSD, _ChemistsERIs
from pyscf.lib.logger import Logger
from pyscf.lib.misc import H5TmpFile
from typing import Callable, List, Optional, Tuple, Union

def kernel(mycc: UCCSD, eris: _ChemistsERIs, t1: Optional[Union[List[ndarray], Tuple[ndarray, ndarray]]]=None, t2: Optional[Union[Tuple[ndarray, ndarray, ndarray], List[ndarray]]]=None, verbose: int=...) -> float64: ...
