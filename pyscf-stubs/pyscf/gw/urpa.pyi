from _typeshed import Incomplete
from pyscf import df as df, lib as lib, scf as scf
from pyscf.gw.rpa import RPA as RPA
from pyscf.lib import logger as logger
from pyscf.mp import dfump2 as dfump2

einsum = lib.einsum

def make_dielectric_matrix(omega, e_ov, f_ov, eris, blksize=None): ...

class URPA(dfump2.DFUMP2):
    get_e_hf: Incomplete
    kernel: Incomplete
    def make_e_ov(self): ...
    def make_f_ov(self): ...
    def make_dielectric_matrix(self, omega, e_ov=None, f_ov=None, eris=None, max_memory=None, blksize=None): ...
