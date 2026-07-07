from _typeshed import Incomplete
from pyscf.data import radii as radii
from pyscf.lib import logger as logger
from pyscf.solvent import pcm as pcm
from pyscf.solvent.smd import hartree2kcal as hartree2kcal, solvent_db as solvent_db

sigma_water: Incomplete
sigma_n: Incomplete
sigma_alpha: Incomplete
sigma_beta: Incomplete
sigma_gamma: float
sigma_phi2: float
sigma_psi2: float
sigma_beta2: float
gamma0: float
r_zz: Incomplete

def swtich_function(R, r, dr): ...
def atomic_surface_tension(symbols, coords, n, alpha, beta, water: bool = True): ...
def molecular_surface_tension(beta, gamma, phi, psi): ...
def naive_sasa(mol, rad): ...
def get_cds(smdobj): ...
