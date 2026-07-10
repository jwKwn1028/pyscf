from _typeshed import Incomplete
from functools import reduce as reduce
from pyscf import __config__ as __config__, ao2mo as ao2mo, dft as dft, lib as lib
from pyscf.lib import logger as logger
from pyscf.tdscf import ghf as ghf, gks as gks
from pyscf.x2c import x2c as x2c
from numpy import ndarray
from pyscf.x2c.dft import UKS
from typing import Tuple

OUTPUT_THRESHOLD: Incomplete
REAL_EIG_THRESHOLD: Incomplete

def gen_tda_operation(mf, fock_ao=None, with_nlc: bool = True): ...
gen_tda_hop = gen_tda_operation

def get_ab(mf: UKS, mo_energy: None=None, mo_coeff: None=None, mo_occ: None=None) -> Tuple[ndarray, ndarray]: ...
def get_nto(tdobj, state: int = 1, threshold=..., verbose=None) -> None: ...
def analyze(tdobj, verbose=None) -> None: ...

class TDBase(ghf.TDBase):
    def get_ab(self, mf: None=None) -> Tuple[ndarray, ndarray]: ...
    analyze = analyze
    get_nto = get_nto
    def nuc_grad_method(self) -> None: ...

class TDA(TDBase, ghf.TDA):
    gen_vind: Incomplete
    def get_init_guess(self, mf, nstates=None, wfnsym=None, return_symmetry: bool = False): ...
    kernel: Incomplete

def gen_tdhf_operation(mf, fock_ao=None, with_nlc: bool = True): ...

class TDHF(TDBase, ghf.TDHF):
    gen_vind: Incomplete
    def get_init_guess(self, mf, nstates=None, wfnsym=None, return_symmetry: bool = False): ...
    kernel: Incomplete
TDDFT = TDHF
