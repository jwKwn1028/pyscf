from _typeshed import Incomplete
from functools import reduce as reduce
from pyscf import __config__ as __config__, ao2mo as ao2mo, lib as lib, scf as scf, symm as symm
from pyscf.lib import logger as logger
from pyscf.scf import ghf_symm as ghf_symm
from pyscf.tdscf import rhf as rhf
from numpy import ndarray
from pyscf.scf.ghf_symm import SymAdaptedGHF
from pyscf.tdscf.gks import CasidaTDDFT, TDA, TDDFT
from typing import Callable, List, Optional, Tuple, Union

OUTPUT_THRESHOLD: Incomplete
REAL_EIG_THRESHOLD: Incomplete

def gen_tda_operation(mf, fock_ao=None, wfnsym=None, with_nlc: bool = True): ...
gen_tda_hop = gen_tda_operation

def get_ab(mf: Incomplete, frozen: None=None, mo_energy: None=None, mo_coeff: None=None, mo_occ: None=None) -> Tuple[ndarray, ndarray]: ...
def get_nto(tdobj, state: int = 1, threshold=..., verbose=None) -> None: ...
def analyze(tdobj, verbose=None) -> None: ...

class TDBase(rhf.TDBase):
    def get_ab(self, mf: None=None) -> Tuple[ndarray, ndarray]: ...
    analyze = analyze
    get_nto = get_nto

class TDA(TDBase):
    singlet: Incomplete
    def gen_vind(self, mf: Optional[Incomplete]=None) -> Tuple[Callable, ndarray]: ...
    def get_init_guess(self, mf: Union[SymAdaptedGHF, Incomplete], nstates: Optional[int]=None, wfnsym: None=None, return_symmetry: bool = False) -> Tuple[ndarray, ndarray]: ...
    nstates: Incomplete
    xy: Incomplete
    def kernel(self, x0: None=None, nstates: Optional[int]=None) -> Tuple[ndarray, List[Tuple[ndarray, int]]]: ...
CIS = TDA

def gen_tdhf_operation(mf, fock_ao=None, wfnsym=None, with_nlc: bool = True): ...

class TDHF(TDBase):
    singlet: Incomplete
    def gen_vind(self, mf: Optional[SymAdaptedGHF]=None) -> Tuple[Callable, ndarray]: ...
    def get_init_guess(self, mf: SymAdaptedGHF, nstates: Optional[int]=None, wfnsym: None=None, return_symmetry: bool = False) -> Tuple[ndarray, ndarray]: ...
    nstates: Incomplete
    e: Incomplete
    xy: Incomplete
    def kernel(self, x0: None=None, nstates: None=None) -> Tuple[ndarray, List[Tuple[ndarray, ndarray]]]: ...
RPA = TDHF
TDGHF = TDHF
