from _typeshed import Incomplete
from pyscf import lib as lib
from pyscf.lib import logger as logger
from pyscf.pbc import tools as tools
from pyscf.pbc.lib.kpts import KPoints as KPoints
from pyscf.scf import addons as mol_addons

SMEARING_METHOD: Incomplete

class _SmearingKSCF(mol_addons._SmearingSCF):
    entropy: Incomplete
    def get_occ(self, mo_energy_kpts=None, mo_coeff_kpts=None): ...
    def get_grad(self, mo_coeff_kpts, mo_occ_kpts, fock=None): ...

def smearing(mf, sigma=None, method=..., mu0=None, fix_spin: bool = False): ...
def smearing_(mf, *args, **kwargs): ...
