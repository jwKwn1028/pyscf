from _typeshed import Incomplete
from pyscf.gw import gw_slow as gw_slow
from pyscf.lib import einsum as einsum

def corrected_moe(eri, k, p): ...

class IMDS(gw_slow.IMDS):
    orb_dims: int
    nk: Incomplete
    nocc: Incomplete
    o: Incomplete
    v: Incomplete
    td_xy: Incomplete
    td_e: Incomplete
    tdm: Incomplete
    def __init__(self, td, eri=None) -> None: ...
    def eri_ov(self, item): ...
    __getitem__ = eri_ov
    def __plain_index__(self, p, spec: bool = True): ...
    def get_rhs(self, p, components: bool = False): ...
    def get_sigma_element(self, omega, p, eta, vir_sgn: int = 1): ...
    def initial_guess(self, p): ...
    @property
    def entire_space(self): ...
kernel = gw_slow.kernel

class GW(gw_slow.GW):
    base_imds = IMDS
