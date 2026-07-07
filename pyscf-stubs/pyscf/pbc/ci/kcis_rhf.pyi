from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.lib import logger as logger
from pyscf.pbc import scf as scf, tools as tools
from pyscf.pbc.df import df as df
from pyscf.pbc.lib import kpts_helper as kpts_helper
from pyscf.pbc.mp.kmp2 import get_frozen_mask as get_frozen_mask, get_nmo as get_nmo, get_nocc as get_nocc, padded_mo_coeff as padded_mo_coeff, padding_k_idx as padding_k_idx

einsum = lib.einsum
direct_sum = lib.direct_sum

def kernel(cis, nroots: int = 1, eris=None, kptlist=None, **kargs): ...
def cis_matvec_singlet(cis, vector, kshift, eris=None): ...
def cis_H(cis, kshift, eris=None): ...
def cis_diag(cis, kshift, eris=None): ...

class KCIS(lib.StreamObject):
    kpts: Incomplete
    verbose: Incomplete
    max_memory: Incomplete
    max_space: Incomplete
    max_cycle: Incomplete
    conv_tol: Incomplete
    keep_exxdiv: bool
    direct: bool
    build_full_H: bool
    davidson: bool
    khelper: Incomplete
    mo_coeff: Incomplete
    mo_occ: Incomplete
    frozen: Incomplete
    voov: Incomplete
    ovov: Incomplete
    def __init__(self, mf, frozen=None, mo_coeff=None, mo_occ=None) -> None: ...
    def dump_flags(self, verbose=None): ...
    @property
    def nkpts(self): ...
    @property
    def nocc(self): ...
    @property
    def nmo(self): ...
    get_nocc = get_nocc
    get_nmo = get_nmo
    get_frozen_mask = get_frozen_mask
    get_diag = cis_diag
    matvec = cis_matvec_singlet
    kernel = kernel
    def vector_size(self): ...
    def vector_to_amplitudes(self, vector, nkpts=None, nmo=None, nocc=None): ...
    def amplitudes_to_vector(self, r): ...
    def ao2mo(self, mo_coeff=None): ...
    def gen_matvec(self, kshift, eris=None, **kwargs): ...
    def get_init_guess(self, nroots: int = 1, diag=None): ...
    def get_kconserv_r(self, kshift): ...

class _CIS_ERIS:
    fock: Incomplete
    mo_energy: Incomplete
    ovov: Incomplete
    voov: Incomplete
    dtype: Incomplete
    feri1: Incomplete
    def __init__(self, cis, mo_coeff=None, method: str = 'incore') -> None: ...
