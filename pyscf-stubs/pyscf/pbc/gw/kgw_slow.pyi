from _typeshed import Incomplete
from pyscf.gw import gw_slow as gw_slow
from pyscf.lib import direct_sum as direct_sum, einsum as einsum
from pyscf.pbc.gw import kgw_slow_supercell as kgw_slow_supercell
from pyscf.pbc.tdscf.krhf_slow import get_block_k_ix as get_block_k_ix

class IMDS(kgw_slow_supercell.IMDS):
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
    def construct_tdm(self): ...
    def get_sigma_element(self, omega, p, eta, vir_sgn: int = 1): ...
kernel = gw_slow.kernel

class GW(gw_slow.GW):
    base_imds = IMDS
