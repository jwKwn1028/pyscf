from pyscf import lib as lib
from pyscf.cc import ccsd_lambda as ccsd_lambda
from pyscf.lib import logger as logger
from numpy import ndarray
from pyscf.cc.gccsd import GCCSD, _PhysicistsERIs
from pyscf.lib.numpy_helper import NPArrayWithTag
from typing import Optional, Tuple, Union

einsum = lib.einsum

def kernel(mycc: GCCSD, eris: Optional[_PhysicistsERIs]=None, t1: Optional[Union[ndarray, NPArrayWithTag]]=None, t2: Optional[Union[ndarray, NPArrayWithTag]]=None, l1: None=None, l2: None=None, max_cycle: int = 50, tol: float = 1e-08, verbose: int=...) -> Tuple[bool, ndarray, ndarray]: ...
def make_intermediates(mycc, t1, t2, eris): ...
def update_lambda(mycc, t1, t2, l1, l2, eris, imds): ...
