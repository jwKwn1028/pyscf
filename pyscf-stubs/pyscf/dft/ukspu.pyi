from _typeshed import Incomplete
from pyscf import lib as lib
from pyscf.data.nist import HARTREE2EV as HARTREE2EV
from pyscf.dft import uks as uks
from pyscf.lib import logger as logger
from pyscf.lo.iao import reference_mol as reference_mol

def get_veff(ks, mol=None, dm=None, dm_last: int = 0, vhf_last: int = 0, hermi: int = 1): ...
def energy_elec(mf, dm=None, h1e=None, vhf=None): ...

class UKSpU(uks.UKS):
    get_veff = get_veff
    energy_elec = energy_elec
    to_hf: Incomplete
    U_idx: Incomplete
    U_val: Incomplete
    C_ao_lo: Incomplete
    minao_ref: Incomplete
    alpha: Incomplete
    def __init__(self, mol, xc: str = 'LDA,VWN', U_idx=[], U_val=[], C_ao_lo=None, minao_ref: str = 'MINAO') -> None: ...
    def dump_flags(self, verbose=None): ...
    def Gradients(self): ...
    def nuc_grad_method(self): ...

def linear_response_u(mf_plus_u, alphalist=(0.02, 0.05, 0.08)): ...
