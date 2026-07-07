from pyscf import lib as lib
from pyscf.scf import hf as hf
from pyscf.soscf import newton_ah as newton_ah
from pyscf.x2c import x2c as x2c

gen_g_hop_x2chf = newton_ah.gen_g_hop_dhf

def newton(mf): ...

class SecondOrderX2CRHF(newton_ah._CIAH_SOSCF):
    gen_g_hop = gen_g_hop_x2chf
    def update_rotate_matrix(self, dx, mo_occ, u0: int = 1, mo_coeff=None): ...
    def rotate_mo(self, mo_coeff, u, log=None): ...

class SecondOrderX2CUHF(newton_ah._CIAH_SOSCF):
    gen_g_hop = gen_g_hop_x2chf
    def update_rotate_matrix(self, dx, mo_occ, u0: int = 1, mo_coeff=None): ...
    def rotate_mo(self, mo_coeff, u, log=None): ...
