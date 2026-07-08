from pyscf import lib as lib, scf as scf
from pyscf.lib import logger as logger
from pyscf.solvent import smd as smd
from numpy import ndarray
from pyscf.solvent.smd import SMD

def get_cds(smdobj: SMD) -> ndarray: ...
