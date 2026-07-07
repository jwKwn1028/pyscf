from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.lib import logger as logger
from pyscf.pbc.dft import gen_grid as gen_grid, krks as krks, kuks as kuks, multigrid as multigrid, rks as rks
from pyscf.pbc.scf import khf as khf, khf_ksymm as khf_ksymm, kuhf_ksymm as kuhf_ksymm

def get_veff(ks, cell=None, dm=None, dm_last: int = 0, vhf_last: int = 0, hermi: int = 1, kpts=None, kpts_band=None): ...

class KsymAdaptedKUKS(kuks.KUKS, kuhf_ksymm.KUHF):
    reset: Incomplete
    get_veff = get_veff
    kpts: Incomplete
    kmesh: Incomplete
    get_ovlp: Incomplete
    get_hcore: Incomplete
    get_jk: Incomplete
    init_guess_by_chkfile: Incomplete
    dump_chk: Incomplete
    nelec: Incomplete
    get_init_guess: Incomplete
    get_occ: Incomplete
    eig: Incomplete
    get_orbsym: Incomplete
    orbsym: Incomplete
    def __init__(self, cell, kpts=..., xc: str = 'LDA,VWN', exxdiv=..., **kwargs) -> None: ...
    def dump_flags(self, verbose=None): ...
    def energy_elec(self, dm_kpts=None, h1e_kpts=None, vhf=None): ...
    def to_hf(self): ...
KUKS = KsymAdaptedKUKS
