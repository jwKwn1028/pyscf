from _typeshed import Incomplete
from pyscf import __config__ as __config__, ao2mo as ao2mo, lib as lib, scf as scf, symm as symm
from pyscf.data import nist as nist
from pyscf.lib import logger as logger
from pyscf.scf import uhf_symm as uhf_symm
from pyscf.tdscf import rhf as rhf
from pyscf.tdscf._lr_eig import real_eig as real_eig
from numpy import ndarray
from pyscf.dft.uks import UKS
from pyscf.dft.uks_symm import SymAdaptedUKS
from pyscf.lib.numpy_helper import NPArrayWithTag
from pyscf.scf.uhf import UHF
from pyscf.scf.uhf_symm import SymAdaptedUHF
from pyscf.tdscf.uks import CasidaTDDFT, TDA, TDDFT
from typing import Callable, List, Optional, Tuple, Union

OUTPUT_THRESHOLD: Incomplete
REAL_EIG_THRESHOLD: Incomplete
MO_BASE: Incomplete

def gen_tda_operation(mf: Union[UHF, UKS], fock_ao: None=None, wfnsym: None=None, with_nlc: bool = True) -> Tuple[Callable, ndarray]: ...
gen_tda_hop = gen_tda_operation

def get_frozen_mask(td: Union[CasidaTDDFT, TDDFT, TDA, TDHF, TDA]) -> Tuple[ndarray, ndarray]: ...
def get_ab(mf: Union[UKS, UHF], frozen: None=None, mo_energy: None=None, mo_coeff: None=None, mo_occ: None=None) -> Tuple[Tuple[ndarray, ndarray, ndarray], Tuple[ndarray, ndarray, ndarray]]: ...
def get_nto(tdobj: "TDA", state: int = 1, threshold: float=..., verbose: None=None) -> Union[Tuple[Tuple[ndarray, ndarray], Tuple[NPArrayWithTag, NPArrayWithTag]], Tuple[Tuple[ndarray, ndarray], Tuple[ndarray, ndarray]]]: ...
def analyze(tdobj: Union[TDA, CasidaTDDFT, TDHF], verbose: None=None) -> Union[TDA, CasidaTDDFT, TDHF]: ...

class TDBase(rhf.TDBase):
    def get_ab(self, mf: None=None, frozen: None=None) -> Tuple[Tuple[ndarray, ndarray, ndarray], Tuple[ndarray, ndarray, ndarray]]: ...
    get_frozen_mask = get_frozen_mask
    analyze = analyze
    get_nto = get_nto

class TDA(TDBase):
    singlet: Incomplete
    def gen_vind(self, mf: Optional[Union[UHF, SymAdaptedUHF, UKS, SymAdaptedUKS]]=None) -> Tuple[Callable, ndarray]: ...
    def get_init_guess(self, mf: Union[UHF, SymAdaptedUHF, UKS, SymAdaptedUKS], nstates: Optional[int]=None, wfnsym: None=None, return_symmetry: bool = False) -> Union[Tuple[ndarray, ndarray], Tuple[ndarray, None]]: ...
    nstates: Incomplete
    xy: Incomplete
    def kernel(self, x0: None=None, nstates: Optional[int]=None) -> Tuple[ndarray, List[Tuple[Tuple[ndarray, ndarray], Tuple[int, int]]]]: ...
    def Gradients(self): ...
    def to_gpu(self): ...
CIS = TDA

def gen_tdhf_operation(mf: Union[UHF, UKS], fock_ao: None=None, wfnsym: None=None, with_nlc: bool = True) -> Tuple[Callable, ndarray]: ...

class TDHF(TDBase):
    singlet: Incomplete
    def gen_vind(self, mf: Optional[Union[UHF, SymAdaptedUHF, UKS]]=None) -> Tuple[Callable, ndarray]: ...
    def get_init_guess(self, mf: Union[UKS, SymAdaptedUHF, UHF], nstates: Optional[int]=None, wfnsym: None=None, return_symmetry: bool = False) -> Union[Tuple[ndarray, ndarray], Tuple[ndarray, None]]: ...
    nstates: Incomplete
    xy: Incomplete
    def kernel(self, x0: None=None, nstates: Optional[int]=None) -> Tuple[ndarray, List[Tuple[Tuple[ndarray, ndarray], Tuple[ndarray, ndarray]]]]: ...
    Gradients: Incomplete
    def to_gpu(self): ...
RPA = TDHF
TDUHF = TDHF
