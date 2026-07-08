from pyscf import lib as lib
from numpy import ndarray
from pyscf.cc.gccsd import GCCSD
from pyscf.lib.numpy_helper import NPArrayWithTag
from typing import Tuple, Union

einsum = lib.einsum

def make_rdm1(mycc: GCCSD, t1: Union[ndarray, NPArrayWithTag], t2: Union[ndarray, NPArrayWithTag], l1: Union[ndarray, NPArrayWithTag], l2: Union[ndarray, NPArrayWithTag], ao_repr: bool = False, with_frozen: bool = True, with_mf: bool = True) -> ndarray: ...
def make_rdm2(mycc: GCCSD, t1: Union[ndarray, NPArrayWithTag], t2: Union[ndarray, NPArrayWithTag], l1: Union[ndarray, NPArrayWithTag], l2: Union[ndarray, NPArrayWithTag], ao_repr: bool = False, with_frozen: bool = True, with_dm1: bool = True) -> ndarray: ...
