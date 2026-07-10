from pyscf import lib as lib, scf as scf
from pyscf.grad import uhf as uhf
from pyscf.hessian import rhf as rhf_hess
from pyscf.lib import logger as logger
from pyscf.scf import ucphf as ucphf
from numpy import ndarray
from pyscf.dft.uks import UKS
from pyscf.hessian.uks import Hessian
from pyscf.lib.logger import Logger
from pyscf.scf.uhf import UHF
from typing import Callable, List, Optional, Tuple, Union

def hess_elec(hessobj: Union[Hessian, Hessian], mo_energy: Optional[ndarray]=None, mo_coeff: Optional[ndarray]=None, mo_occ: Optional[ndarray]=None, mo1: None=None, mo_e1: None=None, h1ao: None=None, atmlst: Optional[Union[range, List[int]]]=None, max_memory: int = 4000, verbose: None=None) -> ndarray: ...
def partial_hess_elec(hessobj: "Hessian", mo_energy: Optional[ndarray]=None, mo_coeff: Optional[ndarray]=None, mo_occ: Optional[ndarray]=None, atmlst: Optional[Union[range, List[int]]]=None, max_memory: int = 4000, verbose: Optional[Logger]=None) -> ndarray: ...
def make_h1(hessobj: "Hessian", mo_coeff: ndarray, mo_occ: ndarray, chkfile: None=None, atmlst: Optional[Union[range, List[int]]]=None, verbose: Optional[Logger]=None) -> Union[Tuple[List[ndarray], List[ndarray]], Tuple[List[Optional[ndarray]], List[Optional[ndarray]]]]: ...
def solve_mo1(mf: Union[UHF, UKS], mo_energy: ndarray, mo_coeff: ndarray, mo_occ: ndarray, h1ao: Union[Tuple[ndarray, ndarray], Tuple[List[ndarray], List[ndarray]], Tuple[List[Optional[ndarray]], List[Optional[ndarray]]]], fx: None=None, atmlst: Optional[Union[range, List[int]]]=None, max_memory: int = 4000, verbose: Optional[Logger]=None, max_cycle: int = 50, level_shift: Union[float, int] = 0) -> Union[Tuple[Tuple[List[Optional[ndarray]], List[Optional[ndarray]]], Tuple[List[Optional[ndarray]], List[Optional[ndarray]]]], Tuple[Tuple[List[ndarray], List[ndarray]], Tuple[List[ndarray], List[ndarray]]]]: ...
def gen_vind(mf: Union[UHF, UKS], mo_coeff: ndarray, mo_occ: ndarray) -> Callable: ...
def gen_hop(hobj, mo_energy=None, mo_coeff=None, mo_occ=None, verbose=None): ...

class Hessian(rhf_hess.HessianBase):
    partial_hess_elec = partial_hess_elec
    hess_elec = hess_elec
    make_h1 = make_h1
    gen_hop = gen_hop
    def solve_mo1(self, mo_energy: ndarray, mo_coeff: ndarray, mo_occ: ndarray, h1ao: Union[Tuple[ndarray, ndarray], Tuple[List[ndarray], List[ndarray]], Tuple[List[Optional[ndarray]], List[Optional[ndarray]]]], fx: None=None, atmlst: Optional[Union[range, List[int]]]=None, max_memory: int = 4000, verbose: Optional[Logger]=None) -> Union[Tuple[Tuple[List[Optional[ndarray]], List[Optional[ndarray]]], Tuple[List[Optional[ndarray]], List[Optional[ndarray]]]], Tuple[Tuple[List[ndarray], List[ndarray]], Tuple[List[ndarray], List[ndarray]]]]: ...
