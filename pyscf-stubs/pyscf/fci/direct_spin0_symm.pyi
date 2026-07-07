from _typeshed import Incomplete
from pyscf import __config__ as __config__, ao2mo as ao2mo, lib as lib, symm as symm
from pyscf.fci import addons as addons, cistring as cistring, direct_spin0 as direct_spin0, direct_spin1 as direct_spin1, direct_spin1_symm as direct_spin1_symm
from pyscf.lib import logger as logger
from pyscf.scf.hf_symm import map_degeneracy as map_degeneracy

libfci: Incomplete

def contract_2e(eri, fcivec, norb, nelec, link_index=None, orbsym=None, wfnsym: int = 0): ...
energy = direct_spin1_symm.energy
kernel = direct_spin1_symm.kernel
make_rdm1 = direct_spin0.make_rdm1
make_rdm1s = direct_spin0.make_rdm1s
make_rdm12 = direct_spin0.make_rdm12
trans_rdm1s = direct_spin0.trans_rdm1s
trans_rdm1 = direct_spin0.trans_rdm1
trans_rdm12 = direct_spin0.trans_rdm12

def get_init_guess(norb, nelec, nroots, hdiag, orbsym, wfnsym: int = 0): ...
def get_init_guess_cyl_sym(norb, nelec, nroots, hdiag, orbsym, wfnsym: int = 0): ...

class FCISolver(direct_spin0.FCISolver):
    davidson_only: Incomplete
    pspace_size: Incomplete
    wfnsym: Incomplete
    sym_allowed_idx: Incomplete
    def __init__(self, mol=None, **kwargs) -> None: ...
    absorb_h1e: Incomplete
    dump_flags: Incomplete
    make_hdiag: Incomplete
    pspace: Incomplete
    contract_1e: Incomplete
    contract_ss: Incomplete
    guess_wfnsym = direct_spin1_symm.guess_wfnsym
    kernel: Incomplete
    def contract_2e(self, eri, fcivec, norb, nelec, link_index=None, orbsym=None, wfnsym=None, **kwargs): ...
    def get_init_guess(self, norb, nelec, nroots, hdiag, orbsym=None, wfnsym=None): ...
FCI = FCISolver
