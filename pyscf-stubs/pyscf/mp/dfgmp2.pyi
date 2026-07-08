from _typeshed import Incomplete
from collections.abc import Generator
from pyscf import __config__ as __config__, lib as lib, scf as scf
from pyscf.lib import logger as logger
from pyscf.mp import dfmp2 as dfmp2, gmp2 as gmp2
from pyscf.mp.gmp2 import _PhysicistsERIs, make_rdm1 as make_rdm1, make_rdm2 as make_rdm2
from numpy import float64, ndarray
from pyscf.lib.numpy_helper import NPArrayWithTag
from typing import Iterator, Optional, Tuple, Union

WITH_T2: Incomplete

def kernel(mp: "DFGMP2", mo_energy: Optional[ndarray]=None, mo_coeff: Optional[ndarray]=None, eris: Optional[_PhysicistsERIs]=None, with_t2: bool=..., verbose: int=...) -> Tuple[float64, ndarray]: ...

class DFGMP2(gmp2.GMP2):
    __init__: Incomplete
    kernel: Incomplete
    split_mo_energy: Incomplete
    split_mo_coeff: Incomplete
    split_mo_occ: Incomplete
    reset: Incomplete
    def loop_ao2mo(self, mo_coeff: Union[ndarray, NPArrayWithTag], nocc: int, orbspin: Optional[ndarray]) -> Iterator[Union[Tuple[ndarray, ndarray], Tuple[ndarray, None]]]: ...
    def ao2mo(self, mo_coeff: Optional[ndarray]=None) -> _PhysicistsERIs: ...
    def make_rdm1(self, t2=None, ao_repr: bool = False, with_frozen: bool = True): ...
    def make_rdm2(self, t2=None, ao_repr: bool = False): ...
    def nuc_grad_method(self) -> None: ...
    def update_amps(self, t2, eris) -> None: ...
    def init_amps(self, mo_energy: Optional[ndarray]=None, mo_coeff: Optional[ndarray]=None, eris: Optional[_PhysicistsERIs]=None, with_t2: bool=...) -> Tuple[float64, ndarray]: ...
    Gradients = NotImplemented
MP2 = DFGMP2
DFMP2 = DFGMP2
