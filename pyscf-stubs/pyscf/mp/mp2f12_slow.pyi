from pyscf import ao2mo as ao2mo, gto as gto, lib as lib
from pyscf.lib import logger as logger
from pyscf.mp import mp2 as mp2
from pyscf.scf import jk as jk
from numpy import ndarray
from pyscf.gto.mole import Mole
from pyscf.scf.hf import RHF
from typing import Tuple

def find_cabs(mol: Mole, auxmol: Mole, lindep: float = 1e-08) -> Tuple[Mole, ndarray]: ...
def trans(eri, mos): ...
def energy_f12(mf: RHF, auxmol: Mole, zeta: float): ...
