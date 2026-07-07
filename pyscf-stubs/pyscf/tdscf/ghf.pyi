from _typeshed import Incomplete
from functools import reduce as reduce
from pyscf import __config__ as __config__, ao2mo as ao2mo, lib as lib, scf as scf, symm as symm
from pyscf.lib import logger as logger
from pyscf.scf import ghf_symm as ghf_symm
from pyscf.tdscf import rhf as rhf

OUTPUT_THRESHOLD: Incomplete
REAL_EIG_THRESHOLD: Incomplete

def gen_tda_operation(mf, fock_ao=None, wfnsym=None, with_nlc: bool = True): ...
gen_tda_hop = gen_tda_operation

def get_ab(mf, frozen=None, mo_energy=None, mo_coeff=None, mo_occ=None): ...
def get_nto(tdobj, state: int = 1, threshold=..., verbose=None) -> None: ...
def analyze(tdobj, verbose=None) -> None: ...

class TDBase(rhf.TDBase):
    def get_ab(self, mf=None): ...
    analyze = analyze
    get_nto = get_nto

class TDA(TDBase):
    singlet: Incomplete
    def gen_vind(self, mf=None): ...
    def get_init_guess(self, mf, nstates=None, wfnsym=None, return_symmetry: bool = False): ...
    nstates: Incomplete
    xy: Incomplete
    def kernel(self, x0=None, nstates=None): ...
CIS = TDA

def gen_tdhf_operation(mf, fock_ao=None, wfnsym=None, with_nlc: bool = True): ...

class TDHF(TDBase):
    singlet: Incomplete
    def gen_vind(self, mf=None): ...
    def get_init_guess(self, mf, nstates=None, wfnsym=None, return_symmetry: bool = False): ...
    nstates: Incomplete
    e: Incomplete
    xy: Incomplete
    def kernel(self, x0=None, nstates=None): ...
RPA = TDHF
TDGHF = TDHF
