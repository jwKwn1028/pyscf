from _typeshed import Incomplete
from pyscf import ao2mo as ao2mo, lib as lib
from pyscf.fci import cistring as cistring, direct_spin1 as direct_spin1
from pyscf.fci.spin_op import spin_square as spin_square

libfci: Incomplete

def contract_1e(f1e, fcivec, norb, nelec, link_index=None): ...
def contract_2e(eri, fcivec, norb, nelec, link_index=None): ...
def contract_2e_hubbard(u, fcivec, norb, nelec, opt=None): ...
def make_hdiag(h1e, eri, norb, nelec, compress: bool = False): ...
def absorb_h1e(h1e, eri, norb, nelec, fac: int = 1): ...
def pspace(h1e, eri, norb, nelec, hdiag=None, np: int = 400): ...
def kernel(h1e, eri, norb, nelec, ci0=None, level_shift: float = 0.001, tol: float = 1e-10, lindep: float = 1e-14, max_cycle: int = 50, max_space: int = 12, nroots: int = 1, davidson_only: bool = False, pspace_size: int = 400, orbsym=None, wfnsym=None, ecore: int = 0, **kwargs): ...
def energy(h1e, eri, fcivec, norb, nelec, link_index=None): ...
make_rdm1s = direct_spin1.make_rdm1s

def make_rdm1(fcivec, norb, nelec, link_index=None) -> None: ...
make_rdm12s = direct_spin1.make_rdm12s
trans_rdm1s = direct_spin1.trans_rdm1s

def trans_rdm1(cibra, ciket, norb, nelec, link_index=None) -> None: ...
trans_rdm12s = direct_spin1.trans_rdm12s

class FCISolver(direct_spin1.FCISolver):
    absorb_h1e: Incomplete
    make_hdiag: Incomplete
    pspace: Incomplete
    contract_1e: Incomplete
    contract_2e: Incomplete
    make_rdm1: Incomplete
    trans_rdm1: Incomplete
    spin_square: Incomplete
FCI = FCISolver
