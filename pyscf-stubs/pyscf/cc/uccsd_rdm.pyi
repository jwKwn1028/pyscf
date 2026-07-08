from pyscf import ao2mo as ao2mo, lib as lib
from numpy import ndarray
from pyscf.cc.uccsd import UCCSD
from pyscf.mp.ump2 import UMP2
from typing import List, Tuple, Union

einsum = lib.einsum

def make_rdm1(mycc: UCCSD, t1: Union[ndarray, List[ndarray], Tuple[ndarray, ndarray]], t2: Union[Tuple[ndarray, ndarray, ndarray], List[ndarray]], l1: Union[ndarray, List[ndarray], Tuple[ndarray, ndarray]], l2: Union[Tuple[ndarray, ndarray, ndarray], List[ndarray]], ao_repr: bool = False, with_frozen: bool = True, with_mf: bool = True) -> Tuple[ndarray, ndarray]: ...
def make_rdm2(mycc: UCCSD, t1: Union[ndarray, List[ndarray], Tuple[ndarray, ndarray]], t2: Union[Tuple[ndarray, ndarray, ndarray], List[ndarray]], l1: Union[ndarray, List[ndarray], Tuple[ndarray, ndarray]], l2: Union[Tuple[ndarray, ndarray, ndarray], List[ndarray]], ao_repr: bool = False, with_frozen: bool = True, with_dm1: bool = True) -> Tuple[ndarray, ndarray, ndarray]: ...
