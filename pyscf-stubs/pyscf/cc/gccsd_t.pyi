from pyscf import lib as lib
from pyscf.cc import gccsd as gccsd
from pyscf.lib import logger as logger
from numpy import complex128, float64, ndarray
from pyscf.cc.gccsd import GCCSD, _PhysicistsERIs
from pyscf.lib.numpy_helper import NPArrayWithTag
from typing import Optional, Union

def kernel(cc: GCCSD, eris: _PhysicistsERIs, t1: Optional[Union[NPArrayWithTag, ndarray]]=None, t2: Optional[Union[NPArrayWithTag, ndarray]]=None, verbose: int=...) -> Union[complex128, float64]: ...
