from _typeshed import Incomplete
from pyscf import df as df, lib as lib, scf as scf
from pyscf.mp.dfmp2_native import DFRMP2 as DFRMP2, ints3c_cholesky as ints3c_cholesky, orbgrad_from_Gamma as orbgrad_from_Gamma
from pyscf.scf import ucphf as ucphf
from numpy import float64, ndarray
from pyscf.gto.mole import Mole
from pyscf.lib.logger import Logger
from pyscf.lib.misc import H5TmpFile
from pyscf.scf.uhf import UHF
from typing import List, Optional, Tuple, Union

class DFUMP2(DFRMP2):
    mo_coeff: Incomplete
    mo_energy: Incomplete
    nocc: Incomplete
    nmo: Incomplete
    e_scf: Incomplete
    frozen_mask: Incomplete
    occ_mask: Incomplete
    mol: Incomplete
    auxmol: Incomplete
    verbose: Incomplete
    stdout: Incomplete
    max_memory: Incomplete
    e_corr: Incomplete
    ps: float
    pt: float
    cphf_max_cycle: int
    cphf_tol: Incomplete
    def __init__(self, mf: UHF, frozen: Optional[Union[int, List[List[int]]]]=None, auxbasis: None=None) -> None: ...
    def dump_flags(self, logger: Optional[Logger]=None) -> None: ...
    def calculate_energy(self) -> float64: ...
    def make_rdm1(self, relaxed: bool = False, ao_repr: bool = False) -> ndarray: ...
    def make_natorbs(self, rdm1_mo: None=None, relaxed: bool = False) -> Tuple[ndarray, ndarray]: ...
    def calculate_integrals_(self) -> None: ...
    def delete(self) -> None: ...
    def nuc_grad_method(self) -> None: ...
    to_gpu = lib.to_gpu
MP2 = DFUMP2
UMP2 = DFUMP2
DFMP2 = DFUMP2

class SCSDFUMP2(DFUMP2):
    ps: Incomplete
    pt: Incomplete
    def __init__(self, mf: UHF, ps: float=..., pt: float=..., *args, **kwargs) -> None: ...
    def dump_flags(self, logger: None=None) -> None: ...
SCSMP2 = SCSDFUMP2
SCSUMP2 = SCSDFUMP2
SCSDFMP2 = SCSDFUMP2

def emp2_uhf(intsfiles: List[H5TmpFile], mo_energy: ndarray, frozen_mask: ndarray, logger: Logger, ps: float = 1.0, pt: float = 1.0) -> float64: ...
def make_rdm1(mp2: Union[DFUMP2, SCSDFUMP2], relaxed: bool, logger: Optional[Logger]=None) -> ndarray: ...
def ump2_densities_contribs(intsfiles: List[H5TmpFile], mo_energy: ndarray, frozen_mask: ndarray, max_memory: Union[float, int], logger: Logger, calcGamma: bool = False, auxmol: Optional[Mole]=None, ps: float = 1.0, pt: float = 1.0) -> Union[Tuple[ndarray, H5TmpFile], Tuple[ndarray, None]]: ...
def fock_response_uhf(mf: UHF, dm: Union[ndarray, List[ndarray]], full: bool = True) -> List[ndarray]: ...
def solve_cphf_uhf(mf: UHF, Lvo: List[ndarray], max_cycle: int, tol: float, logger: Logger) -> Tuple[ndarray, ndarray]: ...
