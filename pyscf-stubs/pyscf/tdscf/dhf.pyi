from _typeshed import Incomplete
from functools import reduce as reduce
from pyscf import __config__ as __config__, ao2mo as ao2mo, lib as lib, scf as scf
from pyscf.lib import logger as logger
from pyscf.tdscf import rhf as rhf

OUTPUT_THRESHOLD: Incomplete
REAL_EIG_THRESHOLD: Incomplete

def gen_tda_operation(mf, fock_ao=None, with_nlc: bool = True) -> None: ...
gen_tda_hop = gen_tda_operation

def get_ab(mf, mo_energy=None, mo_coeff=None, mo_occ=None): ...
def get_nto(tdobj, state: int = 1, threshold=..., verbose=None) -> None: ...
def analyze(tdobj, verbose=None) -> None: ...

class TDBase(rhf.TDBase):
    def get_ab(self, mf=None): ...
    analyze = analyze
    get_nto = get_nto

class TDA(TDBase):
    singlet: Incomplete
    def gen_vind(self, mf=None): ...
    def get_init_guess(self, mf, nstates=None, wfnsym=None): ...
    nstates: Incomplete
    xy: Incomplete
    def kernel(self, x0=None, nstates=None): ...

def gen_tdhf_operation(mf, fock_ao=None, with_nlc: bool = True): ...

class TDHF(TDBase):
    singlet: Incomplete
    def gen_vind(self, mf=None): ...
    def get_init_guess(self, mf, nstates=None, wfnsym=None): ...
    get_precond: Incomplete
    nstates: Incomplete
    e: Incomplete
    xy: Incomplete
    def kernel(self, x0=None, nstates=None): ...
