from pyscf import lib as lib, symm as symm
from pyscf.lib import logger as logger
from _typeshed import Incomplete
from h5py._hl.dataset import Dataset
from numpy import float64, ndarray
from pyscf.cc.ccsd import CCSD
from pyscf.cc.qcisd import QCISD
from pyscf.lib.logger import Logger
from pyscf.lib.numpy_helper import NPArrayWithTag
from typing import Callable, Optional, Tuple, Union

def kernel(mycc: Union[Incomplete, Incomplete, CCSD, Incomplete], eris: Union[Incomplete, Incomplete, Incomplete], t1: Optional[ndarray]=None, t2: Optional[ndarray]=None, verbose: int=...) -> float64: ...
