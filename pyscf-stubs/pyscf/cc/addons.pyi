from pyscf import lib as lib
from pyscf.cc.bccd import bccd_kernel_ as bccd_kernel_
from numpy import ndarray
from pyscf.cc.ccsd import CCSD
from pyscf.cc.gccsd import GCCSD
from pyscf.cc.rccsd import RCCSD
from pyscf.cc.uccsd import UCCSD
from pyscf.lib.numpy_helper import NPArrayWithTag
from typing import List, Optional, Tuple, Union

def spatial2spin(tx: Union[ndarray, Tuple[ndarray, ndarray], List[ndarray], Tuple[ndarray, ndarray, ndarray]], orbspin: Optional[ndarray]=None) -> NPArrayWithTag: ...
spatial2spinorb = spatial2spin

def spin2spatial(tx: Union[ndarray, NPArrayWithTag], orbspin: ndarray) -> Union[Tuple[ndarray, ndarray], Tuple[ndarray, ndarray, ndarray]]: ...
def convert_to_uccsd(mycc: Union[RCCSD, CCSD, UCCSD]) -> UCCSD: ...
def convert_to_gccsd(mycc: Union[RCCSD, CCSD, GCCSD, UCCSD]) -> GCCSD: ...
