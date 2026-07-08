from pyscf import lib as lib
from pyscf.cc import ccsd as ccsd
from pyscf.lib import logger as logger
from _typeshed import Incomplete
from h5py._hl.dataset import Dataset
from numpy import ndarray
from pyscf.cc.ccsd import CCSDBase
from pyscf.cc.gccsd import _PhysicistsERIs
from pyscf.lib.numpy_helper import NPArrayWithTag
from typing import Callable, Optional, Tuple, Union

def kernel(mycc: CCSDBase, eris: Optional[Union[Incomplete, _PhysicistsERIs, Incomplete, Incomplete, Incomplete]]=None, t1: Optional[Union[ndarray, Tuple[ndarray, ndarray], NPArrayWithTag]]=None, t2: Optional[Union[ndarray, Tuple[ndarray, ndarray, ndarray], NPArrayWithTag]]=None, l1: Optional[ndarray]=None, l2: Optional[ndarray]=None, max_cycle: int = 50, tol: float = 1e-08, verbose: int=..., fintermediates: Optional[Callable]=None, fupdate: Optional[Callable]=None) -> Union[Tuple[bool, ndarray, ndarray], Tuple[bool, Tuple[ndarray, ndarray], Tuple[ndarray, ndarray, ndarray]]]: ...
def make_intermediates(mycc, t1, t2, eris): ...
def update_lambda(mycc, t1, t2, l1, l2, eris=None, imds=None): ...
