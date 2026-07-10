from _typeshed import Incomplete
from functools import reduce as reduce
from pyscf import __config__ as __config__, ao2mo as ao2mo, lib as lib, scf as scf
from pyscf.lib import logger as logger
from pyscf.tdscf import rhf as rhf
from numpy import ndarray
from pyscf.dft.dks import DKS
from pyscf.scf.dhf import DHF
from pyscf.tdscf.dks import TDA, TDDFT
from typing import Callable, List, Optional, Tuple, Union

OUTPUT_THRESHOLD: Incomplete
REAL_EIG_THRESHOLD: Incomplete

def gen_tda_operation(mf, fock_ao=None, with_nlc: bool = True) -> None: ...
gen_tda_hop = gen_tda_operation

def get_ab(mf: Union[DKS, DHF], mo_energy: None=None, mo_coeff: None=None, mo_occ: None=None) -> Tuple[ndarray, ndarray]: ...
def get_nto(tdobj, state: int = 1, threshold=..., verbose=None) -> None: ...
def analyze(tdobj, verbose=None) -> None: ...

class TDBase(rhf.TDBase):
    def get_ab(self, mf: None=None) -> Tuple[ndarray, ndarray]: ...
    analyze = analyze
    get_nto = get_nto

class TDA(TDBase):
    singlet: Incomplete
    def gen_vind(self, mf: Optional[DKS]=None) -> Tuple[Callable, ndarray]: ...
    def get_init_guess(self, mf: DKS, nstates: Optional[int]=None, wfnsym: None=None) -> ndarray: ...
    nstates: Incomplete
    xy: Incomplete
    def kernel(self, x0: None=None, nstates: Optional[int]=None) -> Tuple[ndarray, List[Tuple[ndarray, int]]]: ...

def gen_tdhf_operation(mf, fock_ao=None, with_nlc: bool = True): ...

class TDHF(TDBase):
    singlet: Incomplete
    def gen_vind(self, mf: Optional[DKS]=None) -> Tuple[Callable, ndarray]: ...
    def get_init_guess(self, mf: DKS, nstates: Optional[int]=None, wfnsym: None=None) -> ndarray: ...
    get_precond: Incomplete
    nstates: Incomplete
    e: Incomplete
    xy: Incomplete
    def kernel(self, x0: None=None, nstates: Optional[int]=None) -> Tuple[ndarray, List[Tuple[ndarray, ndarray]]]: ...
