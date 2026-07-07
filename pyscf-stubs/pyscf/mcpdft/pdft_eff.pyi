from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.dft import numint as numint
from pyscf.lib import logger as logger

SWITCH_SIZE: Incomplete
libpdft: Incomplete

class _ERIS:
    mol: Incomplete
    mo_coeff: Incomplete
    ncore: Incomplete
    ncas: Incomplete
    vhf_c: Incomplete
    method: Incomplete
    paaa_only: Incomplete
    aaaa_only: Incomplete
    jk_pc: Incomplete
    verbose: Incomplete
    stdout: Incomplete
    papa: Incomplete
    j_pc: Incomplete
    def __init__(self, mol, mo_coeff, ncore, ncas, method: str = 'incore', paaa_only: bool = False, aaaa_only: bool = False, jk_pc: bool = False, verbose: int = 0, stdout=None) -> None: ...

def get_eff_1body(otfnal, ao, weight, kern, non0tab=None, shls_slice=None, ao_loc=None, hermi: int = 0): ...
def get_eff_2body(otfnal, ao, weight, kern, aosym: str = 's4', eff_ao=None): ...
def get_eff_2body_kl(ot, ao_k, ao_l, weight, kern, symm: bool = False): ...
