from _typeshed import Incomplete
from pyscf import __config__ as __config__, ao2mo as ao2mo, lib as lib, scf as scf
from pyscf.lib import logger as logger
from pyscf.mp import mp2 as mp2
from numpy import float64, ndarray
from pyscf.lib.numpy_helper import NPArrayWithTag
from pyscf.mp.dfgmp2 import DFGMP2
from pyscf.scf.ghf import GHF
from typing import Callable, Optional, Tuple, Union

WITH_T2: Incomplete

def kernel(mp: "GMP2", mo_energy: Optional[ndarray]=None, mo_coeff: Optional[ndarray]=None, eris: Optional[Union[_PhysicistsERIs, Callable]]=None, with_t2: bool=..., verbose: None=None) -> Union[Tuple[float64, None], Tuple[float64, ndarray]]: ...
def energy(mp: "GMP2", t2: ndarray, eris: "_PhysicistsERIs") -> float64: ...
def update_amps(mp: "GMP2", t2: ndarray, eris: "_PhysicistsERIs") -> ndarray: ...
def make_rdm1(mp: "GMP2", t2: Optional[ndarray]=None, ao_repr: bool = False, with_frozen: bool = True) -> ndarray: ...
def make_rdm2(mp: "GMP2", t2: None=None, ao_repr: bool = False) -> ndarray: ...

class GMP2(mp2.MP2Base):
    def __init__(self, mf: GHF, frozen: None=None, mo_coeff: Optional[NPArrayWithTag]=None, mo_occ: Optional[ndarray]=None) -> None: ...
    def ao2mo(self, mo_coeff: Optional[ndarray]=None) -> "_PhysicistsERIs": ...
    make_rdm1 = make_rdm1
    make_rdm2 = make_rdm2
    def density_fit(self, auxbasis: None=None, with_df: None=None) -> DFGMP2: ...
    def nuc_grad_method(self) -> None: ...
    energy = energy
    update_amps = update_amps
    def init_amps(self, mo_energy: Optional[ndarray]=None, mo_coeff: Optional[ndarray]=None, eris: Optional[Union[_PhysicistsERIs, Callable]]=None, with_t2: bool=...) -> Union[Tuple[float64, None], Tuple[float64, ndarray]]: ...
MP2 = GMP2

class _PhysicistsERIs:
    mol: Incomplete
    mo_coeff: Incomplete
    nocc: Incomplete
    fock: Incomplete
    orbspin: Incomplete
    oovv: Incomplete
    def __init__(self, mol: None=None) -> None: ...
