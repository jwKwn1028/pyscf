from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib, lo as lo
from pyscf.data.nist import HARTREE2EV as HARTREE2EV
from pyscf.dft.rkspu import reference_mol as reference_mol
from pyscf.lib import logger as logger
from pyscf.pbc.dft import krks as krks

def get_veff(ks, cell=None, dm=None, dm_last: int = 0, vhf_last: int = 0, hermi: int = 1, kpts=None, kpts_band=None): ...
def energy_elec(ks, dm_kpts=None, h1e_kpts=None, vhf=None): ...

class KRKSpU(krks.KRKS):
    get_veff = get_veff
    energy_elec = energy_elec
    to_hf: Incomplete
    U_idx: Incomplete
    U_val: Incomplete
    C_ao_lo: Incomplete
    minao_ref: Incomplete
    alpha: Incomplete
    def __init__(self, cell, kpts=..., xc: str = 'LDA,VWN', exxdiv=..., U_idx=[], U_val=[], C_ao_lo=None, minao_ref: str = 'MINAO', **kwargs) -> None: ...
    def dump_flags(self, verbose=None): ...
    def Gradients(self): ...
    def nuc_grad_method(self): ...

def linear_response_u(mf_plus_u, alphalist=(0.02, 0.05, 0.08)): ...
