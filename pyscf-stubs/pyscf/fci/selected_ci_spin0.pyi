from _typeshed import Incomplete
from pyscf import ao2mo as ao2mo, lib as lib
from pyscf.fci import direct_spin1 as direct_spin1, selected_ci as selected_ci

libfci: Incomplete

def contract_2e(eri, civec_strs, norb, nelec, link_index=None): ...
def enlarge_space(myci, civec_strs, eri, norb, nelec): ...
def make_hdiag(h1e, eri, ci_strs, norb, nelec, compress: bool = False): ...
def kernel(h1e, eri, norb, nelec, ci0=None, level_shift: float = 0.001, tol: float = 1e-10, lindep: float = 1e-14, max_cycle: int = 50, max_space: int = 12, nroots: int = 1, davidson_only: bool = False, pspace_size: int = 400, orbsym=None, wfnsym=None, select_cutoff: float = 0.001, ci_coeff_cutoff: float = 0.001, ecore: int = 0, **kwargs): ...
make_rdm1s = selected_ci.make_rdm1s
make_rdm2s = selected_ci.make_rdm2s
make_rdm1 = selected_ci.make_rdm1
make_rdm2 = selected_ci.make_rdm2
trans_rdm1s = selected_ci.trans_rdm1s
trans_rdm1 = selected_ci.trans_rdm1

class SelectedCI(selected_ci.SelectedCI):
    def contract_2e(self, eri, civec_strs, norb, nelec, link_index=None, **kwargs): ...
    make_hdiag: Incomplete
    enlarge_space = enlarge_space
SCI = SelectedCI
